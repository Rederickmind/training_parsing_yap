'''
При помощи метода session.query() определите
в базе данных количество объектов модели Pep,
у которых значение поля status равно 'Final'.
Напечатайте в консоли полученное число.

Подсказка
Создайте объект сессии для работы с ORM.
Используйте метод сессии query(),
а также методы filter() и count() для получения нужного результата.
Обратите внимание на синтаксис фильтрации элементов:
указывается атрибут модели, затем пишется нужное выражение,
например, равенство.
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
result = session.query(Pep).filter(Pep.status == 'Final').count()
print(result)
