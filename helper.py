import os
from twilio.rest import Client
import random

twilio_sid = os.environ['TWILIO_SID']
twilio_token = os.environ['TWILIO_TOKEN']

client = Client(twilio_sid, twilio_token)

BLUSH_MESSAGES = {1: 'Stop by Blush today for $1 off our classic Dragonfruit flavored frozen yogurt!',
                  2: 'Can\'t beat the heat? Cookies and Cream yogurt is only $1 today at Blush!',
                  3: 'What\'s better than ice cream? Blush Frozen Yogurt!',
                  4: 'We miss you at Blush Frozen Yogurt! Come see us soon at Blush!',
                  5: '$3 large frozen yogurt with toppings at Blush- today only!',
                  6: 'Your Blush double points are here! Reply YES to claim.',
                  7: 'Our new Blush Yogurt Mission location is open today!',
                  }


def send_marketing_message():
    '''Send a random marketing message to the user.'''

    marketing_message = random.choice(BLUSH_MESSAGES.values())

    message = client.messages.create(
        to='+19259806538',
        from_='+19252906483',
        body=marketing_message)

    print(message.sid)
