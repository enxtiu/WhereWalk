import sqlite3, logging

logger = logging.getLogger(__name__)

def create_data_base(name: str, table: str) -> None:
    try:
        with sqlite3.connect(f'{name}.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f"""CREATE TABLE {table}""")
            connection.commit()
    except Exception as e:
        logger.debug(f'EXCEPTION: {e}')
        logger.critical(f'EXCEPTION: {e}')


def start_data_base(name_base: str, fp: str, users_page: str, function: create_data_base) -> None:

    function(name_base, fp)
    function(name_base, users_page)

