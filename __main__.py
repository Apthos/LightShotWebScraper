import urllib.request
import os
import shutil
import _thread
import threading
import time

os.chdir("/Users/apthos/PycharmProjects/Scraper/img")
link = None
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }
find = "http://image.prntscr.com/image/"
pool = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


def prRed(prt): print("\033[91m {}\033[00m".format(prt))


def prGreen(prt): print("\033[92m {}\033[00m".format(prt))


def extract_image_link(url_link):
    request = urllib.request.Request(url_link, None, headers)
    response = urllib.request.urlopen(request)
    data = str(response.read())
    file = ''
    link = 'h'
    index = data.find(find)
    c = ''
    while c is not '"':
        if link.__contains__(find):
            file = file + c
        link = link + c
        index = index + 1
        c = data[index]
    # print(link + "$" + file)
    return link + "$" + file


def extract_image(ex):
    # print(ex.split("$")[0] + " ", ex.split("$")[1])
    request = urllib.request.Request(ex.split("$")[0], None, headers)
    with urllib.request.urlopen(request) as response, open(ex.split("$")[1], 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def process(link):
    try:
        extract = extract_image_link(link)
        extract_image(extract)
        prGreen(link + " has been retrieved successfully!")
    except:
        prRed(link + " was a failed link!")


def main():
    link = input("Enter a lightshot link: ")
    root = link[:-2]
    for first in pool:
        for second in pool:
            while threading.active_count() > 20:
                time.sleep(1)
            new_link = root + first + second
            t = threading.Thread(target=process, args=(new_link,))
            t.start()


if __name__ == '__main__':
    main()
