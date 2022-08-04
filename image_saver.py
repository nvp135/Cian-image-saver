import re
import os
import requests

import urllib.request
from bs4 import BeautifulSoup

BASE_URL_AJAX = "https://map.cian.ru/ajax/map/roundabout/"
BASE_URL_API = "https://ekb.cian.ru/cian-api/mobile-site/v2/offers/clusters/"

BASE_URL = "https://ekb.cian.ru/"
LINKS_FOR_SAVE = ["https://ekb.cian.ru/sale/flat/211846136/"]

IMG_LINKS = [
	
]

def get_html(url):
	response = urllib.request.urlopen(url)
	#print(response.read())
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	img_links = []
	for pic in soup.find_all('img'):
		img_links.append(pic['src'])
	return img_links

def download_file(url, folderName='1'):
	#urllib.request.urlretrieve(url, url.rsplit('/', 1)[-1])
	pathTo = f'images/{folderName}'
	imageBytes = requests.get(f'{url}').content
	fileName=url.rsplit('/', 1)[-1]
	try:
		os.makedirs(f'{pathTo}', exist_ok=True)
	except FileExistsError:
		return
	
	with open(f'{pathTo}/{fileName}', 'wb') as file:
		file.write(imageBytes)
	

def download_imgs():
	for link in IMG_LINKS:
		download_file(link)

def main():
	download_imgs()
	'''for link in LINKS_FOR_SAVE:
		img_urls = parse(get_html(link))
		print(img_urls)
	i = len(img_urls)
	for url in img_urls:
		i -= 1
		print('%d pages left %s' % (i, url))
		#load_file(url)'''

if __name__ == '__main__':
	main()


'''
''
JS script for find image links
''
let imgs = document.querySelectorAll("ul > li > img");
let imgSrc = "";
for (var i = 0; i < imgs.length; i++) 
{
	imgSrc += "\"" + imgs[i].src.replace("-2.jpg", "-1.jpg") + "\",";
}  
console.log(imgSrc);

'''
