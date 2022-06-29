# Author: Are Oelsner
# Python implementation of the gRPC gateway client

from __future__ import print_function

import sys
sys.path.append('C:\grpc')

import grpc
import gateway_pb2
import gateway_pb2_grpc

def guide_get_electrode_state(stub, electrodeNum):
    electrodeState = stub.getElectrodeState(gateway_pb2.ElectrodeNumber(number=electrodeNum.number))
    # electrodeState = stub.getElectrodeState(electrodeNum)
    print("end of guide_get_electrode_state!!")
    #print("Electrode %i state: %i", electrodeNum.number, electrodeState.state)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gateway_pb2_grpc.GatewayStub(channel)
        print("Getting electron 1 state")
        #guide_get_electrode_state(stub, gateway_pb2.ElectrodeNumber(number=1))
        guide_get_electrode_state(stub, gateway_pb2.ElectrodeNumber(number=1))
"""         print("Getting electron 2 state")
        guide_get_electrode_state(stub, 2)
        print("Getting electron 3 state")
        guide_get_electrode_state(stub, 3)
        print("Getting electron 4 state")
        guide_get_electrode_state(stub, 4) """

if __name__ == '__main__':
    run()