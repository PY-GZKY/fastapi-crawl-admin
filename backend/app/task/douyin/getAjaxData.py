# encoding:utf-8
import json
import time
import urllib3

urllib3.disable_warnings()

import requests

# from pymongo import MongoClient


class Dy():
    def __init__(self):
        self.r = requests.session()
        self.r.keep_alive = False
        self.headers = {
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
            "Cookie": "odin_tt=4cd6e2e73adfe7cef1081e16b85dfaaebb166734b8b09ba9e7b2ffa7935b67f2de7a2434b01b6f37411b9a4d442a78b0c7254f5d088fbcb798abe89f8b24051e",
        }
        # self.mongo_client = MongoClient("127.0.0.1", 27017, username=None, password=None)
        # self.db = self.mongo_client["抖音"]
        # self.collection = self.db["库里"]

    # def save_to_mongodb(self,item):
    #     if item:
    #         if self.collection.insert_one(item):
    #             print("成功存储到MONGODB", item)
    #         else:
    #             print("存储到MONGODB失败", item)

    def getHtml(self, url):
        try:
            resp = self.r.get(url, headers=self.headers, timeout=15)
            return resp.text
        except Exception as e:
            print(e)

    def parse(self, result, old_data):
        json_result = json.loads(result)
        old_data["抖音号"] = json_result.get("user_info").get("unique_id")
        old_data["用户签名"] = json_result.get("user_info").get("signature")
        old_data["累计点赞数"] = json_result["user_info"]["total_favorited"]
        old_data["抖音粉丝"] = json_result["user_info"]["follower_count"]
        old_data["作品数"] = json_result["user_info"]["aweme_count"]
        old_data["关注数"] = json_result["user_info"]["following_count"]
        print(old_data)
        # self.save_to_mongodb(old_data)

    def run(self):
        for _ in range(1, 5):
            html = self.getHtml(
                f"https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid=MS4wLjABAAAAOzdObrGxGAyRe0iT5MmYjEBA6s76nCwPY4CwMzakG9aDZUJsrwV8fxverGHwscue")
            self.parse(html, {})
            time.sleep(3)
        return {'success': True, 'code': 200, 'message': '爬取成功'}


if __name__ == "__main__":
    T = Dy()
    T.run()
