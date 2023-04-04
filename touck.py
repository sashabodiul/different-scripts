import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}').json()

        info = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }

        # res = [k for k in info.keys()]
        # print(res)

        for k,w in info.items():
            print(f'{k} : {w}')

        area = folium.Map(location=[response.get('lat'),response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview = Figlet(font='slant')
    print(preview.renderText('IP INFO'))
    ip = input('Please enter target IP address: ')
    
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()