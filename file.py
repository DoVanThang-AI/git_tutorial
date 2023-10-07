import os
from dotenv.main import load_dotenv
load_dotenv()

name = os.environ['name']
print(name)
