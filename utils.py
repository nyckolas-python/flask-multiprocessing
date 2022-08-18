import time
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup

from models import current_user, load_user

base_url = 'https://www.olx.ua'
category_url = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/?page='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


def get_urls(url: str) -> list:
	all_urls = []
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	for item in soup.select("a.css-1bbgabe"):
		href = item.get('href')
		all_urls.append(base_url + href)
	return all_urls

def parse(url: str) -> dict:
	try:
		response = requests.get(url)
		if response.status_code == 200:
			soup = BeautifulSoup(response.content, 'html.parser')
			name = soup.select_one("h1.css-r9zjja-Text").text
			price = soup.select_one("h3.css-okktvh-Text").text
			image = ''
			vendor_name = ''
			if int(current_user.get_id()) == 2:
				image = soup.select_one("div.swiper-zoom-container img[src]").get('src')
			elif int(current_user.get_id()) == 3:
				image = soup.select_one("div.swiper-zoom-container img[src]").get('src')
				print(soup.select_one("h4.css-1rbjef7-Text").text)
				vendor_name = soup.select_one("h4.css-1rbjef7-Text").text
			else:
				return {}
			return {'name': name, 'price': price, 'image': image, 'vendor_name': vendor_name}

	except Exception as ex:
		print(f"{ex} in {url}")


def get_items() -> list:
	urls: list = get_urls(category_url + '1') + get_urls(category_url + '2') + get_urls(category_url + '3')

	try:
		with Pool(processes=10) as p:
			result = p.map(parse, urls)
	except Exception as ex:
		print(ex)
	finally:
		p.join()
		return result


if __name__ == '__main__':
	start = time.time()

	res = get_items()
	print(res)

	end = time.time()
	print('It took', (end - start), 'seconds')