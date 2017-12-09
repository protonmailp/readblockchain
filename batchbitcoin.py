from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


es = Elasticsearch()
# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user ="admin"
rpc_password = "admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))
# best_block_hash = rpc_connection.getbestblockhash()
# print(rpc_connection.getblock(best_block_hash))

# batch support : print timestamps of blocks 0 to 99 in 2 RPC round-trips:
def getbitcointoelastic( i ):
    commands = [["getblockhash", i]]
    block_hashes = rpc_connection.batch_(commands)
    blocks = rpc_connection.batch_([["getblock", h] for h in block_hashes])
    # block_times = [ block["time"] for block in blocks ]
    # # print(block_times)
    # for block_time in block_times:
    #     print(block_time)

    for block in blocks:
        #    print block['tx']
        commandss = [["getrawtransaction", blocktx] for blocktx in block['tx']]
        btx=block['tx']
        rawtransactions = rpc_connection.batch_(commandss)
        print len(rawtransactions)
        bodys = []
        for rawtransaction in rawtransactions:
            body = {
                '_type': 'transactions',
                '_id': 1,
                '_op_type': 'index',
                'doc': rawtransaction
            }
            bodys.append(body)
            # print body['_id']
            # print body['doc']

 #       success, _ = bulk(es, bodys, index='bitcoin')




#for i in range(1,4980000,5):
for i in range(498000,498100):
    getbitcointoelastic(i)
    print i

# a = ['a','b','c','d','e','f']
# # with indexes
# for (i, a) in enumerate(a):
#     print i, a






