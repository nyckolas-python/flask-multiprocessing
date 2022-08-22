import time
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup

from models import current_user, add_announcements

base_url = 'https://www.olx.ua'
category_url = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/?page='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


def get_urls(url: str) -> list:
	all_urls = []
	for i in range(1,10):		
		response = requests.get(url+str(i), headers=headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		for item in soup.select("a.css-1bbgabe"):
			href = item.get('href')
			all_urls.append(base_url + href)
	return all_urls

def parse(url: str) -> dict:
	try:
		response = requests.get(url)
		user_id = int(current_user.get_id())
		if response.status_code == 200 and user_id in (1, 2, 3):
			soup = BeautifulSoup(response.content, 'html.parser')
			name = soup.select_one("h1.css-r9zjja-Text").text
			price = soup.select_one("h3.css-okktvh-Text").text
			olx_id = soup.select_one("span.css-9xy3gn-Text").text[4:]
			image = ''
			vendor_name = ''
			if user_id in (2, 3):
				image = soup.select_one("div.swiper-zoom-container img[src]").get('src')
			if user_id == 3:
				vendor_name = soup.select_one("h4.css-1rbjef7-Text").text
			
			return {'olx_id': olx_id, 'name': name, 'price': price, 'image': image, 'vendor_name': vendor_name}

	except Exception as ex:
		print(f"{ex} in {url}")


def get_items() -> list:
	urls: list = get_urls(category_url)
	user_id = int(current_user.get_id())
	try:
		with Pool(processes=25) as p:
			result = p.map(parse, urls[:user_id*100])
	except Exception as ex:
		print(ex)
	finally:
		p.join()
  
		add_announcements(result[:user_id*100])
		return result


# if __name__ == '__main__':
# 	start = time.time()

# 	res = get_items()
# 	print(res)

# 	end = time.time()
# 	print('It took', (end - start), 'seconds')