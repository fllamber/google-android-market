import urllib.parse
import urllib.request
import socket

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
try:
    response = urllib.request.urlopen(req)
    
except urllib.error.URLError as e:
    print(e.reason)
except urllib.error.HTTPError as e:
    print(e.reason)
except urllib.request.HTTPError as e:
    print(e.reason)
except socket.error as e:
    print(e)
    print("COOKIES")
except BaseException as e:
    print(e)
    print("WOLOLO")


the_page = response.read()
