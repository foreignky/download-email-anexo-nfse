from collections import Counter
import os 
from dotenv import load_dotenv
from imbox import Imbox 
from imbox.settings import Config

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD_SECRET = os.getenv('PASSWORD_SECRET')
HOST_IMAP = os.getenv('HOST_IMAP')

download_folder = r"./downloads"

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
        for i, attachment in enumerate(message.parsed.attachments):
            file = attachment.get('filename')
            dowload_path = f"{download_folder}/{file}"
          
            with open(dowload_path, 'wb') as fp:
                fp.write(attachment.get('content').read())
      print('Concluído')      
            
              
    
  


      
with Imbox(config) as imbox:
     messages = imbox.messages(unread=True, subject='Teste Nota', raw='has:attachment')
     if not messages:
         quit()
     listar_emails(messages, 5)
  
     
    
   
     


