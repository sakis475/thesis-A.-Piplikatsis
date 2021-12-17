const mongoose = require('mongoose');

const TopSimilTrendsSchema = new mongoose.Schema(
  {
    articleCategory: {
      type: String
    },
    articleDate: {
      type: Date
    },
    articleLink: {
      type: String
    },
    articleOriginal: {
      type: String
    },
    articleTitle: {
      type: String
    },
    cosSimil: {
      type: Number
    },
    searchQuery: {
      type: String
    },
    resultCompletedDate: {
      type: Date
    },
    dateDownloaded: {
      type: Date
    },
    rank: {
      type: Number
    },
    volume: {
      type: Number
    },
    dateDiff: { type: String },
    bestResultsDate: { type: Date }
  },
  { collection: 'topSimilTrends' }
);

module.exports = mongoose.model('topSimilTrends', TopSimilTrendsSchema);
