
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.lpush("shuju","1d2b950c432ecc2d42c5b38bf5cbd06c003fd7702c332b97bfd12f462f90256e")
s = r.rpop("shuju")

print(s)
a=[]

for i in range(100000000):
    r.lpush("shuju","1d2b950c432ecc2d42c5b38bf5cbd06c003fd7702c332b97bfd12f462f90256e"+str(i))



for i in range(100000000):
    print(r.rpop("shuju"))



