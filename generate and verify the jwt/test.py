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

# my auth0 token decoded
algo = {
  "alg": "RS256",
  "typ": "JWT",
  "kid": "lCjBVoaxCUJDk1v1WZ3h_"
}
payload = {
  "iss": "https://dev-sy8qy3vw.us.auth0.com/",
  "sub": "auth0|6316a96c840221d1d2316df6",
  "aud": "Trivia",
  "iat": 1662666758,
  "exp": 1662673958,
  "azp": "GRpa4hRE4HirvxYfbc1kZSfxxgCDc1AW",
  "scope": "",
  "permissions": [
    "edit album",
    "post album"
  ]
}
encoded_jwt = jwt.encode(payload, secret, headers=algo)
# encoded_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxDakJWb2F4Q1VKRGsxdjFXWjNoXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zeThxeTN2dy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMxNmE5NmM4NDAyMjFkMWQyMzE2ZGY2IiwiYXVkIjoiVHJpdmlhIiwiaWF0IjoxNjYyNjY2NzU4LCJleHAiOjE2NjI2NzM5NTgsImF6cCI6IkdScGE0aFJFNEhpcnZ4WWZiYzFrWlNmeHhnQ0RjMUFXIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJlZGl0IGFsYnVtIiwicG9zdCBhbGJ1bSJdfQ.nYFfiGW95YjzVwB0FWUw-rPP_YCUtWZlFCWz74CZkiOar92dc0DpYvFzp5zFXxihJbrGP_MRIy2dFWnTU9EPqZ_BKRmBZfqLVaNAt9h6osEQh-TGhtBayfVKBqbB5-F41nYms4w14mu_OuNQ2cLbj_O8e2wJTp4c7nUvwMWtTBw8yEc7HXEPEaXQMwlopyOr6Hi811t2R01svWkGDLF5QGtFpEmNElFzDo7wiA9K-Wvl5A6W70H66G_nWgSJhouUncnmYKgIPrcNHvkcyKEc9E3afKCYbk2t992WP-CMjbJgdaF4eT5AuLxI7Q1kmecTzOt3UC-oTM79t_AxmqwFpw'
decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True, algorithms='RS256')
print('my token decoded', decoded_jwt)
