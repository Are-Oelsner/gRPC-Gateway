using System;
using System.Threading.Tasks;
using Gateway;
using Grpc.Core;

namespace GatewayServer
{
    /// <summary>
    /// GatewayServer is used by the server to implement a gRPC service
    /// </summary>
    class GatewayServer : Gateway.Gateway.GatewayBase
    {
        /// <summary>
        /// Device instance that stores electrodes
        /// </summary>
        Device device;

        /// <summary>
        /// Constructor initializes device
        /// </summary>
        public GatewayServer()
        {
            device = new Device();
        }
        /// <summary>
        /// Server side handler of the getElectrodeState RPC
        /// </summary>
        /// <param name="request">specifies which electrode's state is being requested</param>
        /// <param name="context"></param>
        /// <returns>(ElectrodeState) state of requested electrode</returns>
        public override Task<ElectrodeState> getElectrodeState(ElectrodeNumber request, ServerCallContext context)
        {
            return Task.FromResult(device.get_electrode_state(request));
        }
        /// <summary>
        /// Server side handler for the setElectrodeState RPC
        /// </summary>
        /// <param name="request">specifies which electrode's state is being set and the value to set it to</param>
        /// <param name="context"></param>
        /// <returns>(ElectrodeState) state of electrode after it is set</returns>
        public override Task<ElectrodeState> setElectrodeState(Electrode request, ServerCallContext context)
        {
            return Task.FromResult(device.set_electrode_state(request));
        }

    }
}
