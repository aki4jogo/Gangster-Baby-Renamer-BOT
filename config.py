import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29981627")

API_HASH = os.environ.get("API_HASH", "4ff014bdc13d1622424ac0ef2135e40e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5903043731:AAFYoC7n3LmQfbOt6ulUAwxJ_Gz6YXROXf8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@vexx_amv_official") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://imcrazyagt:xt3Zjr8rIFeFKhij@cluster0.k9km7lh.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e3f4f84f35dfaac9b71ca.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6063029619').split()]

PORT = os.environ.get("PORT", "8080")
