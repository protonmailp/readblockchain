import  json
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)




# a=[]
#
# for i in range(10):
#     r.lpush("shuju","1d2b950c432ecc2d42c5b38bf5cbd06c003fd7702c332b97bfd12f462f90256e"+str(i))
#
#
#
# for i in range(10):
#     print(r.rpop("shuju"))


# for i in range(1,1254223,50):
#     print(i)

for i in range(10000000):
    s =str(i)+":"+"e988229a20070b0d7e68c0921cd34c713ff2647dbbea4084f44a1d56362b7892"+":"+"01000000011fb03965f6653d1f7ede65267a5bdc2fae53fd5761df6e4582d77a8225526d2a010000006a47304402201d1ae5400946dd0823d37831262b2b3e8808b01d14e182d9271bfeff19aedb370220093b268a6171089296d107caa9f03e361a3fc63caf1c82f5e9f278c54d92391b012103110a8a4714ddc71c79ca1d5dd6beb69137a0e5a6b7e3da9fd1bbe01f00a049cdfeffffff02400d0300000000001976a914c507ea81d716f4962b20ade707f8250300d27aa388aca498760b000000001976a9145a33674e5643d42f50bd4619fd25d769d19e65c088ac00000000"
    r.lpush("shuju",s)
    print(i)




