import requests
import json
from views import third

apiKey = "YOUR-APIKEY"  # YOUR-APIKEY

userId = "nature"  # 名称
data = {
    # 请求的类型 0 文本 1 图片 2 音频
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "你是谁"
        }
    },
    "userInfo": {
        "apiKey": apiKey,
        "userId": userId
    }
}

tuling_url = "http://openapi.tuling123.com/openapi/api/v2"

res = requests.post(tuling_url,json=data)  # 请求url
# 将返回信息解码
res_dic = json.loads(res.content.decode("utf-8"))  # type:dict
# 得到返回信息中的文本信息
res_type = res_dic.get("results")[0].get("values").get("text")
# 调用text2audio函数
third.text2audio(res_type)
