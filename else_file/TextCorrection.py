# -*- coding:utf-8 -*-
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import json
import requests
import intNodeInterface
import cyberdog_gpt
class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


class WebsocketDemo:
    def __init__(self,APPId,APISecret,APIKey,Text,dict_corrected):
        self.appid = APPId
        self.apisecret = APISecret
        self.apikey = APIKey
        self.text = Text
        self.dict = dict_corrected
        self.url = 'https://api.xf-yun.com/v1/private/s9a87e3ec'

    # calculate sha256 and encode to base64
    def sha256base64(self,data):
        sha256 = hashlib.sha256()
        sha256.update(data)
        digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
        return digest


    def parse_url(self,requset_url):
        stidx = requset_url.index("://")
        host = requset_url[stidx + 3:]
        schema = requset_url[:stidx + 3]
        edidx = host.index("/")
        if edidx <= 0:
            raise AssembleHeaderException("invalid request url:" + requset_url)
        path = host[edidx:]
        host = host[:edidx]
        u = Url(host, path, schema)
        return u


    # build websocket auth request url
    def assemble_ws_auth_url(self,requset_url, method="POST", api_key="", api_secret=""):
        u = self.parse_url(requset_url)
        host = u.host
        path = u.path
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        #print(date)
        # date = "Thu, 12 Dec 2019 01:57:27 GMT"
        signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
        #print(signature_origin)
        signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            api_key, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        #print(authorization_origin)
        values = {
            "host": host,
            "date": date,
            "authorization": authorization
        }

        return requset_url + "?" + urlencode(values)


    def get_body(self):
        body =  {
            "header": {
                "app_id": self.appid,
                "status": 3,
                #"uid":"your_uid"
            },
            "parameter": {
                "s9a87e3ec": {
                    #"res_id":"your_res_id",
                    "result": {
                        "encoding": "utf8",
                        "compress": "raw",
                        "format": "json"
                    }
                }
            },
            "payload": {
                "input": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "plain",
                    "status": 3,
                    "text": base64.b64encode(self.text.encode("utf-8")).decode('utf-8')
                }
            }
        }
        return body
    def replace_text(self,start_index, wrong_text, correct_text):
        # 将字符串切片为两部分：从开头到指定位置和从指定位置到结尾
        first_part = wrong_text[:start_index]
        second_part = wrong_text[start_index:start_index + len(correct_text)]
        # 将第二部分替换为正确文本
        new_text = first_part + correct_text
    
        # 将剩余部分拼接在一起以创建新的字符串
        if len(wrong_text) > start_index + len(correct_text):
            new_text += wrong_text[start_index + len(correct_text):]
    
        # 返回新的字符串
        return new_text
    
    def get_result(self):
        request_url = self.assemble_ws_auth_url(self.url, "POST", self.apikey, self.apisecret)
        headers = {'content-type': "application/json", 'host':'api.xf-yun.com', 'app_id':self.appid}
        body = self.get_body()
        response = requests.post(request_url, data = json.dumps(body), headers = headers)
        # print('onMessage：\n' + response.content.decode())
        tempResult = json.loads(response.content.decode())
        # print(base64.b64decode(tempResult['text']).decode())
        key_str= base64.b64decode(tempResult['payload']['result']['text']).decode()
        key_text = eval(key_str)
    
        # 获取嵌套列表
        for key in key_text:
            if not key_text[key]:
                continue
        
            else:
                for nested_list in key_text[key]:
                   
                    start_index = nested_list[0]
                    wrong_text = self.text
                    correct_text = nested_list[2]
                    new_text = self.replace_text(start_index, wrong_text, correct_text)
                    self.text = new_text
        self.dict['text'] = self.text
        print("识别后的问题为"+ self.text )
    
        with open('data_corrected.json', 'w') as f:
            json.dump(self.dict,f)
    
def Correct(node: intNodeInterface.interactionNodeInterface, req: str):
    #控制台获取
    APPId = "9ffcb3f8"
    APISecret = "YzE5YzkwZDI3NTE0Y2QzMTBkNjQ2MzYx"
    APIKey = "9f3126ede8284c7c91a3e1077bc29aa2"

    #需纠错文本
    with open('data_incorrected.json', 'r') as f:
        dict_corrected = json.load(f)
        Text = dict_corrected['text']
    demo = WebsocketDemo(APPId,APISecret,APIKey,Text,dict_corrected)
    result = demo.get_result()
    
    cyberdog_gpt.interact(node, req)




