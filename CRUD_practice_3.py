'''
Удалите все записи со статусом 'Rejected'
(не забудьте применить изменения к БД)
и подсчитайте количество оставшихся записей.
Полученное число напечатайте в консоли.

Подсказка
Для операций, которые изменяют данные (вставка, обновление, удаление),
необходимо использовать метод commit(), иначе изменения не запишутся.
Даже если query() выдаёт правильный результат, записи в БД не изменятся,
пока не выполнен коммит.
Подсчитать все объекты можно, применив метод count() прямо к методу query().
'''
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, Session


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'


engine = create_engine('sqlite:///sqlite_train.db')
# Ваш код - здесь.
session = Session(engine)
deletion = session.query(Pep).filter(
    Pep.status == 'Rejected'
    ).delete()
session.commit()
remains = session.query(Pep).count()
print(remains)
