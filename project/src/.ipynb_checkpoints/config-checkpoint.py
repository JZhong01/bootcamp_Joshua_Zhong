from dotenv import load_dotenv
import os

def load_env(path=".env"):
    load_dotenv(path)

def get_key(name):
    return os.getenv(name)
