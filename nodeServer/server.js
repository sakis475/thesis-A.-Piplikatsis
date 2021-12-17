const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const dayjs = require('dayjs');

const errorHandler = require('./middleware/error');
const connectDB = require('./config/db');

//Load env vars
dotenv.config({ path: './config/config.env' });

const ResultsSchema = require('./models/Results');
const TweetsSchema = require('./models/Tweets');
const searchQuerySchema = require('./models/SearchQuery');
const TopSimilTrendsSchema = require('./models/TopSimilTrends');
const countStatsSchema = require('./models/countStats');
const sourcesScoreSchema = require('./models/cosSimilScores');

//Connect to database
connectDB();

const app = express();

app.use(cors());

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(errorHandler);

app.use(express.static('dist/twitter-articles'));

const PORT = process.env.PORT;

const server = app.listen(
  PORT,
  console.log(`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`)
);

let results = ResultsSchema;

let topTweets = TweetsSchema;

let searchQuery = searchQuerySchema;

let trends;

let topSimilTrends = TopSimilTrendsSchema;

let countStats = countStatsSchema;

let sourcesScore = sourcesScoreSchema;

app.get('/', (req, res) => {
  res.sendFile('index.html', { root: __dirname });
});

let bestResultsDate = '';
// app.post('/', (req, res) => {
//   console.log('POST work!!!');
// });

app.get('/trends', function (req, res, next) {
  if (req.query.data == '') {
    results
      .findOne({})
      .sort({ bestResultsDate: -1 })
      .limit(1)
      .then((maxDate) => {
        results.find(
          //resultCompletedDate: resultCompletedDate
          { bestResultsDate: maxDate.bestResultsDate },
          '-_id searchQuery rank volume freshness_trend dateDiscovered_trend bestResultsDate',
          {
            skip: 0, // Starting Row
            limit: 25, // Ending Row
            sort: {
              rank: 1 //Sort by Rank ASC
            }
          },
          function (err, result) {
            trends = [...new Set(result.map((item) => item.searchQuery))];
            bestResultsDate = result[0].bestResultsDate;
            res.send(JSON.stringify(result));
          }
        );
      });
  } else if (req.query.data) {
    bestResultsDate = req.query.data;

    results.find(
      //resultCompletedDate: resultCompletedDate
      { bestResultsDate: bestResultsDate },
      '-_id searchQuery rank volume freshness_trend dateDiscovered_trend bestResultsDate',
      {
        skip: 0, // Starting Row
        limit: 25, // Ending Row
        sort: {
          rank: 1 //Sort by Rank ASC
        }
      },
      function (err, result) {
        trends = [...new Set(result.map((item) => item.searchQuery))];

        res.send(JSON.stringify(result));
      }
    );
  }
});

app.get('/articles', function (req, res, next) {
  results.find(
    { bestResultsDate: bestResultsDate },
    '-_id searchQuery articleTitle articleLink articleDate articleCategory articleSource cosSimil diffDate bestResultsDate',
    {
      skip: 0, // Starting Row
      limit: 25 // Ending Row
    },
    function (err, result) {
      res.send(JSON.stringify(result));
    }
  );
});

app.get('/tweets', function (req, res, next) {
  topTweets.find(
    { bestResultsDate: bestResultsDate },
    '-_id RTCount date dateSearched fullText hashtags searchQuery tweetID userID userScreenName bestResultsDate',
    {
      limit: 5000,
      sort: {
        RTCount: -1 //Sort by RTCount DESC
      }
    },
    function (err, result) {
      res.send(JSON.stringify(result));
    }
  );
});

app.get('/searchquery', function (req, res, next) {
  const hashtag = req.query.data;

  //results.distinct('bestResultsDate', function (error, dates) {
  //bestResultsDate = dates.sort().reverse()[parseInt(req.query.data)];
  if (hashtag) {
    searchQuery.find(
      { hashtag: hashtag },
      '-_id dateDownloaded hashtag rank',
      {
        limit: 5000,
        sort: {
          dateDownloaded: 1 //Sort by dateDownloaded ASC
        }
      },
      function (err, result) {
        res.send(JSON.stringify(result));
      }
    );
  } else {
    searchQuery
      .find({
        dateDownloaded: {
          $gte: dayjs().subtract(7, 'day').format('YYYY-MM-DD')
        }
      })
      .distinct('hashtag', function (err, result) {
        res.send(JSON.stringify(result));
      });
  }
});

app.get('/topsimiltrends', function (req, res, next) {
  topSimilTrends.find({}, function (err, result) {
    res.send(JSON.stringify(result));
  });
});

String.prototype.allReplace = function (obj) {
  var retStr = this;
  for (var x in obj) {
    retStr = retStr.replace(new RegExp(x, 'g'), obj[x]);
  }
  return retStr;
};

function makeRegexSearch(searchKeyword) {
  //^(?=.*λεξηΑ)(?=.*λεξηΒ)(?=.*λέξηΓ)...
  queryRegex = '^(?=.*';

  searchKeyword = searchKeyword.map((keyword) => {
    return keyword.allReplace({
      α: '[αά]',
      ε: '[εέ]',
      η: '[ηή]',
      ι: '[ιί]',
      ο: '[οό]',
      υ: '[υύ]',
      ω: '[ωώ]'
    });
  });

  for (let index in searchKeyword) {
    if (parseInt(index) + 1 === searchKeyword.length) {
      queryRegex += searchKeyword[index] + ')...';
    } else {
      queryRegex += searchKeyword[index] + ')(?=.*';
    }
  }
  return queryRegex;
}

