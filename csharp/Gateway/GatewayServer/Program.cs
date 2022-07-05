// Author: Are Oelsner
/* 
 * C# implementation of gRPC Gateway Server 
 */

using System;
using System.Threading.Tasks; // I think I would only need this for async calls?
using Grpc.Core;
using Gateway;

namespace GatewayServer
{
    // <summary>Device simulating neural implant with four electrodes </summary>
    // Stores states for four electrodes
    class Device
    {
        public int[] electrodes;

        // <summary> Constructor, initializes default electrode states to 0 </summary>
        public Device()
        {
            this.electrodes = new int[] { 0, 0, 0, 0 };
        }

        // <summary> Returns the state of the requested electrode </summary>
        // <param name="electrodeNumber"> Specifies which electrode's state is requested</param>
        public ElectrodeState get_electrode_state(ElectrodeNumber electrodeNumber)
        {
            if(electrodeNumber.Number < electrodes.Length)
            {
                return new ElectrodeState { State = electrodes[electrodeNumber.Number] };
            }
            return new ElectrodeState { State = -1 };
        }

        public ElectrodeState set_electrode_state(Electrode electrode)
        {
            if(electrode.Number < electrodes.Length)
            {
                electrodes[electrode.Number] = electrode.State;
                return new ElectrodeState { State = electrodes[electrode.Number] };
            }
            return new ElectrodeState { State = -1 };
        }
    }
    class GatewayServer : Gateway.Gateway.GatewayBase
    {
        // Server side handler of the getElectrodeState RPC
        public override Task<ElectrodeState> getElectrodeState(ElectrodeNumber request, ServerCallContext context)
        {
            return Task.FromResult(new ElectrodeState { State = -1}); // TODO change state value passed in?
        }
        // TODO Server side handler for the setElectrodeState RPC
        public override Task<ElectrodeState> setElectrodeState(Electrode request, ServerCallContext context)
        {
            return Task.FromResult(new ElectrodeState { State = -1 }); // TODO change value
        }

    }

    class Program
    {
        const int Port = 30051; // TODO should this be 50051?

        public static void Main(string[] args)
        {
            //GatewayServer server = new GatewayServer();
            //ServerServiceDefinition serverServiceDefinition = Gateway.Gateway.BindService(server);
            //ServerPort Ports = new ServerPort("localhost", Port, ServerCredentials.Insecure);
            
            //server.Start(); // TODO Start not declared in GatewayBase superclass

            Console.WriteLine("Greeter server listening on port " + Port);
            Console.WriteLine("Press any key to stop the server...");
            Console.ReadKey();

            //server.ShutdownAsync().Wait(); // TODO not declared in GatewayBase superclass

        }
    }
}