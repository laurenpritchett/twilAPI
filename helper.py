import os
from twilio.rest import Client

twilio_sid = os.environ['TWILIO_SID']
twilio_token = os.environ['TWILIO_TOKEN']

client = Client(twilio_sid, twilio_token)

message = client.messages.create(
    to="+19259806538",
    from_="+19252906483",
    body="Hello from Python!")

print(message.sid)
