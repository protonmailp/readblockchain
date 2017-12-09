import redis
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)



step =50
rpc_user ="admin"
rpc_password = "admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))

def getTxsToRedis( height ):
    commands = [["getblockhash", height] for height in range(height,height+step)]
    block_hashes = rpc_connection.batch_(commands)
    blocks = rpc_connection.batch_([["getblock", block_hash] for block_hash in block_hashes])

    for block in blocks:
        btx=block['tx']
        for tx in btx:
            r.lpush("txs",tx)
            print(" {} : {} : {}".format(block['height'], block['hash'],tx))



for j in range(1,498253,step):
    getTxsToRedis(j)


