import redis
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

r = redis.StrictRedis(host='localhost', port=6379, db=0)

es = Elasticsearch()


rpc_user ="admin"
rpc_password = "admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))



step =100
for i in range(0,30000000):
    a=[]
    for j in range(step):
        a.append(r.rpop("txs").decode("utf-8"))
    commands = [["getrawtransaction", blocktx,1] for blocktx in a]
    rawtransactions = rpc_connection.batch_(commands)
    bodys = []
    for rawtransaction in rawtransactions:
        body = {
            '_type': 'transactions',
            '_id': rawtransaction['txid'],
            '_op_type': 'index',
            'doc': rawtransaction
        }
        bodys.append(body)
    success, _ = bulk(es, bodys, index='bitcoin')



    
