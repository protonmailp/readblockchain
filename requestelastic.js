var elasticsearch = require('elasticsearch');
var client = new elasticsearch.Client({
  host: 'localhost:9200',
  log: 'trace'
});

client.search({
  index: 'bitcoin',
  type:'transactions',
  q: '*:1MyAwSkfdnTsV2uAsHiHMNcxqYhtWwNWSQ'
}, function (error, response) {
//	console.log(response)
    for( var i =0;i<response.hits.total;i++){

      console.log(response.hits.hits[i]._id)
    }

});






// c24410a736c3ce2a1f3fa62e1649b6ec72b0af91fdf0cb20feea00c8c7999024
// 751673c363080e0e18d6e11cbb49537e68e4162de615aab245a8b6f59c425904
// 1c4942e6e7bc675b0023801d41b476b1faf9efec30b23536362663bab7b48514
// 2b24de0fd74c47b81cce353ce1a7c378d493a0cb1ead3e3e0c19e323aa8c66e6
// ff2b65f34d67f8fd2b69c196b21cb8d07058d39877d2409b96f7dea65a7f8101
// 7ff90356a1da968e48dd91aad6aa56a9ea36fa8ab0dea43fd6fbf5c5b7dfd263
// 74483f76878e15c57ce27a0f1f26c6d5ad66734460cd05b9bcb298960be3e6dd
// c3fc801420a79883421f7225f428de8e9832c2446391fd7d24a9b2237307852c

