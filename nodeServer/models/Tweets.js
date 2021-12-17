const mongoose = require('mongoose');

const TweetsSchema = new mongoose.Schema(
  {
    RT: {
      type: Number
    },
    RTCount: {
      type: Number
    },
    date: {
      type: Date
    },
    dateSearched: {
      type: Date
    },
    fullText: {
      type: String
    },
    hashtags: {
      type: Array
    },
    searchQuery: {
      type: String
    },
    userID: {
      type: String
    },
    userScreenName: {
      type: String
    },
    bestResultsDate: {
      type: Date
    }
  },
  { collection: 'topTweets' }
);

module.exports = mongoose.model('topTweets', TweetsSchema);
