#!/usr/bin/node
import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);
/**
 * Set a key-value pair in redis
 * @param {string} schoolName - key
 * @param {string} value      - value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * retrieves and display the value associated
* with given key in the store.
 * @param {string} schoolName - key to search in the redis store
 */
function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
