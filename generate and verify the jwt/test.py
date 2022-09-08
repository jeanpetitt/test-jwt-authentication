import base64
import jwt

payload = {'park':'madison square'}
algo = 'HS256' #HMAC-SHA 256
secret = 'learning'

encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)
