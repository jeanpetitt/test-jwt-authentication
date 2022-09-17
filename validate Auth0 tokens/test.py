import json
from jose import jwt
from urllib.request import urlopen

# Configuration
# UPDATE THIS TO REFLECT YOUR AUTH0 ACCOUNT
AUTH0_DOMAIN = 'fullstac-udacity-ndg.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeshop'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# paste your tokenMAKE SURE THIS IS A VALID AUTH0 TOKEN FROM THE LOGIN FLOW
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE1dEhKZ0NJOUlqTFF4R3p6dVk2TiJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFjay11ZGFjaXR5LW5kZy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMyNTNiYjEzOWYxMWUwM2ZkOGYyYWNhIiwiYXVkIjoiY29mZmVzaG9wIiwiaWF0IjoxNjYzMzg1NDUwLCJleHAiOjE2NjM0NTc0NTAsImF6cCI6ImkxNW1nc1QxSndISjFwYm5aR3hHNFN4czFFWUwxYTBXIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkcmluay1kZXRhaWwiLCJkcmlua3MiXX0.Lmhn3oMGl4-33ZGsDBunf6jXTQKNLGeGvE_3J1sxl1j8Ec1ou_6b_lhRyEVOBzcPN2IDUuozUBUd4iN38Gz8IAywbRktU4ywmDW_cfNZ9xPEGwFawcdCwS-2PtQJQmHY2G9kDbSVZ-mfl8Qfgs4TYlxpiCOe5aqq2utR9ePwTTWhSwI3s1TO-iXXQTa7NlIWALocx18JfZNPb6ZJ32z42m7_a4AfZ4apf-IPr-IYGD6H2tt8aY7CUEdeTZIcMRImIZIS0sWxlXrbOjMku4UBFcOBDcH4pe23cJAdIph2UCjUlurXxuoOUwm43IkzHOpEU9wYAWr7mIFjTrAlC1wUmg' 

## Auth Header
def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    print('JWK', jwks)
    
    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)
    
    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    
    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
            }, 400)

verify_decode_jwt(token)