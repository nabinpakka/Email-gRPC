import grpc
from concurrent import futures
import time

import send_email
import send_email_pb2
import send_email_pb2_grpc

class SendEmailServicer(send_email_pb2_grpc.SendEmailServicer):
    def send_email(self, request, context):
        response = send_email_pb2.Response()
        response.response = send_email.send_email(request.password,request.message,request.receiver,request.sender)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
send_email_pb2_grpc.add_SendEmailServicer_to_server(
    SendEmailServicer(),server
)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)