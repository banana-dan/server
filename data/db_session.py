# здесь всё для подключения к базе данных
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session  # обьект Session отвечает за соединение с бд
import sqlalchemy.ext.declarative as dec  # этот модуль нужен для обьявления бд

SqlAlchemyBase = dec.declarative_base()  # создаем обстрактную декларативную базу данных,
# будем использовать для получения сессий подключения к нашей базе данных.

__factory = None


# Кроме того, в файле db_session.py нам понадобится сделать еще две функции
# global_init и create_session

def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)

# global_init принимает на вход адрес базы данных, затем проверяет,
# не создали ли мы уже фабрику подключений (то есть не вызываем ли мы
# функцию не первый раз). Если уже создали, то завершаем работу, так
# как начальную инициализацию надо проводить только единожды.

# Если в функцию create_engine() передать параметр echo со значением True,
# в консоль будут выводиться все SQL-запросы, которые сделает SQLAlchemy,
# что очень удобно для отладки.

def create_session() -> Session:
    global __factory
    return __factory()
