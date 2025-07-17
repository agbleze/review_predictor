from decouple import config

HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', default=8000)
ENDPOINT = config('ENDPOINT', default="predict")

URL = f'{HOST}:{PORT}/{ENDPOINT}'
