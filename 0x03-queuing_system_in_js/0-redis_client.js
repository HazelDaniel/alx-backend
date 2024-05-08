#!/usr/bin/node
import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

redisClient.on('connect', () => console.log('Redis client connected to the server'));
