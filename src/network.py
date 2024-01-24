import time

class Port:
        def __init__(self, num, open, state, internalConnection = None, externalConnection = None):
                self.num = num
                self.open = open

                # valid states are:
                # LISTENING - 'waiting' for a connection, just free
                # IDLE - no data is being sent but IP is connected to port
                # CONNECTED - sending/recieving data
                self.state = state

                self.internalConnection = internalConnection
                self.externalConnection = externalConnection

                self.internalData = Data("", "")
                self.externalData = Data("", "")

        def Open(self):
                self.open = True
        
        def Close(self):
                self.open = False
                self.Disconnect()

        def Disconnect(self):
                self.externalIP = None

        def ConnectInternal(self, connection):
                self.internalConnection = connection

        def ConnectExternal(self, connection):
                self.externalConnection = connection

        def UpdateState(self):
                if (self.internalConnection == None and self.externalConnection == None):
                        self.state = "LISTENING"
                elif (self.internalData.data != "" or self.externalData.data != ""):
                        self.state = "CONNECTED"
                elif (self.internalConnection != None or self.externalConnection != None):
                        self.state = "IDLE"

        # called every second
        def Update(self):
                if (self.internalConnection != None):
                        self.internalConnection.Update(self)
                        self.internalData = self.internalConnection.data

                if (self.externalConnection != None):
                        self.externalConnection.Update(self)
                        self.externalData = self.externalConnection.data

                self.UpdateState()
                
# to make a special type of connection, make a class and
# use this class as a super class, then change the behaviour
# in the Update() function
class Connection:
        def __init__(self, ip, data):
                self.ip = ip
                self.data = data

        def SendData(self, data):
                self.data = Data(data, "send")

        def RecvData(self, data):
                self.data = Data(data, "recv")

        # called every second while connected to a port
        # called by the port
        def Update(self, port):
                pass

# used to differentiate between recieved data and sent data
# used for monitoring connections
class Data:
        def __init__(self, data, type):
                self.data = data
                self.type = type