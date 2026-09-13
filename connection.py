import os 
from dotenv import load_dotenv
from imbox import Imbox 
from imbox.settings import Config

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD_SECRET = os.getenv('PASSWORD_SECRET')
HOST_IMAP = os.getenv('HOST_IMAP')


config = Config(
    imap_url=HOST_IMAP,
    username=EMAIL,
    password=PASSWORD_SECRET,
    ssl=True,
    ssl_context=None,
    starttls=False
)
def listar_emails(messages, quantityEmail=5):
      for uid, message in messages[-quantityEmail:]:
        print(f"De: {message.parsed.sent_from}\nAssunto: {message.parsed.subject}\n")     
        
with Imbox(config) as imbox:
     messages = imbox.messages(unread=True)
     if not messages:
         quit()

     print('=========== Mensagens ==============')
     listar_emails(messages, 3)
  
     
    
   
     


