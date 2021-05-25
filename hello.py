import json
import random
import pickle
from hashids import Hashids

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'user01',
        'PASSWORD': '12 3456',
        #  在master分支迁移
        # 'HOST': 'localhost',
        #  在develop分支迁移
        'HOST': '192.168.152.138',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
"""
a = ['127.0.0.1', '172.16.165.46', '172.16.165.47', '47.114.102.227']

def encrypt_id(raw_id):
    hash_key = 'Tw2se8LYnyQdUAEn'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_course(raw_id):
    hash_key = 'jTQlYjvfI0ZwYbrI'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_user(raw_id):
    hash_key = 'Tw2se8LYnyQdUAEn'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_helper(raw_id):
    hash_key = 'BBq9kdsdg9gfla15'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_plan(raw_id):
    hash_key = 'GEjW5kMQD6Y3b6bW'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_practice(raw_id):
    hash_key = 't4AY5DXsOOPZzbDe'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_order(raw_id):
    hash_key = 'irH8OndTstU9mtRo'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def encrypt_id_rewardlog(raw_id):
    hash_key = 'JMVyanFwqMAUauCo'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))


def encrypt_id_piece(raw_id):
    hash_key = 'JMVyanFwqMAUauCo'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def decrypt_id_test(encrypted_id):
    hash_key = 'jTQlYjvfI0ZwYbrI'
    crypto = Hashids(salt=hash_key, min_length=24)
    decode_result_array = crypto.decode(encrypted_id)
    if len(decode_result_array) != 1:
        return None
    decode_id = int(decode_result_array[0])
    return decode_id
def decrypt_id_course(encrypted_id):
    hash_key = 'jTQlYjvfI0ZwYbrI'
    crypto = Hashids(salt=hash_key, min_length=24)
    decode_result_array = crypto.decode(encrypted_id)
    if len(decode_result_array) != 1:
        return None
    decode_id = int(decode_result_array[0])
    return decode_id
# a = encrypt_id(5819)
# print(a)

"""
user_5820_token: authorization: EngliteToken 06cb47bb6547d403dc4671c4dbb6cc0933693775
user_5819_token: authorization: EngliteToken 2722e2ab49fd938e65d6dcdee13c7d9c450888b9
user_5823_token: authorization: EngliteToken 3668eb531d994f7c41a65efdb45fe55b82a8181e
user_5768_token: authorization: EngliteToken dcc011570a00c342924296e50d148efab262d34a
user_5819_id:0EZ56Ney2keoldxKl98JrAPR
course_excel_id: 3nV0Pkql58MJ3DXRE4oy26Gr
HELPER： BBq9kdsdg9gfla15
plan_id: rjnbD4Wlq2gY24poBV3NemOy
local: 192.168.1.133:8000
test: beta.pyhot.cn
plan_id: l50zyrVAPbgLlgRG3NXwOKLY
helper_id:4jEgOmbr7pRK5G5noQ1PWqD2
authorization:EngliteToken 06cb47bb6547d403dc4671c4dbb6cc0933693775

EngliteToken 3d75d96390478684e61e7ddd79a345a03b334896   HJD 正式服
EngliteToken 041e95864bc150dbd830f6ffeacb5bdd3eea01ce

excel课程id测试服（228）：laWJoOg0kVXzlowL6QP59byZ
excel课程id正式服（304）：AeWZ27Ey9LMYbYXG6VJna1vz
"""
def gen_hash_key():
    a = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    str_ = ''
    for _ in range(16):
        str_ += random.choice(a)

    return str_

def encrypt_id_test(raw_id):
    hash_key = 'Tw2se8LYnyQdUAEn'
    crypto = Hashids(salt=hash_key, min_length=5)
    return str(crypto.encode(raw_id))

def decrypt_id_test2(encrypted_id):
    hash_key = 'ee4s4gd8iHtux1p8'
    crypto = Hashids(salt=hash_key, min_length=5)
    decode_result_array = crypto.decode(encrypted_id)
    if len(decode_result_array) != 1:
        return None
    decode_id = int(decode_result_array[0])
    return decode_id

if __name__ == '__main__':
    a = decrypt_id_test2('8a6fcbf6bfae8019dc474b6abb0ef560')
    print(a)
    # x = []
    # y = []
    # for i in range(100):
    #     a = encrypt_id_test(i)
    #     x.append(a)
    # print(x)
    # for j in x:
    #     b = decrypt_id_test2(j)
    #     y.append(b)
    # print(y)

    # hash_key = gen_hash_key()
    # print(hash_key)
    # a = encrypt_id_course(328)
    # print(a)
    # # a = encrypt_id_helper(3)
    # print(a)
    # a = encrypt_id_plan(77)
    # print(a)
    # a = encrypt_id_practice(1426)
    # print(a)
    # a = encrypt_id_order(33)
    # print(a)
    # a = encrypt_id(906)
    # print(a)
    # a = encrypt_id_user(906)
    # print(a)
    # a = encrypt_id_rewardlog(55)
    # print(a)
    # hash_key = 't4AY5DXsOOPZzbDe'
    # crypto = Hashids(salt=hash_key, min_length=24)
    # print(str(crypto.decode('AoBzkJdegqXmOVGN9bxKL47j')))

    # a = {"user_id": 1, "searchkey": "我很牛", "searchcontent":[1,2,3,4,4]}
    # b = pickle.dumps(a)
    # c = pickle.loads(b)
    # d = str(a)
    # e = eval(d)
    # print(c,type(c))
    # print(b, type(b))
    # print(d,type(d))
    # print(e, type(e),e['searchcontent'][3])
    # print(decrypt_id_test(264))
    # a = decrypt_id_course('AeWZ27Ey9LMYbYXG6VJna1vz')
    # print(a)


