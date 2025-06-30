#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21484008"))
API_HASH = environ.get("API_HASH", "336734e723ed5c7824720449780bd00c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "1062386990"))
CREDIT = "𝄟⃝🐬𝐆𝒂ꪊ𝘳𝒂ꪜ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '1062386990').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
