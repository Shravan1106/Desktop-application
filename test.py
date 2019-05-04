#from twilio.rest import TwilioRestClient
from twilio.rest import Client


#----------------------------------------------------------------------
def send_sms(msg, to):
    """"""
    sid = "ACb78f700e33a4fd49b88732b4ae9ff98d"
    auth_token = "6d18566e439f4849ab824e0594871f51"
    twilio_number = "+19186094397"

    #client = TwilioRestClient(sid, auth_token)
    tClient= Client(sid, auth_token)
    message = tClient.messages.create(body=msg,
                                     from_='+19186094397',
                                     to='+919121931106',
                                     )

if __name__ == "__main__":
    msg = "thanks for shopping..!!"
    to = "+919121931106"
    send_sms(msg, to)

