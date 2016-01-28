import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9a33684bb61278dec1bb2b47302bcf70"
auth_token  = "a37af4a80901bd1b9ab397889a589626"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+18323776562",    # Replace with your phone number
    from_="+12818702492") # Replace with your Twilio number
print message.sid
