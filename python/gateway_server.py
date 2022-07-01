# Author: Are Oelsner
""" Python implementation of Gateway Server  """

from concurrent import futures
import sys
sys.path.append('C:\grpc')
import grpc
import gateway_pb2
import gateway_pb2_grpc

class Device():
    """ Stores electrodes and their states """

    def __init__(self):
        """ Constructor - Initializes electrodes """
        self.electrodes = [0, 0, 0, 0]

    def getElectrode(self, num):
        """ Returns the state of the requested electrode 
        
        Args:
            num(ElectrodeNumber): specifies which electrode's state is requested. Contains (int) number
        Returns:
            (int): state of requested electrode or -1 for invalid request
        """
        if(num < len(self.electrodes)):
            return self.electrodes[num]
        return -1
    
    def setElectrode(self, electrode):
        """ Sets specified electrode's state to the provided state 
        Args:
            electrode(Electrode): Electrode message that contains an int state and int number
    
        Returns:
            ElectrodeState: message containing int value of the requested electrode state, or -1 if invalid input
        """
        if(electrode.number < len(self.electrodes)):
            self.electrodes[electrode.number] = electrode.state
            return self.electrodes[electrode.number]
        return -1


def get_electrode_state(device, electrodeNumber):
    """ Returns state of given electron or -1.  

    Args:
        device(Device): instance of the device class
        electrodeNumber : ElectrodeNumber message that contains an int number 

    Returns:
        ElectrodeState: message containing int value of the requested electrode state, or -1 if invalid input
    """
    return gateway_pb2.ElectrodeState(state=device.getElectrode(electrodeNumber.number))

def set_electrode_state(device, electrode):
    """ Sets specified electrode's state to the provided state 
    Args:
        device(Device): instance of the device class
        electrode(Electrode): Electrode message that contains an int state and int number
    
    Returns:
        ElectrodeState: message containing int value of the requested electrode state, or -1 if invalid input
    """
    return gateway_pb2.ElectrodeState(state=device.setElectrode(electrode))




class GatewayServicer(gateway_pb2_grpc.GatewayServicer):
    """ GatewayServiceer used by the server to implement a gRPC service. 
        
        Provides methods that implement functionality of gateway server.  
    """

    def __init__(self):
        """ Constructor """
        self.device = Device()
        

    def getElectrodeState(self, request, context):
        """ Implements Servicer getElectrodeState function """
        return get_electrode_state(self.device, request)

    def setElectrodeState(self, request, context):
        """ Implements Servicer setElectrodeState function """
        return set_electrode_state(self.device, request)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gateway_pb2_grpc.add_GatewayServicer_to_server(GatewayServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()