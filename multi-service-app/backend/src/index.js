const express = require('express');
const mongoose = require('mongoose');
const Redis = require('ioredis');
const winston = require('winston');

const app = express();
const port = 3000;

// Logging configuration
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ]
});

// MongoDB connection
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Redis connection
const redis = new Redis(process.env.REDIS_URI);

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

app.listen(port, () => {
  logger.info(`Server running on port ${port}`);
});