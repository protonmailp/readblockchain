import psycopg2

conn = psycopg2.connect("dbname=simple_db user=postgres password=12eX12EJwSkTR8twwZbVusHLPYRbobbfpa")

cur = conn.cursor()

#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

#cur.execute("INSERT INTO people (txid,hex) VALUES ('txid111111111111111','hex12333333333333333')")
step =2000

for j in range(10048487,100000000,step):
    for i in range(j,j+step):
        cur.execute("INSERT INTO people (txid,hex) VALUES  (%s, %s)", ('txid' + str(i)+"b"*100, 'hex' + str(i)+"a"*500))
        conn.commit()







cur.close()

conn.close()