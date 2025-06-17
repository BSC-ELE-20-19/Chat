import africastalking

from chattwo import chat

# TODO: Initialize Africa's Talking


username="sandbox"
api_key="atsk_a9c76a831fee0036f7bebd11e5b72961b965cf839779078cd908c7e9d1341400cd5be540"
africastalking.initialize(username,api_key)

sms = africastalking.SMS


def sending(question,phone_number):
    recipients = [f"{phone_number}"]
    message=chat(question)
    sender = 15575

    try:
        response = sms.send(message, recipients, sender)
        print (response)
    except Exception as e:
        print (f'We have a problem: {e}')
def send(self):
        pass #delete this code
