// Author: Are Oelsner
/* 
 * C# implementation of gRPC Gateway Server 
 */


using System;
using Grpc.Core;

namespace GatewayServer
{
    public class Program
    {
        const int Port = 50051;
        /// <summary>
        /// Main method for Server, sets up and starts server
        /// </summary>
        /// <param name="args"></param>
        public static void Main(string[] args)
        {
            Server server = new Server
            {
                Services = { Gateway.Gateway.BindService(new GatewayServer()) },
                Ports = { new ServerPort("localhost", Port, ServerCredentials.Insecure) }
            };
            server.Start();

            Console.WriteLine("Greeter server listening on port " + Port);
            Console.WriteLine("Press any key to stop the server...");
            Console.ReadKey();

            server.ShutdownAsync().Wait();

        }
    }
}