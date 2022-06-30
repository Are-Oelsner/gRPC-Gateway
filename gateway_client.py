# Author: Are Oelsner
""" Python implementation of the gRPC gateway client """

from __future__ import print_function

import sys
sys.path.append('C:\grpc')

import grpc
import gateway_pb2
import gateway_pb2_grpc

def guide_get_electrode_state(stub, electrodeNum):
    """ Client guide function that takes provided input (electrodeNum) and makes a request from the stub
    ### Parameters
    1. stub : 
    2. electrodeNum : ElectrodeNumber message containing int number
    
    ### Returns
    - Any : currently prints out the ElectrodeState returned from the stub and doesn't return anything
    """
    electrodeState = stub.getElectrodeState(electrodeNum)
    # electrodeState = stub.getElectrodeState(gateway_pb2.ElectrodeNumber(number=electrodeNum))
    print("Electrode %i state: %i" % (electrodeNum.number, electrodeState.state))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gateway_pb2_grpc.GatewayStub(channel)

        user_input = ""
        command = []
        while user_input != "quit":
            user_input = input("please enter command: ")
            command = user_input.split(" ")
            if(command[0] == "help"):
                print("get <(int) electrode number>")
                print("set <(int) electrode number> <(int) value>")
            elif(command[0] == "get"):
                if(len(command) > 1):
                    print("Getting electrode %s state" % (command[1]))
                    guide_get_electrode_state(stub, gateway_pb2.ElectrodeNumber(number=int(command[1])))
            elif(command[0] == "set"):
                if(len(command) > 2):
                    print("Setting electrode %i state to %i" % (command[1], command[2]))
            else:
                print("invalid input: %s \n Please try again, or enter help for details" % (user_input))

if __name__ == '__main__':
    run()