# coding = utf-8
"""
@author: zhou
@time:2019/8/24 13:01
@File: details_page.py
"""

import requests
import time
import json
#from pymongo import MongoClient


#conn = MongoClient("mongodb://%s:%s@ds149974.mlab.com:49974/you163" % ('you163', 'you163'))
#db = conn.you163
#mongo_collection = db.iPhone


def details(product_id):
    url = 'https://openapi.vmall.com/rms/comment/getCommentList.json?t=1571369417856'
    #proxy = {"https": "xx.aa.com:8080"}
    try:
        C_list = []
        for i in range(1, 3):
            #data={'userCode':'csqy123456','userPWD':'123456'}
            query = {"pid":"10086471194207","gbomCode":"","type":0,"extraType":1,"pageSize":10,"pageNum":i}
            res = requests.post(url, data=json.dumps(query))
            print(res.encoding)
            res.encoding = 'utf-8'
            print(res.json())
            print(res.status_code)
            print("爬取第 %s 页评论" % i)
            resp=res.json()
            comment = resp['data']['comments']
            #commentlist=comment['content']
            C_list.append(comment)
            time.sleep(1)
            # save to mongoDB
            # try:
            #     mongo_collection.insert_many(commentList)
            # except:
            #     continue
        return C_list
    except:
        raise


if __name__ == '__main__':
    commentlist = details("10086341244716")
    print(commentlist)
