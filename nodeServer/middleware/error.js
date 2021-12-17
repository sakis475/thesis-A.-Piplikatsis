const ErrorResponse = require('../utils/errorResponse');

const errorHandler = (err, req, res, next) => {
  // Spread Syntax "...", here it copies the object.
  let error = { ...err };

  //The err.message is not an accessible object property..
  error.message = err.message;

  console.log(err.message);
  //console.log(err);

  console.log('error stack: ', err.stack);

  console.log(`error name is: ${err.name}`);

  // Mongoose bad ObjectId
  if (err.name === 'CastError') {
    const message = `Resource not found with id of ${err.value}`;

    error = new ErrorResponse(message, 404);
  }

  // Mongoose dublicate key
  if (err.code === 11000) {
    const message = `Dublicate key value entered`;
    error = new ErrorResponse(message, 400);
  }

  // Mongoose validation error
  if (err.name === 'ValidationError') {
    const message = Object.values(err.errors).map((val) => val.message);
    error = new ErrorResponse(message, 400);
  }
  res.status(error.statusCode || 500).json({
    success: false,
    error: error.message || 'server Error'
  });
};

module.exports = errorHandler;
