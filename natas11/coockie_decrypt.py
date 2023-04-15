from email.mime import base
import json
import base64

encrypted_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLX54bjY='


default_cookie = {
    "showpassword": "no",
    "bgcolor": "#ffffff"
}

cookies = {"data": None}

def xor_encrypt(inp:str):
    key = 'hello world'
    text = inp
    out_text = ''

    # Iterate through each character
    for i in range(len(text)):
        out_text += str(str(text[i]) ^ str(key[i % len(key)]))

    return out_text


def xor_decrypt(inp):
    key = '<censored>'
    text = inp
    out_text = b''

    # Iterate through each character
    for i in range(len(text)):
        out_text += bytes([text[i] ^ key[i % len(key)]])

    return out_text.decode('utf-8')


def save_data(data): 
    return base64.b64encode(xor_encrypt(json.dumps(data).encode('utf-8'))).decode('utf-8')


# cookies["data"] = save_data(default_cookie)

print(json.dumps(default_cookie).encode('utf-8'))
