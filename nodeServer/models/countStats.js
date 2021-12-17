const mongoose = require('mongoose');

const countStatsSchema = new mongoose.Schema(
  {
    countArticles: {
      type: Number
    },
    countResults: {
      type: Number
    },
    countTrends: {
      type: Number
    },
    countTweets: {
      type: Number
    }
  },
  { collection: 'countStats' }
);

module.exports = mongoose.model('countStats', countStatsSchema);
