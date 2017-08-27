import urllib.request
import urllib.parse
import re

import ssl

# siin defineerin mingi muutuja mida ei soovitata tegelikult teha. vaata https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://jira.arib.pria.ee/projects/EPRIA?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page&status=all'
#url = 'http://pythonprogramming.net'

values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# leian kogu sisu mis on <p> ja </p> vahel
paragraphs = re.findall(r'<h1>(.*?)</h1>', str(respData))

for rida in paragraphs:
    print(rida)

