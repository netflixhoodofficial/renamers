# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29203173")

API_HASH = os.environ.get("API_HASH", "a381dcb2c26a9c9b1f603a64d7fc51ed")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6861196951:AAHHsUME7u-2rkg6cIsMjX5uKL6jLWzp7dA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002052778414") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "flixhoodbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://flixhoodbot:QwertY@cluster0.ihgqn3q.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5918559647' ).split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
