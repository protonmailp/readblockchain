var levelup = require('levelup')
var leveldown = require('leveldown')
//var conv = require('binstring');
// 1) Create our store
var db = levelup(leveldown('./.bitcoin/testnet3/chainstate'))

// 2) Put a key & value
db.createReadStream()
  .on('data', function (data) {
 	console.log(data.key.toString('hex'), '=', data.value.toString('hex'))
  // console.log(data.value.toString('hex'))
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


 // db.createKeyStream()
 //  .on('data', function (data) {





   
 //  })

 // db.get('4300bff9b3df5fcd32a803ef290b3dd6ee92ecfb71d97d8cae1ec079ae06d62cab62', function (err, value) {
 //    if (err) return console.log('Ooops!', err) // likely the key was not found

 //    // Ta da!
 //    console.log('name=' + value)
 //  })

 // console.log("bffbdd052b16703c9b2df5a7084abf7e79d465a7551b5f299179720bf68b".length)
// //  key= 4300bff9b3df5fcd32a803ef290b3dd6ee92ecfb71d97d8cae1ec079ae06d62cab62
// // key= 4300bff9b3df5fcd32a803ef290b3dd6ee92ecfb71d97d8cae1ec079ae06d62cab63
// // key= 4300bffbdd052b16703c9b2df5a7084abf7e79d465a7551b5f299179720bf68bfd00
// // key= 4300bffbdd052b16703c9b2df5a7084abf7e79d465a7551b5f299179720bf68bfd01


// = 622f2af7db73dafcedefc0c32726536680fd84fc04424d6c060000000000000000
// key= 622f2b09cd44b2a16874f643f2adb69acecf311c6b06bd18e33f00000000000000
// key= 622f2b23084406a39cddd2d22b15bae845891b13b14056d9100000000000000000
