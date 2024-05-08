#!/usr/bin/node
import { print, createClient } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

const getAsync = promisify(redisClient.get).bind(redisClient);

/**
 * Set a key-value pair in redis
 * @param {string} schoolName - key
 * @param {string} value      - value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * Gets and display the value associated with given key
 * in redis store - asynchronously.
 * @param {string} schoolName - key to search in redis
 */
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  if (value) console.log(value);
}

/**
 * Entry point into the program
 */
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

const initializer = () => {
  console.log('Redis client connected to the server');
  main();
}

redisClient.on('connect', initializer);
