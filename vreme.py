import urllib2
from bs4 import BeautifulSoup

# not done yet!!!!

soup = BeautifulSoup(urllib2.urlopen("http://www.arso.gov.si/vreme/napovedi%20in%20podatki/vreme_si_w.html").read(), "lxml")
#soup = BeautifulSoup(urllib2.urlopen("http://pro-vreme.net/index.php?id=8").read(), "lxml")
#result = soup.select("#glavna" > "tbody" > "tr" > "td[2]"> "table")
#print result


for p in divs.select('.//*[@id="glavna"]/tbody/tr/td[2]/table'):
# extracts all <p> inside
    print p.extract()


for row in soup("table", {"id": "glavna"})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string
    #//*[@id="glavna"]/tbody/tr/td[2]/table
    #//*[@id="glavna"]/tbody/tr/td[2]/table

    #father.findNext('div',{'class':'class_value'}).findNext('div',{'id':'id_value'}).findAll('a')