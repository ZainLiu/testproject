import hashlib
import time
import base64
import json
from hashids import Hashids

def encrypt_id(raw_id):
    hash_key = 'PP75O7XsVawZzbDe'
    crypto = Hashids(salt=hash_key, min_length=24)
    return str(crypto.encode(raw_id))

def decrypt__sheet_id(encrypted_id):
    hash_key = 'PP75O7XsVawZzbDe'
    crypto = Hashids(salt=hash_key, min_length=24)
    decode_result_array = crypto.decode(encrypted_id)
    if len(decode_result_array) != 1:
        return None
    decode_id = int(decode_result_array[0])
    return decode_id

def decrypt__refund_id(encrypted_id):
    hash_key = 'irH8OndTstU9mtRo'
    crypto = Hashids(salt=hash_key, min_length=24)
    decode_result_array = crypto.decode(encrypted_id)
    if len(decode_result_array) != 1:
        return None
    decode_id = int(decode_result_array[0])
    return decode_id



if __name__ == '__main__':
    # 解密sheetid
    # print(decrypt__sheet_id('123444'))
    print(decrypt__refund_id('2gBpbnvo16ElbZQm9RXDVWl4'))