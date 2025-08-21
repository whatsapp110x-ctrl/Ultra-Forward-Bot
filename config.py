import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "29756601")
    API_HASH = environ.get("API_HASH", "967c4656b8dd6a475b7786e3287ba2d3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8372107408:AAEdnBUYJLmDhOKycjQHsvN30bmKjfCejcY") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://whatsapp110x:whatsapp110x@cluster0.dh2ygtt.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "NastyBot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7052170756').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002319385484'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/XDemonHunter_Channel") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
