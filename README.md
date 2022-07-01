Author: Are Oelsner

# Gateway gRPC code simulating communication between an app and a simple neural implant with four electrodes. 
The App and the device communicate through gRPC for getting and setting individual electrode states. 

## Running the server: 
    python ./gateway_server.py

## Running the client: 
    python ./gateway_client.py
    < see Client command formats below>


## Client command formats:
get:
    get <(int) electrode number (0-3)>

set:
    set <(int) electrode number (0-3)> <(int) electrode state(>=0)>

## Example: 
### In one terminal

```
PS C:\PATH\gRPC_Gateway> python .\gateway_server.py
```

### In another terminal

```
PS C:\PATH\gRPC_Gateway> python .\gateway_client.py
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

