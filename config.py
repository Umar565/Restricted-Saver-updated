# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9972455"))
API_HASH = getenv("API_HASH", "5b1fd83b698e4e6670f3dcb053eecc06")
BOT_TOKEN = getenv("BOT_TOKEN", "7212745746:AAF0ocuS_1eFzwfhkjr4WZRv_tzRTqlGME0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6928637808").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Restrictedbotforeveryone:publicontentsaver@restrictedbot.yah0l.mongodb.net/?retryWrites=true&w=majority&appName=Restrictedbot")
LOG_GROUP = getenv("LOG_GROUP", "-1002357764876")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002234404301"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
