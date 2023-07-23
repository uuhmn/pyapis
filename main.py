import requests
from bs4 import BeautifulSoup
import json

# آدرس صفحه‌ی مورد نظر
url = "https://aiofilm.org/anime/"

# درخواست GET برای دریافت صفحه
response = requests.get(url)

# تبدیل صفحه به شیء BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
anime_info_list = []
# # استخراج عنوان انیمه
# title = soup.find('h2', class_='singletitle').text.strip()
# stustos = soup.find('div',class_='vazipakh1').text.strip()
# img_tag = soup.find('img',class_='postimgf')
# img_src = img_tag.get('src') if img_tag else None

# # پیدا کردن تگ ul با کلاس mb-4 text-gray-800
# ul_tag = soup.find('ul', class_='mb-4')
# # print(ul_tag)

# for tag in ul_tag.find_all(text=True):
#     print(tag)

# # چاپ تگ لینک
# for link in ul_tag.find_all('a'):
#     print(link.get('href'))

# print(title)
# print(stustos)
# print(img_src)
anime_list = soup.find_all('div', class_='grid')
# for anime in anime_list:
#     print(anime.h2.text.strip())
# anime_info_list.append({
#     'title': title,
#     'img_url': img_src,
#     'status': stustos
#     })
anime_data = []
for anime in anime_list:
    title = anime.h2.text.strip()
    url = anime.a.get('href')
    img_src = anime.img.get('src')
    rating_tag = anime.find('span', class_='imdb')
    rating = rating_tag.text.strip() if rating_tag else None
    anime_data.append({'title': title, 'url': url, 'img_src': img_src, 'rating': rating})

# چاپ دیکشنری حاوی اطلاعات انیمه‌ها به صورت JSON
print(json.dumps(anime_data, indent=4, ensure_ascii=False))
# # ذخیره اطلاعات به صورت JSON

# print(title)
