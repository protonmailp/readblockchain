const Client = require('bitcoin-core');
const _ = require("underscore")
const client = new Client({ port: 8332 ,
    username:"admin",
    password:"admin"});

client.getInfo().then((help) => console.log(help.version))


const batch = [
    { method: 'getrawtransaction', parameters: ["0c5e4cb78d3696fd55070d26bf11814b4ec9aee7dc585c7698b8fb11533ff6ad"] }
   // { method: 'getnewaddress', parameters: [] }
]

client.command(batch).then((responses)=>console.log(responses))

a=_.map([1, 2, 3], function(num){ return num*8 });

_.each(a,function(a){console.log(a)})

var abatch =[]
for(var i=498000;i<498206;i++){

    abatch.push({ method: 'getblockhash', parameters: [i] })

}

console.log(abatch)

client.command(abatch).then(function(responses){
    bbatch =_.map(responses,function(blockhash){ return    { method: 'getblock', parameters: [blockhash] }    })


})




