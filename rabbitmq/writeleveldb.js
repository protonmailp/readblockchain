var levelup = require('levelup')
var leveldown = require('leveldown')
var amqp = require('amqplib/callback_api');
// 1) Create our store
var db = levelup(leveldown('./mydb'))

// 2) Put a key & value



var add =function(i){

db.put('name'+i, i+"  bbbbbbbbbb", function (err) {
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
    var q = 'hello';

    ch.assertQueue(q, {durable: false});
    console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q);
    ch.consume(q, function(msg) {
    	add(msg.content.toString())
      console.log(" [x] Received %s", msg.content.toString());
    }, {noAck: true});
  });
});