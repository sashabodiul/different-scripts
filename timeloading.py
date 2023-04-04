from urllib.request import urlopen
import time
from pyfiglet import Figlet


def get_load_time(url):
    if ('http' or 'https') in url:
        open_this_url = urlopen(url)
    else:
        open_this_url = urlopen("https://" + url)
    start_time = time.time()
    open_this_url.read()
    end_time = time.time()
    open_this_url.close()
    time_to_load = end_time - start_time

    return time_to_load

preview = Figlet(font='slant')
print(preview.renderText('Check loading'))
url = input('URL:')
print('Time to load: ',f'{get_load_time(url):.4} seconds')