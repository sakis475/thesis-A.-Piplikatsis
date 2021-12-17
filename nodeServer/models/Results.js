const mongoose = require('mongoose');

const ResultsSchema = new mongoose.Schema(
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
    freshness_trend: {
      type: String
    },
    dateDiff: { type: String },
    bestResultsDate: { type: Date }
  },
  { collection: 'resultsLastAll' }
);

module.exports = mongoose.model('resultsLastAll', ResultsSchema);
