import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token_for_sms")
BASE_URL = os.getenv("base_url_for_sms")


headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# SMS Yuborish
def send_sms(phone: str, message: str) -> dict:
    response = requests.post(
        f"{BASE_URL}/send_sms.php",
        headers=headers,
        json={
            "phone": phone,
            "message": message
        }
    )
    return response.json()


def generate_code():
    import random

    d1 = random.randint(0, 9)
    d2 = random.randint(0, 9)
    d3 = random.randint(0, 9)
    d4 = random.randint(0, 9)

    return f"{d1}{d2}{d3}{d4}"