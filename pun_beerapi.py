import urllib2
import requests

response = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
html = response.read()
html = html.replace("{","\n")
html = html.replace(",","\n")  
html = html.replace("[","\n")
html = html.replace("}","\n")
html = html.replace("]","\n")
print type(html)
lines = []
lines = html.split("\n")
beer_name =[]
beer_name = lines[3].replace(":"," ")
print beer_name
print "================================="

print beer_name


key = 'key-46ec6f14108cada377640a996cac2617'

recipient = 'tester@mailinator.com'

request_url = 'https://api.mailgun.net/v3/sandboxcc90c3a4370f4a5aa1561a9223b5487b.mailgun.org'

request = requests.post(request_url, auth=('api',key), data={
    'from': 'work.kolobosd@gmail.com',
    'to':recipient,
    'subject': 'Punkapi',
    'text': 'hello'
})



