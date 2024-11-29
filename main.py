import requests, os

from typing import Callable, Any

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Recursed(Exception):

    def __init__(self, *obj: tuple[int]) -> None:
        super().__init__()
        self.obj = obj


def tail_recursed(*obj: int) -> None:
    raise Recursed(*obj)

def recursed_decorated(func: Callable[[int], Any]) -> Callable[[int, int], None]:
    def wrapper(*obj: int) -> None:
        while True:
            try:
                func(*obj)
            except Recursed as exc:
                obj = exc.obj
    return wrapper

@recursed_decorated
def request_Telegram(count: int, offset: int) -> None:

    uppdate_Telegram = requests.get(f'{api_url_Telegram}{Token}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    uppdate_Cat = requests.get(f'{api_url_Cat}').json()[0]
    if uppdate_Telegram['result']:
        for result in uppdate_Telegram['result']:
            offset = result['update_id']
            chat_id: int = result['message']['chat']['id']
            if result['message']['text'] == r'/start':
                sendMessage = requests.get(f'{api_url_Telegram}{Token}/sendMessage?chat_id={chat_id}&text={info}')
            else:
                sendPhoto = requests.get(f'{api_url_Telegram}{Token}/sendPhoto?chat_id={chat_id}&photo={uppdate_Cat['url']}')

    print(count)
    return tail_recursed(count + 1, offset)



if __name__ == '__main__':

    Token = os.getenv('TOKEN')
    api_url_Telegram = 'https://api.telegram.org/bot'
    api_url_Cat = 'https://api.thecatapi.com/v1/images/search'
    info = (
        'Привет, я ещё нахожусь в разработке, поэтому тебе придётся подождать моего релиза)'
        '\nНо чтобы тебе не было скучно я могу сгенирировать случайные фото котиков)'
        '\nНапиши дaлее любой текст и они появятся!)'
    )

    count = 0
    offset = -2
    timeout = 60


    request_Telegram(0, offset)