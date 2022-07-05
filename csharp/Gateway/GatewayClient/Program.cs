// Author: Are Oelsner
/* 
 * C# implementation of gRPC Gateway client
 */

using System;
using Grpc.Core;
using Gateway;

namespace GatewayClient
{
    class Program
    {
        public static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:30051", ChannelCredentials.Insecure); // TODO change port to 50051 to match python implementation?
            
            var client = new Gateway.Gateway.GatewayClient(channel);

            var reply = client.getElectrodeState(new ElectrodeNumber { Number = 0 });
            Console.WriteLine(reply.State);
            
            channel.ShutdownAsync().Wait();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}