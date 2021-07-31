# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED by @Perfect_Vazha')
idle()
app.stop()
print('\n>>> USERBOT STOPPED by @Perfect_Vazha')

