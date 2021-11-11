using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcTestClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7295");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "Sunil !!" });


Console.WriteLine("Greeting: " + reply.Message);
var reply2 = await client.SayHelloAgainAsync(
                  new HelloRequest { Name = "Sunil !!" });


Console.WriteLine("Greeting Message: " + reply2.Message);

Console.WriteLine("Press any key to exit...");
Console.ReadKey();