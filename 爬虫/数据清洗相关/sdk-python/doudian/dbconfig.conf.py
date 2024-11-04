# -*- coding:utf-8 -*-
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    # 连接到数据库，如果数据库不存在，MongoDB会自动创建
    db = client['xdmp']

    # 连接到集合，如果集合不存在，MongoDB会自动创建
    collection = db['shop']

    query = {"platform": "dy"}
    results = collection.find(query)

    for result in results:
        print(result["plat_shop_id"])
        # with open('plat_shop_ids.txt', 'w') as file:
        #     for result in results:
        #         file.write(str(result["plat_shop_id"]) + '\n')

    # 关闭客户端连接
    client.close()