import logging
from dotenv import load_dotenv
import os


logger = logging.getLogger('kurwa')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

TG_TOKEN = os.getenv('TOKEN')
logger.error('ffff')
print(TG_TOKEN)
