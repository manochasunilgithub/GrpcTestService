
#Why gRPC? 
#- HTTP/2 based transport - It uses HTTP/2 protocol instead of HTTP 1.1. HTTP/2 protocol provides multiple benefits over the latter. One major benefit is multiple bidirectional streams that can be created and sent over TCP connections parallelly, making it swift. 

#- Auth, tracing, load balancing and health checking - gRPC provides all these features, making it a secure and reliable option to choose.

#- Language independent communication- Two services may be written in different languages, say Python and Golang. gRPC ensures smooth communication between them.

#- Use of Protocol Buffers - gRPC uses protocol buffers for defining the type of data (also called Interface Definition Language (IDL)) to be sent between the gRPC client and the gRPC server. It also uses it as the message interchange format. 
import grpc
import greet_pb2_grpc as pb2_grpc
import greet_pb2 as pb2


class GRPCClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 5000

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.GreeterStub(self.channel)

    def get_CallHello(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.HelloRequest(name=message)
        print(f'{message}')
        return self.stub.SayHello(message)


if __name__ == '__main__':
    client = GRPCClient()
    result = client.get_CallHello(message="Hello Server you there?")
    print(f'{result}')
