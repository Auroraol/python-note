# -*- coding:utf-8 -*-
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['xdmp']
    collection = db['shop']

    query = {"platform": "dy"}
    results = collection.find(query)
    print(results[0]["plat_shop_id"])
    # for result in results:
    #     print(result["plat_shop_id"])
        # with open('plat_shop_ids.txt', 'w') as file:
        #     for result in results:
        #         file.write(str(result["plat_shop_id"]) + '\n')

    # 关闭客户端连接
    client.close()