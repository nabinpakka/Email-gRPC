import grpc

import send_email_pb2
import send_email_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

client = send_email_pb2_grpc.SendEmailStub(channel)

sender =input("Sender address:")
password = input("Enter your password")
receiver = input("Receiver address:")
body = input("Body of mail:")

message = send_email_pb2.Email(receiver=receiver,password=password,message=body,sender=sender)

#calling the function
response = client.send_email(message)

print(response)