
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='txids')





rpc_user ="admin"
rpc_password = "admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))

def getTxsToRabbitmq( height ,step):
    commands = [["getblockhash", height] for height in range(height,height+step)]
    block_hashes = rpc_connection.batch_(commands)
    blocks = rpc_connection.batch_([["getblock", block_hash] for block_hash in block_hashes])
    for block in blocks:
        btx=block['tx']
        txheight =str(block['height'])
        for tx in btx:

            channel.basic_publish(exchange='',
                                  routing_key='txids',
                                  body=tx+txheight)



for j in range(389651,500984,50):
    getTxsToRabbitmq(j,50)
    print(j)

connection.close()
