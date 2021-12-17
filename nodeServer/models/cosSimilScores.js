const mongoose = require('mongoose');

const sourcesScoreSchema = new mongoose.Schema(
  {
    source: {
      type: String
    },
    sumCosSimil: {
      type: Number
    }
  },
  { collection: 'sourcesScore' }
);

module.exports = mongoose.model('sourcesScore', sourcesScoreSchema);
