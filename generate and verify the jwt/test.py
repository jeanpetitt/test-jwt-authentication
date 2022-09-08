import base64
import jwt

payload = {'park':'madison square'}
algo = 'HS256' #HMAC-SHA 256
secret = 'learning'

# encode the jwt
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print('json web token encoded is ',encoded_jwt)

# decode the jwt
decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True, algorithms=algo)
print('json web token decoded is ', decoded_jwt)

# decode with simple base64 encoding
payload = {'city':'yaounde'}
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)

base64_decode = base64.b64decode(str(encoded_jwt).split('.')[1]+'==')
print('decode jwt with base64 is ', base64_decode)