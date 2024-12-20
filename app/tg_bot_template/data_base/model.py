import sqlite3, logging, os


logger = logging.getLogger(__name__)

def list_all_table(name_db: str, name_line: str, name_table: str, if_: str='') -> list[tuple[str, str]]:
    if os.path.exists(f'{name_db}.db'):

        try:

            with sqlite3.connect(f'{name_db}.db') as connection:
                cursor = connection.cursor()
                cursor.execute(f'SELECT {name_line} FROM {name_table}{if_}')
                connection.commit()
                logger.debug('return cursor')
                return cursor.fetchall()

        except Exception as e:
            logger.debug(f'EXCEPTION: {e}')
            logger.critical(f'EXCEPTION: {e}')
    else:
        logger.debug('Name data base not found')
        logger.error('Name data base not found')



favourites_places = """IF NOT EXISTS favourites_places (
name_place TEXT NOT NULL,
info TEXT NOT NULL,
user_id INTEGER NOT NULL
)"""

users_page = """IF NOT EXISTS users_page (
user_id INTEGER NOT NULL UNIQUE,
page INTEGER NOT NULL,
category TEXT NOT NULL
)"""