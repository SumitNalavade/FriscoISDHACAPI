import requests

def sendIp(ip):
    url = "https://una-opened-subscriber-capable.trycloudflare.com/"
    obj = { "ip": ip}

    x = requests.post(url, json=obj)


