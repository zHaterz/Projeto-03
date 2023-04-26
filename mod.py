def sms(*txt):
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "AC1c4b214001e13359ed587278477cf1f4"
    # Your Auth Token from twilio.com/console
    auth_token  = "5470376e028dc37a1efb9976e10f7190"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+5521983854412",
        from_="+16073604246",
        body=(f"{txt}"))

def cole(*txt):
    for c in txt:
        print(c)