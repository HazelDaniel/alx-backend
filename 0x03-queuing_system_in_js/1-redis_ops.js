#!/usr/bin/node
import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
