import requests

proxies = {
    'http':'http://104.225.220.233:80'
}

info = requests.get('http://ipinfo.io/json', proxies=proxies)

print(info.text)