import os
from pyrogram import Client
from os import mkdir

app_id = int(input("API_ID"))
app_key = input('API_HASH')
token = input('BOT_TOKEN')

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
