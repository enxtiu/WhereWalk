LEXICON = {
    '/start': """
    Привет! Я ваш персональный гид и помощник по рекомендациям мест. Я помогу вам найти лучшие рестораны, кафе, парки, музеи и другие интересные места. Если вам понравится какое-то место, вы можете сохранить его в избранное, чтобы не забыть.

Вот что я могу для вас сделать:

👉 <u>Рекомендовать места на основе ваших предпочтений.</u>

👉 <u>Предоставить информацию о местах, включая адрес, часы работы и отзывы.</u>

👉 <u>Сохранить ваши любимые места в избранное для быстрого доступа.</u>

Если хочешь узнать подробную информацию по моему функционалу, автору или политика конфиденциальности можешь использовать меню, расположенное слева снизу на экране)

Начнем? Просто нажми на продолжить, и я подберу для вас лучшие варианты!
ps: К сожалению некоторый функционал ещё не доступен, поэтому он будет помечен крестиком, но я надеюсь, что в скором времени он будет доступен) """,
    'menu_des': {
    'description': 'Описание возможностей бота',
    'author': 'Тех-поддержка',
    'politic': 'Политика конфиденциальности',
    'favourites': 'Избранные заведения'},

    '/description': """<b>Описание бота</b>
Этот бот был создан для того, чтобы помогать пользователям находить интересные места и сохранять их в избранное.
Он обладает широким спектром возможностей и функций, которые делают его полезным и удобным инструментом для повседневного использования.

<u>Основные функции бота:</u>
<b>1) Рекомендации мест:</b>

👉 Бот может рекомендовать различные места, такие как рестораны, кафе, парки, музеи и другие интересные локации на основе ваших предпочтений и интересов.

👉 Предоставляет подробную информацию о местах, включая адрес, часы работы, отзывы и рейтинги.

<b>2) Сохранение в избранное:</b>

👉 Вы можете сохранять понравившиеся места в избранное, чтобы легко находить их в будущем.

👉 Управление списком избранных мест, добавление и удаление записей.

<b>3) Проведение пути до выбранного места:</b>

👉 Бот может проложить маршрут до выбранного места, предоставляя пошаговые инструкции и информацию о транспорте.

👉 Помогает вам добраться до места назначения наиболее удобным и быстрым способом.

<u>Преимущества использования бота:</u>
<b>Удобство</b>: Бот доступен в любое время и может помочь вам в любой ситуации.

<b>Персонализация</b>: Бот учитывает ваши предпочтения и интересы, чтобы предоставлять наиболее релевантные рекомендации и информацию.

<b>Эффективность</b>: Быстрый доступ к информации и рекомендациям позволяет экономить время и усилия.

<b>Интерактивность<b/>: Бот поддерживает диалог и может адаптироваться к вашим запросам и потребностям.

Этот бот создан для того, чтобы сделать вашу жизнь проще и удобнее, предоставляя полезную информацию и рекомендации в любое время.

<u>Сводка по функционалу</u>:
1. Кнопка продолжить ведёт к дольнейшим инструкциям
2. Фильтрации имеется трёх видов
3. В подробной придётся пройти Опрос по месту назначения, предпочтений, вид заведения и т.п(после прохождения один раз можно будет пользоваться постоянно)
4. По запросу нужно будет выбрать вид заведения
5. Случайное - может выпасть как парк, так и ресторан
6. Добавление в избранное происходит по кнопке с сердечком
7. Просмотреть заведения можно по команде в меню: Избранное
8. При нажатие на название места откроется виджет с местом
9. Редактировать - удаление мест""",
    '/author': 'Разработчик: @enxteu_1, github: @enxtiu.\nПо вопросам или не работы бота писать в тг',
    '/politic': 'Будет позже)',
    'keyboard': {
        'next': 'Продолжить',
        'next_web': '<s>Продолжить в веб.версии</s>',
        'detailed_filter': '<s>Подробная фильтрации</s>',
        'requests_filter': 'Фильтрации по виду заведения',
        'random': 'Случайное место',
        'edit': 'Редактировать',
        'cancel': 'Вернуться'
    },
    'data_requests_filter': 'Выберете интересующий вас вид заведений 👇'
}

def widget(*args) -> str:
    result = f"""Название места: {args[0]}
<b>Описание места<b>: {args[1]}
⭐ <b>Рейтинг на yandex map<b>: {args[2]} - <a href={args[3]}>Подробнее про отзывы</a>
📍 <b>Адрес<b>: {args[4]}
Часы работы: {args[5]}
Контакты: {args[6]}
<a href={args[7]}>Подробнее</a>"""
    return result

