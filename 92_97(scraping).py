import urllib.request as req ## it returns a file like obj
response = req.urlopen("https://stackoverflow.com/documentation/")
#print(response.code)
#print(response.read())


import urllib

query_param = {"usename" : "stackoverflow" , "password" : "me.em"}
query_encode = urllib.parse.urlencode(query_param).encode('utf8')
response_param = req.urlopen("https://stackoverflow.com/users/login" ,query_encode)
print(response_param.code)

# 92.5 BeautifulSoup

from bs4 import BeautifulSoup
import requests
"""
# Use a bage ready by obtaining it by request module
res = requests.get("https://www.codechef.com/problems/easy")
page = BeautifulSoup(res.text , 'lxml')
tags_tbl = page.select('table.dataTable') ## Select table tage with class name dataTable
print("tags_tbl",len(tags_tbl)  )

"""

data = """
	<ul>
		<li class ="item"> l1 </li>
		<li class ="item"> l2 </li>
		<li class ="item"> l3 </li>
	</ul>
"""

soup = BeautifulSoup(data , 'html.parser')

for l in soup.select("li.item"):
	print(l.get_text())





html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>
<label> Name :</label>
	Dana
'''

soup = BeautifulSoup(html , 'html.parser')

for a in soup.find_all('label'):
    print ("Found the URL:", a.next_sibling.strip())

for a in soup.find_all('a', href=True):
	print("Found the URL:", a['href'])



import requests

with requests.Session() as session:
	# Set Cookies
	session.get('http://httpbin.org/cookies/set?key=value')
	# Get Cookies
	response = session.get('http://httpbin.org/cookies')
	print(response.text)








from requests import post
foo = post('http://httpbin.org/post', data = {'key':'value'})
print(foo.headers)





"""
Selenium works as we pretend like an actuall user,
It simulates a real user as some websites don't like to be scraped


browser = webdriver.Firefox()
browser.get('http://stackoverflow.com/questions?sort=votes') ##Load document
title = browser.find_element_by_css_selector('h1')
print(title)
"""


"""

Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8.
"""



