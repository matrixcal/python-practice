#!/bin/python
import oauth2 as oauth
import urlparse
import json

consumer_key = "YIgutbtxMRLnLVkmsh083fbhWXP_Qy4XEn4yo0d1q5NTLukWHJp_H_q-lczwj170"
consumer_secret = "5gQyhI1gWATu7793j0WlsvsRUBlcg6TrymC8m44JABmje6rk3z4Ev_87uK_RxsJm"

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
print resp,type(resp)

if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

#print content
print resp['content-length']
print "\n"

request_token = dict(urlparse.parse_qsl(content))
print request_token['oauth_token']
#print "Requesr Token:",  "\n"
#print "- oauth_token        = %s" % request_token['oauth_token'], "\n"
#print "- oauth_token_secret = %s" % request_token['oauth_token_secret'], "\n"

#authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'
#print "Go to the following link in your browser:", "\n"
#print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']), "\n"ikhn

#!/bin/python
import requests
import json
import simplejson
url='http://gun.io'
req = requests.get('https://github.com/timeline.json')
print req.status_code
req=requests.get(url)
print req.content
req=requests.get('https://api.github.com/user', auth=('matrixcal', 'Ilovekamlo$123'))
print req.status_code
req=requests.get('https://github.com/timeline.json')
c=req.content
j=simplejson.loads(c)
print j
#for item in j:
#       print item['repository']['name']

#print type(req)
