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
        self.electrode1 = 0
        self.electrode2 = 1
        self.electrode3 = 2
        self.electrode4 = 3

    def getElectrode(self, num):
        """ Returns the state of the requested electrode 
        
        Args:
            num(ElectrodeNumber): specifies which electrode's state is requested. Contains (int) number
        Returns:
            (int): state of requested electrode or -1 for invalid request
        """
        print("Getting electrode %i state..." % (num))
        if(num == 3):
            return 2
        match num:
            case 1: return self.electrode1
            case 2: return self.electrode2
            case 3: return self.electrode3
            case 4: return self.electrode4
            case _: return -1

def get_electrode_state(device, electrodeNumber):
    """ Returns state of given electron or -1.  

    Args:
        electrode_db: function that takes in a number (1-4)
        electrodeNumber : ElectrodeNumber message that contains an int number 

    Returns:
        ElectrodeState: message containing int value of the requested electrode state, or -1 if invalid input
    """
    electrodeState = device.getElectrode(electrodeNumber.number)
    print("get_electrode_state::electrode %i state: %i" % (electrodeNumber.number, electrodeState))
    return gateway_pb2.ElectrodeState(state=electrodeState)

class GatewayServicer(gateway_pb2_grpc.GatewayServicer):
    """ GatewayServiceer used by the server to implement a gRPC service. 
        
        Provides methods that implement functionality of gateway server.  
    """

    def __init__(self):
        """ Constructor """
        self.device = Device()
        

    def getElectrodeState(self, request, context):
        state = get_electrode_state(self.device, request)
        return state

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gateway_pb2_grpc.add_GatewayServicer_to_server(GatewayServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()