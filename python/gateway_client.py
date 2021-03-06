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
    if(electrodeState.state == -1):
        print("\terror: invalid input: %i" % (electrodeNum.number))
    else:
        print("\telectrode %i state: %i" % (electrodeNum.number, electrodeState.state))

def guide_set_electrode_state(stub, electrode):
    """ Client guide function that takes provided input (electrode) and makes a request from the stub
    ### Parameters
    1. stub : 
    2. electrode : Electrode message containing int number and int state
    
    ### Returns
    - Any : currently prints out the ElectrodeState returned from the stub and doesn't return anything
    """
    electrodeState = stub.setElectrodeState(electrode)
    if(electrodeState.state == -1):
        print("\terror: invalid input: %i, state not set" % (electrode.number))
    else:
        print("\telectrode %i state set to %i" % (electrode.number, electrodeState.state))


def run():
    """ Initializes Gateway Stub and handles Client input """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gateway_pb2_grpc.GatewayStub(channel)

        user_input = ""
        command = []
        while user_input != "quit":
            user_input = input("please enter command: ")
            command = user_input.split(" ")
            if(command[0] == "help"):
                print("get <(int) electrode number(0-3)>")
                print("set <(int) electrode number(0-3)> <(int) value(>=0)>")
            elif(command[0] == "get"):
                if(len(command) > 1):
                    print("\tgetting electrode %s state..." % (command[1]))
                    guide_get_electrode_state(stub, gateway_pb2.ElectrodeNumber(number=int(command[1])))
            elif(command[0] == "set"):
                if(len(command) > 2):
                    print("\tsetting electrode %s state to %s..." % (command[1], command[2]))
                    guide_set_electrode_state(stub, gateway_pb2.Electrode(number=int(command[1]),  state=int(command[2])))
            else:
                print("invalid input: %s \n Please try again, or enter help for details" % (user_input))

if __name__ == '__main__':
    run()