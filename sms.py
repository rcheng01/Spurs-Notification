from twilio.rest import Client
import json

# twilio information
with open("secrets.json", "r") as f:
    secrets = json.loads(f.read())

account_sid = secrets["Twilio_API_ID"]
auth_token = secrets["Twilio_API_Token"]
client = Client(account_sid, auth_token)

def send_notification(other_team):
    message = client.messages \
                    .create(
                         body="Spurs are playing " + other_team + " in five minutes. COYS!",
                         from_='+15034069835',
                         to='+13142952690'
                     )

    message.sid






