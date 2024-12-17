LEXICON = {
'/start': """
Hello! I am your personal guide and assistant for recommendations of places. I will help you find the best restaurants, cafes, parks, museums and other interesting places. If you like a place, you can save it to your favorites so that you don't forget it.

Here's what I can do for you:

👉 <u>Recommend places based on your preferences.</u>

👉 <u>Provide information about the locations, including the address, opening hours and reviews.</u>

👉 <u>Save your favorite places to favorites for quick access.</u>

If you want to find out more information about my functionality, author, or privacy policy, you can use the menu located on the bottom left of the screen)

Shall we start? Just click on continue and I'll pick the best options for you!
ps: Unfortunately some functionality is not available yet, so it will be crossed out, but I hope it will be available soon) """,
    'menu_des': {
    'start': 'restart bot',
    'description': "Description of the bot's capabilities",
    'author': 'Tech support',
    'politic': 'Privacy Policy',
    'favorites': 'Selected establishments'},

    '/description': """<b>Description of the bot</b>
This bot was created to help users find interesting places and save them to favorites.
It has a wide range of features and functions that make it a useful and convenient tool for everyday use.

<u>The main functions of the bot:</u>
<b>1) Recommendations of places:</b>

The bot can recommend various places such as restaurants, cafes, parks, museums and other interesting locations based on your preferences and interests.

Provides detailed information about locations, including address, opening hours, reviews and ratings.

<b>2) Save to favorites:</b>

👉 You can save your favorite places to favorites so that you can easily find them in the future.

👉 Manage the list of favorite places, add and delete entries.

<b>3) Carrying out the path to the selected location:</b>

The bot can plot a route to a selected location by providing step-by-step instructions and transport information.

👉 Helps you get to your destination in the most convenient and fastest way.

<u>Summary of the functionality</u>:
1. The continue button leads to the most detailed instructions
2. There are three types of filtration
3. In the detailed form, you will have to take a survey by destination, preferences, type of institution, etc. (after passing once you can use it all the time)
4. Upon request, you will need to select the type of institution
5. Random - both a park and a restaurant can fall out
6. Adding to favorites is done by clicking the heart button
7. You can view the establishments by clicking on the command in the menu: Favorites
8. When you click on the place name, a widget with the place will open
9. Edit - delete places""",
    '/author': "Developer: @enxteu_1, github: @enxtiu. If you have questions or not about the bot's work, write to tg",
    '/politic': 'It will be later)',
    'keyboard': {
'next': 'Continue',
        'next_web': '<s>Continue to the web.versions</s>',
        'detailed_filter': '<s>Detailed filtering</s>',
        'requests_filter': 'Filtering by type of institution',
        'random': 'Random location',
        'edit': 'Edit',
        'cancel': 'Return'
    },
    'data_requests_filter': 'Choose the type of establishments you are interested in 👇'
}

def widget(*args) -> str:
    result = f"""Place name: {args[0]}
<b>Place description<b>: {args[1]}
⭐ <b>Rating on yandex map<b>: {args[2]} - <a href={args[3]}>Learn more about reviews</a>
📍 <b>Address<b>: {args[4]}
Opening hours: {args[5]}
Contacts: {args[6]}
<a href={args[7]}>Learn more</a>"""
    return result
