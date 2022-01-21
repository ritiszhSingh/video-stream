import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBYjCXw3wNi6gpS_Zjh-xMpuGUgOTIhDUKrvlPBzaFOfcNBzKUiBI2QRa_AYP7p6IbRpy12Bpzf9AGjFz6IW5nMoKtcCjeJOrMuB5Q2XB34dd8tWfDfum14Jwg9H1mYG78pXSjBWzrvNC7TYHsJmx-dhFY6ng9ilpm8g7ysNEfI7LN8IHqlWcj1OoF1qdJI4bMWq5CR9tZi4Jl1v2MtLm6WGxUYOyopXKgS_4V_95cUZLTlUHXLcaHcNMl83oaEqUNBvQrTv08Q3k7bfuhEeQtjRHL8pEVYVEFnIkQDszx3f3PXRsMupvHOCZGSbraSZG9NqohU2JOVPtIsxmOs5QG3dNs7EAA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "『匚ᴀʀ🇬ᴀ丂ᴍ』 ᴠᴄ ᴘʟᴀʏᴇʀ")
API_ID = int(getenv("API_ID" "11259645")
API_HASH = getenv("API_HASH" "2a0091696eecde4ae7c3f76cbf848c53")
OWNER_NAME = getenv("OWNER_NAME", "𝐑𝐈𝐓Σ𝐒𝐇🥀『")
ALIVE_NAME = getenv("ALIVE_NAME", "『匚ᴀʀ🇬ᴀ丂ᴍ』)
BOT_USERNAME = getenv("BOT_USERNAME", "@ritiszh_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cargasm_ritesh")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "-1001776335996")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ritiszh_Op")
SUDO_USERS = list(map(int, getenv("SUDO_USERS" "1960524560
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
