import pdfkit, urllib, urllib2
from pyPdf import PdfFileWriter, PdfFileReader

#url of the statistics textbook
baseurl = 'http://slader.com/textbook/9781429245593-the-practice-of-statistics-for-ap-4th-edition/'

#keywords to search for to extrct the shit
ex = 'h3 id="exercises"'
chrex = 'h3 id="chapter-review-exercises'
chtest = 'ap-statistics-practice-test'
identifier = 'data-url="/textbook/9781429245593-the-practice-of-statistics-for-ap-4th-edition/'
options = {
	'page-size' : 'Letter',
    'margin-top' : '0.25in',
    'margin-right' : '0.25in',
    'margin-bottom' : '0.25in',
    'margin-left' : '0.25in',
    'no-outline' : None,
    'no-background': None,
}

# most pages don't have exercises, they redirect to the next one that does
def getredirectpage(iurl):
	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
	request = opener.open(iurl)
	newurl = request.url
	return int(newurl.replace(baseurl, "")[:-1])

#gets the actual urls of the problems for easy enumeration
def problemurls(pagen):
	purls = []
	index = pagen.find(identifier)
	while (index != -1):
		jck = pagen[index+len(identifier) : pagen.find('>', index)-1]
		purls.append(jck)
		index = pagen.find(identifier, index+1)
	return purls


#finnascrape 
#i is the PAGE NUMBER TO START more hardcoded stuff lol
i = 621
iend = 692
pn = 1
while (i < iend): # 809
	#reasoning for getredirect:
	#	-query to find if there are even problems on that page, if not
	#	 then skip to the next page with actual problems on it as the site automatically does
	page = getredirectpage(baseurl + str(i)) #int
	if page != i:
		i = page
		continue
	print i
	#do the magic @exercises pages
	starter = '' #where to start the search for exercises and links and shit
	pagedata = urllib.urlopen(baseurl+str(i)).read()
	if (ex in pagedata):
		starter = ex
	elif (chrex in pagedata):
		starter = chrex
	elif (chtest in pagedata):
		starter = chtest
	else:
		i += 1
		continue #this means it's a 'cumulative test or whatever'
	pagedata = pagedata[pagedata.find(starter):] #PEACE
	problemas = problemurls(pagedata)#pdfkit.from_url(baseurl+'36', 'out.pdf', options=options)

	for urlext in problemas:
		fullurl = baseurl + urlext
		print fullurl
		#ATTENTION BELOW: images/(chapter number)/prblm ... hardcoded cause i was lazy
		pdfkit.from_url(fullurl, 'images/10/prblm'+str(pn)+'.pdf', options=options)
		pn += 1

	i += 1



