
import requests

dic= open('/Users/ahmed/Desktop/dic.txt', 'r')
url = input ('please enter url: ')

for x in dic:
    r= requests.get(url + '/' + x.rstrip('/n'))
    if r.status_code ==200:
        print(' the page ' + url + '/' + x + 'is there')
    else:
        print('the page ' + url + '/' + x + 'is not there ')
    