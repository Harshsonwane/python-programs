from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC43e595471763e2e4d3f33203650b05d6"
# Your Auth Token from twilio.com/console
auth_token  = "745c208a7cbe68866838555a504d84fd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917020667432", 
    from_="+18649027730",
    body="dada ky kar raha hai")

print(message.sid)
