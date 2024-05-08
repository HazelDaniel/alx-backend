#!/usr/bin/node
import { createQueue } from 'kue';

const queue = createQueue();

/**
	sends notification to a specific subscriber
 * @param {string} phoneNumber  - recipient's phone number
 * @param {string} message      - message
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
