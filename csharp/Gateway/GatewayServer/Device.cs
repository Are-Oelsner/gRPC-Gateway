using System;
using Gateway;

namespace GatewayServer
{
    /// <summary>
    /// Device simulating neural implant with four electrodes
    /// </summary>
    class Device
    {
        /// <summary>
        /// Static array storing electrode states as ints
        /// </summary>
        public static int[] electrodes = { 0, 0, 0, 0 };
        /// <summary>
        /// Returns the state of the requested electrode
        /// </summary>
        /// <param name="electrodeNumber">Specifies which electrode's state is requested</param>
        /// <returns>(ElectrodeState) State of requested electrode</returns>
        public static ElectrodeState get_electrode_state(ElectrodeNumber electrodeNumber)
        {
            Console.WriteLine("\tgetting electrode {0} state...", electrodeNumber.Number);
            if (electrodeNumber.Number < electrodes.Length)
            {
                Console.WriteLine("\treturning electrode {0} state: {1}", electrodeNumber.Number, electrodes[electrodeNumber.Number]);
                return new ElectrodeState { State = electrodes[electrodeNumber.Number] };
            }
            Console.WriteLine("\terror: electrode {0} not found. returning -1", electrodeNumber.Number);
            return new ElectrodeState { State = -1 };
        }
        /// <summary>
        /// Sets specified electrode's state to the provided state
        /// </summary>
        /// <param name="electrode">message that contains an int State and int Number</param>
        /// <returns>(ElectrodeState) message containing int value of the requested electrode state, or -1 if invalid input</returns>
        public static ElectrodeState set_electrode_state(Electrode electrode)
        {
            Console.WriteLine("\tsetting electrode {0} state to {1}...", electrode.Number, electrode.State);
            if (electrode.Number < electrodes.Length)
            {
                electrodes[electrode.Number] = electrode.State;
                Console.WriteLine("\treturning electrode {0} state: {1}", electrode.Number, electrodes[electrode.Number]);
                return new ElectrodeState { State = electrodes[electrode.Number] };
            }
            Console.WriteLine("\terror: electrode {0} not found. returning -1", electrode.Number);
            return new ElectrodeState { State = -1 };
        }
    }
}
