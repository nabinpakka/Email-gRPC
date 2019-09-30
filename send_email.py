import smtplib, ssl
from email.mime.text import MIMEText
#for attaching files to the email
from email.mime.base import MIMEBase
from email import encoders
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

    #attaching file to the mail
    filename= "tcrt5000.pdf"
    attachment =open("./tcrt5000.pdf","rb")
    p = MIMEBase('application','octet-stream')
    #to change payload into encoded form
    p.set_payload((attachment).read())
    #encoding into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    #writing msg and attaching it to the msg
    body = MIMEText(msg,"plain")
    message.attach(body)
    message.attach(p)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string(),)

    return "passed"