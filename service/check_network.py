from urllib import request


def check_network():
    '''use https://www.google.com.tw check network'''
    try:
        request.urlopen('https://www.google.com.tw', timeout=1)
        return True
    except request.URLError:
        return False
