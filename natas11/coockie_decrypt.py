from tqdm import tqdm
import json
import base64

encrypted_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLX54bjY='


default_cookie = {
    "showpassword": "no",
    "bgcolor": "#ffffff"
}

cookies = {"data": None}


def xor_encrypt(in_str, key):
    key = str(key)
    out_text = ''

    # Iterate through each character
    for i in range(len(in_str)):
        out_text += chr(in_str[i] ^ ord(key[i % len(key)]))

    return bytes(out_text, 'utf-8')



def save_data(data, key): 
    return base64.b64encode(xor_encrypt(json.dumps(data).encode('utf-8'), key)).decode('utf-8')



# print(json.dumps(default_cookie))


def key_finder(encrypt_cookie):
    # try every password from of length 1 to 100 characters long using utf-8 encoding
    for i in range(1, 100):
        raw_key = [''] * i
    for j in range(32, 123):
        print(chr(j).encode(encoding='UTF-8'), j)



print(key_finder(encrypted_cookie))

# print(save_data(default_cookie, 'test'))
