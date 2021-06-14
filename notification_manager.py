from twilio.rest import Client

TWILIO_SID = 'AC76d43e9882c9262c50d9bdb2df731261'
TWILIO_AUTH_TOKEN = '0f7a4a95dbf665bdbafbec67fe1e24a9'
TWILIO_VIRTUAL_NUMBER = '+16788654717'
TWILIO_VERIFIED_NUMBER = '+48506694555'



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
