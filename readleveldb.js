var levelup = require('levelup')
var leveldown = require('leveldown')
var amqp = require('amqplib/callback_api');

// 1) Create our store
var db = levelup(leveldown('D:\\height'))



db.createReadStream()
  .on('data', function (data) {
  
    console.log(data.key.toString('utf8'), ':', data.value.toString('utf8'))
  })
  .on('error', function (err) {
    console.log('Oh my!', err)
  })
  .on('close', function () {
    console.log('Stream closed')
  })
  .on('end', function () {
    console.log('Stream ended')
  })







