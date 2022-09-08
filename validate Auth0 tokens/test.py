import json
from jose import jwt
from urllib.request import urlopen

# Configuration
# UPDATE THIS TO REFLECT YOUR AUTH0 ACCOUNT
AUTH0_DOMAIN = 'dev-sy8qy3vw.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Trivia'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# paste your tokenMAKE SURE THIS IS A VALID AUTH0 TOKEN FROM THE LOGIN FLOW
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxDakJWb2F4Q1VKRGsxdjFXWjNoXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zeThxeTN2dy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMxNmE5NmM4NDAyMjFkMWQyMzE2ZGY2IiwiYXVkIjoiVHJpdmlhIiwiaWF0IjoxNjYyNjY2NzU4LCJleHAiOjE2NjI2NzM5NTgsImF6cCI6IkdScGE0aFJFNEhpcnZ4WWZiYzFrWlNmeHhnQ0RjMUFXIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJlZGl0IGFsYnVtIiwicG9zdCBhbGJ1bSJdfQ.nYFfiGW95YjzVwB0FWUw-rPP_YCUtWZlFCWz74CZkiOar92dc0DpYvFzp5zFXxihJbrGP_MRIy2dFWnTU9EPqZ_BKRmBZfqLVaNAt9h6osEQh-TGhtBayfVKBqbB5-F41nYms4w14mu_OuNQ2cLbj_O8e2wJTp4c7nUvwMWtTBw8yEc7HXEPEaXQMwlopyOr6Hi811t2R01svWkGDLF5QGtFpEmNElFzDo7wiA9K-Wvl5A6W70H66G_nWgSJhouUncnmYKgIPrcNHvkcyKEc9E3afKCYbk2t992WP-CMjbJgdaF4eT5AuLxI7Q1kmecTzOt3UC-oTM79t_AxmqwFpw' 

## Auth Header
def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    
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