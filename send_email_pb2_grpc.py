# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import send_email_pb2 as send__email__pb2


class SendEmailStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_email = channel.unary_unary(
        '/SendEmail/send_email',
        request_serializer=send__email__pb2.Email.SerializeToString,
        response_deserializer=send__email__pb2.Response.FromString,
        )


class SendEmailServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_email(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendEmailServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_email': grpc.unary_unary_rpc_method_handler(
          servicer.send_email,
          request_deserializer=send__email__pb2.Email.FromString,
          response_serializer=send__email__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SendEmail', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
