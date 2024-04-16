## Инициализация миграций alembic
- `cd src`
- `alembic init alembic`
- `alembic.ini` кидаем в корень проекта и в нем устанавливаем значение `script_location` на `src/alembic`
- в `alembic/env.py` импортируем:
  - `from src.config import settings`
  - `from src.db import Base` класс, который наследуется от `DeclarativeBase`. От него наследуются все таблицы
  - `from src.candies.models import Candies` обязательно импортируем схему таблицы, иначе миграция будет пустой
- в `alembic/env.py`:
  - меняем значение для `target_metadata` с `None` на `Base.metadata`
  - пишем `config.set_main_option("sqlalchemy.url", f"{settings.DB_URL}")` для перезаписи sqlalchemy.url в alembic.ini

- возвращамся в корень проекта и выполняем команду для создания миграции указанным в кавычках названием:  `alembic revision --autogenerate -m "initial migration"`. После выполнения команды в src/alembic/versions появится модуль миграции, в котором будет отображена структура миграции.
- теперь можем применить миграцию командой `alembic upgrade head`
