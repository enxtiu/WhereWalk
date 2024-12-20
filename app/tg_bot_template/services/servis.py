import logging

from app.data.process_data import Data


logger = logging.getLogger(__name__)

_info_list = [i for i in range(1, 11)]
count_info_list = {i: _info_list for i in range(1, 11)}

# all((17 строк, 8 столбцов))

sh_all = set(tuple(Data().all[y][x].value for x in range(8))for y in range(2, 19))

sh_apt = set(tuple(Data().apt[y][x].value for x in range(8)) for y in range(2, 4))

sh_prod = set(tuple(Data().prod[y][x].value for x in range(8)) for y in range(2, 6))

sh_gost = set(tuple(Data().gost[y][x].value for x in range(8)) for y in range(2, 5))

sh_whe = set(tuple(Data().whe[y][x].value for x in range(8)) for y in range(2, 9))

sh_con = set(tuple(Data().con[y][x].value for x in range(8) )for y in range(2, 3))

def find_category(function, user) -> str:

    all_table = function(
        'base',
        '*',
        'users_page',
    )
    logger.debug(f'{all_table}')
    for i in all_table:
        logger.debug(f'{user.id}')
        if user.id == i[0]:
            logger.debug(f'{i, i[2]}')
            return i[2]


