import requests, bs4

# 1
# res = requests.get('https://nostarch.com/automate-boring-stuff-python-3rd-edition')

# res.raise_for_status()

# noStrachSoup = bs4.BeautifulSoup(res.text)

# print(type(noStrachSoup))

# # 2
# exampleFile = open('examplehtml.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile)

# print(type(exampleSoup))

# 3
# exampleFile = open('examplehtml.html', encoding = 'utf-8')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read())

# elems = exampleSoup.select('#author')

# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# print(str(elems[0]))
# print(elems[0].attrs)

# pElems = exampleSoup.select('p')

# print(type(pElems))
# print(len(pElems))
# print(type(pElems[0]))
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# # print(str(pElems[2]))
# # print(pElems[2].getText())
# print(pElems[0].attrs)

# 4
soup = bs4.BeautifulSoup(open('examplehtml.html', encoding = 'utf-8'))
spanElem = soup.select('span')[0]

print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.attrs)

