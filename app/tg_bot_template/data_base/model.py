import sqlite3, logging, os

logger = logging.getLogger(__name__)

def insert_data_base(name_db: str, table_rows: str, *args: str | int) -> None:
    if os.path.exists(f'app/tg_bot_template/data_base/{name_db}.db'):
        try:
            with sqlite3.connect(f'{name_db}.db') as connection:
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO {table_rows}", args)
                connection.commit()
        except Exception as e:
            logger.debug(f'EXCEPTION: {e}')
            logger.critical(f'EXCEPTION: {e}')
    else:
        logger.debug('Name data base not found')
        logger.error('Name data base not found')



def update_data_base(name_db: str, name_table: str, name_field: str, name_chang: str, if_: str = '') -> None:
    if os.path.exists(f'app/tg_bot_template/data_base/{name_db}.db'):
        try:
            with sqlite3.connect(f'{name_db}.db') as connection:
                cursor = connection.cursor()
                cursor.execute(f"UPDATE {name_table} SET {name_field} = {name_chang}{if_}")
                connection.commit()
        except Exception as e:
            logger.debug(f'EXCEPTION: {e}')
            logger.critical(f'EXCEPTION: {e}')
    else:
        logger.debug('Name data base not found')
        logger.error('Name data base not found')



def delete_data_base_filed(name_db: str, name_table: str, if_: str = '') -> None:
    if os.path.exists(f'app/tg_bot_template/data_base/{name_db}.db'):
        try:
            with sqlite3.connect(f'{name_db}.db') as connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM {name_table}{if_}")
                connection.commit()
        except Exception as e:
            logger.debug(f'EXCEPTION: {e}')
            logger.critical(f'EXCEPTION: {e}')
    else:
        logger.debug('Name data base not found')
        logger.error('Name data base not found')

