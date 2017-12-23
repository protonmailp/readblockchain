
# import leveldb

# # leveldb.DestroyDB('./db')
# db = leveldb.LevelDB('./.bitcoin/testnet3/blocks/index')
# # db.Put('hello','world')
# # print(db.Get('1'))
# # for i in range(10000000):
# # 	db.Put(str(i),str(i%10)*50)
# # 	print i

# it = db.iterator(include_value=False)
# print next(it)

# import plyvel
# db = plyvel.DB('./.bitcoin/testnet3/chainstate/', create_if_missing=True)


def reserve(s):

	ss=[]
	for i in range(0,len(s),2):
		ss.append(s[i]+s[i+1])
	sss=""
	for  s in ss:
		sss=s+sss
	print sss[:-2]
	print len(sss[:-2])

s= "620580609ccf46add7b84fa63aa071e609be677f3fa545c7183e88040000000000"
#000000000004883e18c745a53f7f67be09e671a03aa64fb8d7ad46cf9c608005    BlockHash 
#889354bee907801d0542a8d7967485c3ce0800000020dac484647c96fc6040e05adf7057bb4da148483465587dee50edcc0000000000b72753ffba0ce209c63ac628a0c0e297eb7948ab773612520efb9fdb88fbd7a0533244582865021c1264147e


reserve(s)

s="889354bee907801d0542a8d7967485c3ce0800000020dac484647c96fc6040e05adf7057bb4da148483465587dee50edcc0000000000b72753ffba0ce209c63ac628a0c0e297eb7948ab773612520efb9fdb88fbd7a0533244582865021c1264147e"
reserve(s)
#7e1464121c02652858443253a0d7fb88db9ffb0e52123677ab4879eb97e2c0a028c63ac609e20cbaff5327b70000000000cced50ee7d5865344848a14dbb5770df5ae04060fc967c6484c4da2000000008cec3857496d7a842051d8007e9be549388


#43008a32b7375e67b32266e2cdc27635c4c3e77b46f8385162aa29c82737aaae8601 = e61eecffbe7a9eaf674a94a95e2ff904178a36e2e889ccde2e640e97f
s="43008a32b7375e67b32266e2cdc27635c4c3e77b46f8385162aa29c82737aaae8601"

reserve(s)
#0186aeaa3727c829aa625138f8467be7c3c43576c2cde26622b3675e37b7328a00  Transaction id txid
s="e61eecffbe7a9eaf674a94a95e2ff904178a36e2e889ccde2e640e97f"

reserve(s)
# a ="0000000000000000006a22eff01aa49398422045a299139cdb5d2a5cc8c9f106"

# print len(a)

#print len("3e5eeb24877f40f1f9429eec42a4d11aae867570b783f90180d2220b41f9e7ec")




