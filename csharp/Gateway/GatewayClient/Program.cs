// Author: Are Oelsner
/* 
 * C# implementation of gRPC Gateway client
 */

using System;
using Grpc.Core;

namespace GatewayClient
{
    class Program
    {
        /// <summary>
        /// Client guide function that takes provided input and makes a request from the server
        /// </summary>
        /// <param name="client"></param>
        /// <param name="request">specifies which electrode's state is being requested</param>
        private static void guide_get_electrode_state(Gateway.Gateway.GatewayClient client, Gateway.ElectrodeNumber request)
        {
            Console.WriteLine("\tgetting electrode {0} state...", request.Number);
            var electrodeState = client.getElectrodeState(request);
            if (electrodeState.State == -1)
            {
                Console.WriteLine("\terror: invalid input: {0} is not a valid electrode", request.Number);
            }
            else
            {
                Console.WriteLine("\telectrode {0} state: {1}", request.Number, electrodeState.State);
            }
        }
        /// <summary>
        /// Client guide function that takes provided input and makes a request from the server
        /// </summary>
        /// <param name="client"></param>
        /// <param name="request">specifies which electrode's state is being set and to what</param>
        private static void guide_set_electrode_state(Gateway.Gateway.GatewayClient client, Gateway.Electrode request)
        {
            Console.WriteLine("\tsetting electrode {0} state to {1}...", request.Number, request.State);
            var electrodeState = client.setElectrodeState(request);
            if (electrodeState.State == -1)
            {
                Console.WriteLine("\terror: invalid input: {0} is not a valid electrode", request.Number);
            }
            else
            {
                Console.WriteLine("\telectrode {0} state set to: {1}", request.Number, electrodeState.State);
            }
        }
        /// <summary>
        /// Main function for Client, handles user input
        /// </summary>
        /// <param name="args"></param>
        public static void Main(string[] args)
        {
            string Port = "127.0.0.1:50051";
            Channel channel = new Channel(Port, ChannelCredentials.Insecure);
            var client = new Gateway.Gateway.GatewayClient(channel);

            var user_input = "";
            string[] command;
            while (user_input != "quit")
            {
                Console.Write("please enter command: ");
                user_input = Console.ReadLine();
                command = user_input.Split(' ');
                if (command[0] == "get")
                {
                    guide_get_electrode_state(client, new Gateway.ElectrodeNumber { Number = Int32.Parse(command[1]) });
                }
                else if (command[0] == "set")
                {
                    guide_set_electrode_state(client, new Gateway.Electrode { Number = Int32.Parse(command[1]), State = Int32.Parse(command[2]) });
                }
                else if (command[0] == "help")
                {
                    Console.WriteLine("get <(int) electrode number(0-3)>");
                    Console.WriteLine("set <(int) electrode number(0-3)> <(int) value(>=0)>");
                }
                else
                {
                    Console.WriteLine("\tinvalid input: {0} is not a valid command", user_input);
                }

            }

            channel.ShutdownAsync().Wait();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}

