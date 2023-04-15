import json

def xor_encrypt(inp):
    key = '<censored>'
    text = inp.encode('utf-8')
    out_text = b''

    # Iterate through each character
    for i in range(len(text)):
        out_text += bytes([text[i] ^ key[i % len(key)]])

    return out_text


def xor_decrypt(inp):
    key = '<censored>'
    text = inp
    out_text = b''

    # Iterate through each character
    for i in range(len(text)):
        out_text += bytes([text[i] ^ key[i % len(key)]])

    return out_text.decode('utf-8')

"""decode json"""
def decode_json(inp):
    return json.loads(xor_decrypt(inp))

print(decode_json('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLX54bjY='))