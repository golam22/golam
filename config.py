## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuwVoBas5BjEovP8xg7ifYmVoqVAmAPLF60Lmx2pyHf4Yz_jSb5oc9A_DUiox9zWVX37dDtFK9-g2PhE5UxNIF4rgfw1AeT2WZpknV0EUsu2ynxqkP1ArAgZ2BTXhaZMpd6UZW_At2aWjyAWmF5-_BHlxufdgkWPB3JOUdVjaHeG0rf4yk3YNz8BXs-f_SAEgxCEC9c6fh1JsUysMmAysV5r9CvOSNnqtNWf-UPCiprzPvbgXwWN8kV61DTVux8wkdZizTMpS5qs8G2KCW-yRGA9L6VqiUI0uUMRS2DdNLfyP48iMsOmxJnBcPx5Qj2pWokU71vQ9Dr_74dVe3eNZg6U=")
BOT_TOKEN = getenv("BOT_TOKEN", "5422361517:AAE_v1NMzr9uxUkQGorNFw9B27SkxgXTn9k")
BOT_NAME = getenv("BOT_NAME", "لـ طـلب الـعلم")
API_ID = int(getenv("API_ID", "17471548"))
API_HASH = getenv("API_HASH", "60a3a449df977116f4e2f9178fa04b5b")
OWNER_NAME = getenv("OWNER_NAME", "غُــلام")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr4rg")
ALIVE_NAME = getenv("ALIVE_NAME", "غُــلام")
BOT_USERNAME = getenv("BOT_USERNAME", "RR4RGBOT")
OWNER_ID = getenv("OWNER_ID", "5117249907")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RR4RO")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FF89F")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FF89F")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5117249907").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
