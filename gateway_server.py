# Author: Are Oelsner
# Python server 

from concurrent import futures
import sys
sys.path.append('C:\grpc')
import grpc
import gateway_pb2
import gateway_pb2_grpc
import device

def get_electrode_state(electrode_db, electrodeNumber):
    # Returns state of given electron or -1. 
    print("In get_electrode_state")
    print(electrodeNumber)
    electrodeState = electrode_db(electrodeNumber.number) #.state?
    print("Electrode " + electrodeNumber.number + " state: " + electrodeState.state)
    return gateway_pb2.ElectrodeState(state=electrodeState)


class GatewayServicer(gateway_pb2_grpc.GatewayServicer):
    # Provides methods that implement functionality of route guide server. 

    def __init__(self):
        self.db = device.getElectrode # Stores getElectrode function in class variable db

    def getElectrodeState(self, request, context):
        state = get_electrode_state(self.db, request)
        return state

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gateway_pb2_grpc.add_GatewayServicer_to_server(GatewayServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()