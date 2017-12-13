import redis
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time
import pika
import json


r = redis.StrictRedis(host='localhost', port=6379, db=0)




rpc_user ="admin"
rpc_password = "admin"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='rawtransactions')


step =500
for i in range(0,300000000,step):
    print(i)
    txs=[]
    heights=[]
    for j in range(step):
        ss = r.rpop("heighttx").decode("utf-8")
        sss= ss.split(':')
        heights.append(sss[0])
        txs.append(sss[1])

    commands = [["getrawtransaction", tx] for tx in txs]
    hexs = rpc_connection.batch_(commands)

    jieguos=[]
    for ii,hex in enumerate(hexs):
        jieguos.append(heights[ii]+":"+txs[ii]+":"+hex)

    for jieguo in jieguos:
        r.lpush("heighttxhex", jieguo)


        # channel.basic_publish(exchange='',
        #                       routing_key='rawtransactions',
        #                       body=json.dumps(body))





    
