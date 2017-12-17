from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()



from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time


rpc_user= "admin"
rpc_password ="admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))



def puttoelastic(tx,body):
	es.index(index="bitcoin", doc_type='transactions', id=tx, body=body)
	

def getheightandputtoelastic(height):
	block = rpc_connection.getblock(rpc_connection.getblockhash(height))
	txs = block["tx"]
	for tx in txs:
		rawtransaction = rpc_connection.getrawtransaction(tx)
		body= {'rt':rawtransaction}
		puttoelastic(tx,body)
    

#getheightandputtoelastic(1231539)


#getheightandputtoelastic(1231545)
for j in range(1,495855):
	getheightandputtoelastic(j)


#curl -XPUT 'localhost:9200/bitcoin?pretty' -H 'Content-Type: application/json' -d' { "settings": { "number_of_shards" : 3, "number_of_replicas" : 0 } } '
#curl -XDELETE 'localhost:9200/bitcoin?pretty'







