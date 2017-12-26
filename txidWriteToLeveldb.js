var levelup = require('levelup')
var leveldown = require('leveldown')
var amqp = require('amqplib/callback_api');
// 1) Create our store
var db = levelup(leveldown('D:\\height'))


var add =function(txid,height){

db.put(txid, height, function (err) {
  if (err) return console.log('Ooops!', err) // some kind of I/O error

  // 3) Fetch by key
  // db.get('name'+i, function (err, value) {
  //   if (err) return console.log('Ooops!', err) // likely the key was not found

  //   // Ta da!
  //   console.log('name=' + value)
  // })
})


}


amqp.connect('amqp://localhost', function(err, conn) {
  conn.createChannel(function(err, ch) {
    var q = 'txids';

    ch.assertQueue(q, {durable: false});

    ch.consume(q, function(msg) {
    	add(msg.content.slice(0,64),msg.content.slice(64))
      console.log(msg.content.slice(0,64)+"  :   "+msg.content.slice(64))
    }, {noAck: true});
  });
});