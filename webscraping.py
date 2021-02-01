from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

############################################################

# --------------------------> Direct
"""Rarely used but at least you will know how it works"""
#print(soup.body) # try each of those 1 by 1
#print(soup.head)
#print(soup.title)

############################################################

# --------------------------> find()
"""commonly used"""
#el = soup.find('div')
#el = soup.find(id='section-1')
#el = soup.find(class_='items')
#el = soup.find(attrs={"data-hello": "hi"})

# --------------------------> find_all() or findAll()
#el = soup.find_all('div')
#el = soup.find_all('div')[1] # the [1] works like an array (element one = [0])

############################################################

# --------------------------> select()
#el = soup.select('#section-1')
#el = soup.select('#section-1')[1]
#el = soup.select('.item')[0]

# --------------------------> get_text()
#el = soup.find(class_='item').get_text()

#for item in soup.select('.item'):
#    print(item.get_text())

# --------------------------> navigation
#el = soup.body.contents[1].contents[1].next_sibling()
#el = soup.find(id='section-2').find_previous_sibling()
#el = soup.find(class_='item').find_parent()
#el = soup.find('h3').find_next_sibling('p')


############################################################
print(el)