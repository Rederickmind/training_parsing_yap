# Импортируйте все нужные библиотеки.
import requests
from bs4 import BeautifulSoup

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base, Session

PEP_URL = 'https://peps.python.org/'


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))


engine = create_engine('sqlite:///sqlite.db')

# создайте таблицу в БД;
Base.metadata.create_all(engine)
bd_session = Session(engine)
# загрузите страницу PEP_URL;
response = requests.get(PEP_URL)
response.encoding = 'utf-8'
# создайте объект BeautifulSoup;
soup = BeautifulSoup(response.text, 'lxml')
main_tag = soup.find('section', attrs={'id': 'numerical-index'})
pep_list = main_tag.find('tbody')
pep_rows = pep_list.find_all('tr')

# спарсите таблицу построчно и запишите данные в БД.
for pep_row in pep_rows:
    type_status = pep_row.find('abbr').text
    number_title = pep_row.find_all(
        'a',
        attrs={'class': 'pep reference internal'}
    )
    number = number_title[0].text
    title = number_title[1].text
    authors = pep_row.find_all('td')[-1].text

    current_pep = Pep(
        type_status=type_status,
        number=number,
        title=title,
        authors=authors
    )
    bd_session.add(current_pep)
    bd_session.commit()
