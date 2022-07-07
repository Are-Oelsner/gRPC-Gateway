Author: Are Oelsner

# Gateway gRPC code simulating communication between an app and a simple neural implant with four electrodes. 
The App and the device communicate through gRPC for getting and setting individual electrode states. 

## Client command formats:
get:
    get <(int) electrode number (0-3)>

set:
    set <(int) electrode number (0-3)> <(int) electrode state(>=0)>


# Python
## Compiling Proto to python
from gRPC_Gateway directory
```
// <python protoc compiler> -I<path to protos folder> --python_out=<path to new pb2 file> --grpc_python_out=<path to new pb2_grpc file> <path to proto file>
$ python -m grpc_tools.protoc -I./protos --python_out=./python --grpc_python_out=./python ./protos/gateway.proto   
```
## Running the server: 
    python ./python/gateway_server.py

## Running the client: 
    python ./python/gateway_client.py
    < see Client command formats above>

## Example: 
### In one terminal

```
PS C:\PATH\gRPC_Gateway> python .\python\gateway_server.py
```

### In another terminal

```
PS C:\PATH\gRPC_Gateway> python .\python\gateway_client.py
please enter command: get 1
        getting electrode 1 state...
        electrode 1 state: 0
please enter command: set 1 100
        setting electrode 1 state to 100...
        electrode 1 state set to 100
please enter command: get 1
        getting electrode 1 state...
        electrode 1 state: 100
```




# C#
## Building the client and server
    dotnet build .\csharp\Gateway\

## Running the server 
    dotnet run --project .\csharp\Gateway\GatewayServer\GatewayServer.csproj

## Running the client
    dotnet run --project .\csharp\Gateway\GatewayClient\GatewayClient.csproj
    <see client command formats above>

# Doxygen
## Building Documentation
```
$ doxygen doxygen-config-file
```

Load constructed documentation/API by accessing ./documentation/html/index.html in your browser

