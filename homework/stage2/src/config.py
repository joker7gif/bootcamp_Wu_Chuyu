from dotenv import load_dotenv
import os 

def load_env():
    load_dotenv()


def get_key():
    api_key = os.getenv("API_KEY")
    return api_key