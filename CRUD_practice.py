# Создать сессию:
session = Session(engine)

# CREATE
# Создать новую запись в БД (obj - это объект модели):
session.add(obj)
# Создать несколько записей в БД:
session.add_all(obj1, obj2, obj3)

# READ
# Получить из базы объект Query, содержащий все объекты модели Model
session.query(Model)
# Получить из базы список, содержащий все объекты модели Model
session.query(Model).all()
# Получить из базы первый объект модели Model
session.query(Model).first()
# Получить число - количество объектов модели Model
session.query(Model).count()
# Получить объект Query, содержащий объекты Model,
# у которых поле is_human равно False
session.query(Model).filter(Model.is_human == False)
# Получить объект Query, содержащий первые 12 объектов модели Model
session.query(Model).limit(12)
# Получить объект Query, содержащий все объекты Model, начиная с 10-го
session.query(Model).offset(9)

# UPDATE
# Во всех объектах модели Model присвоить полю is_human значение True
session.query(Model).update(
    {"is_human": True}
)

# DELETE
# Получили отдельный объект модели Model
obj = session.query(Model).first()
# ...и удалили его:
session.delete(obj)
# Удаляем объекты, у которых в поле color хранится значение Yellow:
session.query(Model).filter(Model.color == 'Yellow').delete()

# Для действий, изменяющих базу данных (для Create, Update и Delete)
# после внесения всех изменений
# необходимо закоммитить сессию - отправить изменения в БД:
session.commit()

