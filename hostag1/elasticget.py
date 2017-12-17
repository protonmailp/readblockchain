from elasticsearch import Elasticsearch
es = Elasticsearch()

# res = es.get(index="bitcoin", doc_type='transactions', id="7ff90356a1da968e48dd91aad6aa56a9ea36fa8ab0dea43fd6fbf5c5b7dfd263")
# print(res["_source"]['doc']['vout'])

# 1MyAwSkfdnTsV2uAsHiHMNcxqYhtWwNWSQ

res = es.search(index="bitcoin", body={"query": {"match_phrase": {  "addresses":"1MyAwSkfdnTsV2uAsHiHMNcxqYhtWwNWSQ"    }}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"])

print("Got %d Hits:" % res['hits']['total'])