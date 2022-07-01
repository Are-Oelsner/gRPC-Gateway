Author: Are Oelsner

Gateway gRPC code simulating communication between an app and a simple neural implant with four electrodes. 
The App and the device communicate through gRPC, and we can get and set individual electrode states. 

Currently implemented: 
Python Client and Server 

Todo:
C# Server

Client command formats:
get:
    get <(int) electrode number (0-3)>

set:
    set <(int) electrode number (0-3)> <(int) electrode state(>=0)>


