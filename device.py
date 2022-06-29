# Author: Are Oelsner
# Python implementation of device
# Represents 4 electrodes

electrode1 = 0
electrode2 = 1
electrode3 = 2
electrode4 = 3
def getElectrode(num):
    match num:
        case 1: return electrode1
        case 2: return electrode2  
        case 3: return electrode3
        case 4: return electrode4
        case _: 
            print("invalid input: " + num)
            return -1