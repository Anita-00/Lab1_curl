import requests
print(requests.__version__)
#r = requests.get('http://google.com/').text
r = requests.get('https://raw.githubusercontent.com/Anita-00/Lab1_curl/67228df53c32baed925fb99e81fe41f75237fde0/Request_Version.py?token=GHSAT0AAAAAABQOH7E6QMW45OY6FGB66QSUYO5EWUQ')
print(r.text)