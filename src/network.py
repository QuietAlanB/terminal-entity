import time
import random
from color import COLOR

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
		self.data = ""
		self.internalData = ""

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
	def __init__(self, ip, data, chance = 0):
		self.ip = ip
		self.data = data
		self.chance = chance  # works the same as failures

	def SendData(self, data):
		self.data = data

	# called every second while connected to a port
	# called by the port
	def Update(self, port):
		pass

# custom AI for connections
# cyberattacks
class BUG(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 240)
		self.time = 60
		self.complete = False
		
	def Update(self, port):
		self.time -= 1
		
		self.SendData(f"uploading FailCause.p ETA {self.time}")
		
		if (self.time == 0):
			self.SendData("upload heartbeat recieved. restarting.")
			self.complete = True
			self.time = 60

class FIX_KILL(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 290)
		self.time = 20
		self.uploaded = False
		self.started = False
		self.fixKill = False
		
	def Update(self, port):
		self.time -= 1

		# first phase, uploading
		if (not self.uploaded):
			self.SendData(f"uploading FKILL.p [ {20 * 67282 - self.time * 67282} / {19 * 67282} ]")

		# second phase, beginning the kill process
		if (self.time == 0 and not self.uploaded and not self.started):
			self.uploaded = True
			self.time = 10
			self.SendData(f"FKILL.p uploaded, begin transmit() process")
			return
		
		# addition on to second phase where it prints this to the port
		# monitor every second
		if (self.time >= 0 and self.uploaded and not self.started):
			num = random.randint(34, 156)
			self.SendData(f"transmit() -> {num}")

			if (self.time == 0):
				self.started = True

		# final phase where it starts sending the pulses
		if (self.time == 0 and self.started):
			self.time = 5
			self.fixKill = True
			self.SendData(f"transmitting kill pulse at 13hz...")
			return
		
		# time in between the "pulses"
		if (self.time > 0 and self.started):
			# equation to get the "count" before it restarts the pulse
			# look i can def make this cleaner i just cant be asked
			count = self.time - (6 - self.time) + -6 + 3 * (6 - self.time)

			self.SendData(f"restarting pulse [{count - 1}/4]")

class POWER_FEEDER(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 330)
		self.time = 50
		self.uploaded = False

	def Update(self, port):
		if (self.time > -1): self.time -= 1

		if (self.time == 0 and not self.uploaded):
			self.uploaded = True
			self.SendData(f"ATTACHED TO PWS_{port.num}_2K, POWER DRAINING STARTED")

		elif (self.time > 0 and not self.uploaded):
			self.SendData(f"ATTACHING TO PWS_{port.num}_2K ETA: {self.time}")

		else:
			volts = random.uniform(4, 23.5)
			self.SendData(f"DRAIN: V={volts} A=4.0 CURRENT=DC")

class DOOR_SHUTDOWN(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 310)
		self.time = 60
		self.amount = random.randint(6, 10)

	def Update(self, port):
		if (self.time > -1): self.time -= 1
		
		if (self.time > 0):
			self.SendData(f"Injecting DOOR_SYS_OVERRIDE.p ...")

		elif (self.time == 0):
			self.SendData(f"Overloading injected software... {self.amount} softwares overloaded.")

		else:
			self.SendData(f"Injected software heartbeat recieved, attempting to spread...")

class OVERLOADER(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 280)
		self.time = 80
		self.phase = 0

	def Update(self, port):
		self.time -= 1

		if (self.time > 0 and self.phase == 0):
			self.SendData(f"UPLOADING OVERLOADER... {self.time}s")

		elif (self.time == 0 and self.phase == 0):
			self.phase = 1
			self.SendData(f"OVERLOADER UPLOADED.")
			return
		
		if (self.phase == 1):
			self.SendData(f"OVERLOADER HEARTBEAT RECIEVED. BEGINNING OVERLOAD.")
			self.phase = 2
			self.time = 60

		if (self.phase == 2):
			self.SendData(f"WAITING FOR SUCCESS PACKET...")

		if (self.phase == 2 and self.time == 0):
			self.SendData(f"SUCCESS.")
			self.phase = 3

class CORRUPTOR(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 210)
		self.time = 180
		self.phase = 0

	def Update(self, port):
		if (self.time > 0): self.time -= 1

		self.SendData(f"CORRUPTING SERVER DATA. CORRUPTING POWER {self.phase}")
		
		if (self.time == 150):
			self.phase = 1
			self.SendData(f"INCREASING CORRUPTING POWER")
		if (self.time == 100):
			self.phase = 2
			self.SendData(f"INCREASING CORRUPTING POWER")
		if (self.time == 60):
			self.phase = 3
			self.SendData(f"INCREASING CORRUPTING POWER")
		if (self.time == 30):
			self.phase = 4
			self.SendData(f"INCREASING CORRUPTING POWER")
		if (self.time == 0):
			self.phase = 5
			self.SendData(f"CORRUPTING SERVER DATA. MAX CORRUPTION POWER REACHED.")

class BAIT(Connection):
	def __init__(self, ip):
		super().__init__(ip, "")
		
	def Update(self, port):
		self.SendData(f"SITE TERMINAL MANAGER FOUND, EXECUTING drain() siphon()")

class BREACHER(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 430)
		self.time = 70	
		self.amount = random.randint(3, 5)

	def Update(self, port):
		if (self.time > -1): self.time -= 1

		if (self.time > 0):
			self.SendData("FINDING CONTAINMENT CHAMBERS...")
		elif (self.time == 0):
			self.SendData(f"FOUND {self.amount} CONTAINMENT CHAMBERS. BEGINNING ERROR SEQUENCE.")

class KILLBOT(Connection):
	def __init__(self, ip):
		super().__init__(ip, "", 600)
		self.time = 15

	def Update(self, port):
		if (self.time > -1): self.time -= 1

		if (self.time > 0):
			self.SendData("Uploading KILLBOT.exe...")
		elif (self.time == 0): self.SendData(f"{COLOR.RED}KLLBOT.EXE{COLOR.WHITE}")

# BAIT is not included in this list because it is
# transmitted by email
cyberattacks = [
	BUG(""),
	FIX_KILL(""),
	POWER_FEEDER(""),
	DOOR_SHUTDOWN(""),
	OVERLOADER(""),
	CORRUPTOR(""),
	BREACHER(""),
	KILLBOT("")
]