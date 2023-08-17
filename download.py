from pathlib import Path
import requests_cache
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
# Путь до директории с программой
BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # Получили таблицу с сайта и выбрали нужный регулярным выражением
    table_tag = soup.find('table', attrs={'class': 'docutils'})
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    # Сохраняем ссылку на файл
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    # Получаем имя файла из ссылки
    filename = archive_url.split('/')[-1]
    # Создаем дирекиорию загрузки и получаем путь сохранения файла
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    # Загрузка файла
    response = session.get(archive_url)
    # В бинарном режиме открывается файл на запись по указанному пути.
    with open(archive_path, 'wb') as file:
        # Полученный ответ записывается в файл.
        file.write(response.content)
