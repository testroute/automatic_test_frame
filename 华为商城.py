# coding = utf-8
"""
@author: wg
@time:2019/10/16
@File: 华为商城.py
"""

import requests
import time
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#修改Windows默认输出，对应GBK can't decode error


def details(product_id):
    url = 'https://openapi.vmall.com/rms/comment/getCommentList.json?t=1571369417856'
    try:
        C_list = []
        for i in range(1, 3):
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

        return C_list
    except:
        raise


if __name__ == '__main__':
    commentlist = details("10086341244716")
    print(commentlist)
