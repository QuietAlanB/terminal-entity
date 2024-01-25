import time

class Port:
        def __init__(self, num, open, state, internalConnection = None, connection = None):
                self.num = num
                self.open = open

                # valid states are:
                # LISTENING - 'waiting' for a connection, just free
                # IDLE - no data is being sent but there is a connection
                # CONNECTED - sending/recieving data
                # NOT_BOUND - no internal connection
                
                self.state = state

                self.internalConnection = internalConnection
                self.connection = connection

                self.internalData = ""
                self.data = ""

        def Open(self):
                self.open = True
                self.UpdateState()
        
        def Close(self):
                self.open = False
                self.Disconnect()

        def Disconnect(self):
                self.connection = None
                self.UpdateState()

        def ConnectInternal(self, connection):
                self.internalConnection = connection
                self.UpdateState()

        def Connect(self, connection):
                self.connection = connection
                self.UpdateState()

        def UpdateState(self):
                if (self.internalConnection == None):
                        self.state = "NOT_BOUND"
                elif (self.connection == None and self.internalConnection != None):
                        self.state = "LISTENING"
                elif (self.internalData != "" or self.data != ""):
                        self.state = "CONNECTED"
                elif (self.internalConnection != None and self.connection != None):
                        self.state = "IDLE"

        # called every second
        def Update(self):
                if (self.internalConnection != None):
                        self.internalConnection.Update(self)
                        self.internalData = self.internalConnection.data

                if (self.connection != None):
                        self.connection.Update(self)
                        self.data = self.connection.data

                self.UpdateState()
                
# to make a special type of connection, make a class and
# use this class as a super class, then change the behaviour
# in the Update() function
class Connection:
        def __init__(self, ip, data):
                self.ip = ip
                self.data = data

        def SendData(self, data):
                self.data = data

        # called every second while connected to a port
        # called by the port
        def Update(self, port):
                pass