const mongoose = require('mongoose');

const SearchQuerySchema = new mongoose.Schema(
  {
    dateDownloaded: {
      type: Date
    },
    hashtag: {
      type: String
    },
    rank: {
      type: Number
    }
  },
  { collection: 'trends' }
);

module.exports = mongoose.model('trends', SearchQuerySchema);
