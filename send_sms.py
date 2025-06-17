import africastalking
# TODO: Initialize Africa's Talking


username="sandbox"
api_key="atsk_a9c76a831fee0036f7bebd11e5b72961b965cf839779078cd908c7e9d1341400cd5be540"
africastalking.initialize(username,api_key)

sms = africastalking.SMS
def sending():
    # Set the numbers in international format
    recipients = ["+265994136905","+265998137309","+265888391093"]
    # Set your message
    message = "Bulk SMS TESTING TESTING"
    # Set your shortCode or senderId
    sender = "ACADES"
    try:
        response = sms.send(message, recipients, sender)
        print (response)
    except Exception as e:
        print (f'Houston, we have a problem: {e}')
def send(self):

    pass #delete this code