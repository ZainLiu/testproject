import json

import requests



def data_upload(data):
    """数据上传"""
    headers = {'Content-Type': 'application/json'}
    result = requests.post('http://172.16.165.46/mk-collect', json=data, headers=headers)
    res = json.loads(result.text)
    if res['code'] != 200:
        return res['cnmsg']
    else:
        return 'success'
if __name__ == '__main__':
    data = '{"m": "/report/questionnaire", "v": 1, "p": {"common": {"user": 4566232, "request_id": "1617092390334566232", "sid": "6e85bf3f02a16af7a87669fca8af8b2795965f3c", "platform": "wechat", "ip": "221.226.177.146", "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "time": 1617092390}, "event": {"gender": 2, "occupation": "\u4eba\u4e8b/\u8d22\u52a1/\u884c\u653f", "schooling": "\u5927\u5b66\u672c\u79d1", "province": "\u6c5f\u82cf\u7701", "city": "\u5357\u4eac\u5e02", "age": "", "profession_category": "", "studying_reason": "\u63d0\u9ad8\u6280\u672f\u5b9e\u529b\uff0c\u4e0d\u5728\u5927\u6570\u636e\u65f6\u4ee3\u843d\u4f0d ", "birth_year": "1975"}}}'
    data = json.loads(data)
    print(data)
    res = data_upload(data)
    print(res)