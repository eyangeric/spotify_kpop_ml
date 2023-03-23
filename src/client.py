import requests

# CLIENT_ID = 'b786186d17994d0899e7b554333a561b'
# CLIENT_SECRET = '37cb414ac34844e0965fe8c107d3f270'

# body_params = {'grant_type' : 'client_credentials'}

def get_authorization_token(CLIENT_ID, CLIENT_SECRET):
    url='https://accounts.spotify.com/api/token'
    token_response = requests.post(url, data = {'grant_type' : 'client_credentials'}, auth = (CLIENT_ID, CLIENT_SECRET)) 
    token = token_response.json()
    access_token = token['access_token']
    token_type = token['token_type']
    HEADERS = {'Authorization': f"{token_type} {access_token}"}
    return HEADERS









