from twilio.rest import Client

# twilio information
account_sid = 'ACe32f19d54110fbd869514ac17e443ef3'
auth_token = '20f45cc2933d3fd9875c1e6293ee0327'
client = Client(account_sid, auth_token)

def send_notification(other_team):
    message = client.messages \
                    .create(
                         body="Spurs are playing " + other_team + " in five minutes. COYS!",
                         from_='+15034069835',
                         to='+13142952690'
                     )

    message.sid






