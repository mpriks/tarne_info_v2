import urllib.r
from lxml import html

# ilma ssl moodulita veateade [SSL: CERTIFICATE_VERIFY_FAILED]
import ssl



# loon [SSL: CERTIFICATE_VERIFY_FAILED] veateate vältimiseks vajaliku muutuja
context = ssl._create_unverified_context()

# lisan urlopen funktsiooni argumendi context=context
html_file = urllib.urlopen('https://jira.arib.pria.ee/projects/EPRIA?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page&status=all', context=context) #.read()

html_text = html_file.read()

print(html_text)

