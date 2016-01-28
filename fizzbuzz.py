from twilio.rest import TwilioRestClient

ACCOUNT_SID = "AC9a33684bb61278dec1bb2b47302bcf70"
AUTH_TOKEN = "a37af4a80901bd1b9ab397889a589626"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

call = client.calls.create(url=""
                           to="+18323776562"
                           from_="+2814702492")
