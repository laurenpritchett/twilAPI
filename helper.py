import os
from twilio.rest import Client

twilio_sid = os.environ['TWILIO_SID']
twilio_token = os.environ['TWILIO_TOKEN']

client = Client(twilio_sid, twilio_token)


def send_marketing_message(marketing_message):
    '''Send a random marketing message to the user.'''

    message = client.messages.create(
        to='+19259806538',
        from_='+19252906483',
        body=marketing_message)

    print(message.sid)