const searchKeywords = ['ελλάδα'];

app.post('/searcharticlesbykeywords', function (req, res, next) {
  const searchKeywords = req.body.searchKeywords.split(' ');
  const hashtagKeyword = req.body.searchKeywords;
  const searchFieldToggle = req.body.searchType; //(articleTitle, searchQuery)
  const sortBy = JSON.parse(req.body.sortObject);
  console.log(searchKeywords);
  console.log(sortBy);
  if (searchFieldToggle === 'articleTitle' && searchKeywords.length > 0) {
    results
      .aggregate([
        {
          $match: {
            articleTitle: {
              $regex: makeRegexSearch(searchKeywords),
              $options: 'i'
            }
          }
        },
        {
          $sort: { cosSimil: -1 }
        },
        {
          $group: {
            _id: '$articleLink',
            doc: { $first: '$$ROOT' }
          }
        },
        {
          $replaceRoot: {
            newRoot: '$doc'
          }
        }
      ])
      .sort(sortBy)
      .exec(function (err, result) {
        if (result) {
          res.send(JSON.stringify(result.slice(0, 10)));
        } else {
          res.send('none_found');
        }

        //console.log(result);
      });
  } else if (searchFieldToggle === 'searchQuery' && hashtagKeyword.length > 0) {
    results
      .aggregate([
        {
          $match: {
            searchQuery: {
              $regex: hashtagKeyword,
              $options: 'i'
            }
          }
        },
        {
          $sort: { cosSimil: -1 }
        },
        {
          $group: {
            _id: '$searchQuery',
            doc: { $first: '$$ROOT' }
          }
        },
        {
          $replaceRoot: {
            newRoot: '$doc'
          }
        }
      ])
      .sort(sortBy)
      .exec(function (err, result) {
        if (result) {
          res.send(JSON.stringify(result.slice(0, 10)));
        } else {
          res.send('none_found');
        }
      });
  }
});

app.get('/daterangeresults', (req, res) => {
  results.aggregate(
    [
      {
        $group: {
          _id: null,
          max_date: { $max: '$bestResultsDate' },
          min_date: { $min: '$bestResultsDate' }
        }
      },
      {
        $project: {
          _id: 0
        }
      }
    ],
    function (err, result) {
      res.send(JSON.stringify(result));
    }
  );
});

app.post('/resultdates', (req, res) => {
  const date = dayjs(new Date(req.query.data));

  results
    .find({
      bestResultsDate: {
        $gte: date,
        $lt: date.add(1, 'day')
      }
    })
    .distinct('bestResultsDate', function (err, timestamps) {
      res.send(JSON.stringify(timestamps));
    });
});

//count tweets, count articles...
app.get('/countstats', (req, res) => {
  countStats
    .find({})
    .select({ _id: 0 })
    .exec(function (err, counts) {
      res.send(JSON.stringify(counts));
    });
});

//sources score of cosine similarity...
app.get('/sourcesscore', (req, res) => {
  sourcesScore
    .find({})
    .select({ _id: 0 })
    .exec(function (err, scores) {
      res.send(JSON.stringify(scores));
    });
});

app.get('/gettrendscorrespondingarticle', (req, res) => {
  const trend = req.query.data;
  results
    .findOne({
      searchQuery: trend,
      dateDownloaded: {
        $gte: dayjs().subtract(10, 'day').format('YYYY-MM-DD')
      }
    })
    .sort('-cosSimil') //find the max cosSimil of that trend
    .exec(function (err, scores) {
      res.send(JSON.stringify(scores));
    });
});

//repeated trends
app.get('/freshnesstrend', (req, res) => {
  const freshness = req.query.data;

  let matchOption;

  if (freshness == 'old') {
    matchOption = {
      freshness_trend: freshness,
      bestResultsDate: {
        $gte: dayjs().subtract(3, 'day').toDate()
      }
    };
  } else if (freshness == 'new') {
    matchOption = {
      freshness_trend: freshness,
      bestResultsDate: {
        $gte: dayjs().subtract(3, 'day').toDate()
      }
    };
  } else {
    res.send('bad query, freshness value not (new | old)');
    return;
  }
  console.log(matchOption);

  results
    .aggregate(
      [
        {
          $match: matchOption
        },
        { $project: { _id: 0, articleOriginal: 0 } },
        {
          $sort: { cosSimil: -1 }
        },
        {
          $group: {
            _id: '$searchQuery',
            doc: { $first: '$$ROOT' }
          }
        },
        {
          $replaceRoot: {
            newRoot: '$doc'
          }
        }
      ],
      { allowDiskUse: true }
    )
    .sort({ dateDiscovered_trend: -1 })
    .exec(function (err, result) {
      if (err) {
        console.log(err);
      }

      if (result) {
        res.send(JSON.stringify(result));
      } else {
        res.send('none_found');
      }
    });
});

//Handle unhandled promise rejections
process.on('unhandledRejection', (err, promise) => {
  console.log(`Error:  ${err.message}`);
  //Close server & exit process
  server.close(() => process.exit(1));
});
