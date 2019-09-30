import smtplib, ssl
from email.mime.text import MIMEText
#we can separate subject of msg,from, to etc
from email.mime.multipart import MIMEMultipart


#IMPORTANT the inputs are not taken from here as it runs on server
#not on client side

def send_email(password,msg,receiver,sender):
    #port for ssl
    port = 465

    #create a secure ssl
    context = ssl.create_default_context()

    sender = "nabindpakka706@gmail.com"

    message = MIMEMultipart()
    message["Subject"]="gRPC Email"
    message["From"] = sender
    message["To"]=receiver
    #writing msg and attaching it to the msg
    body = MIMEText(msg,"plain")
    message.attach(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string(),)

    return "passed"