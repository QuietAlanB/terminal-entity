import time
import random
from color import COLOR

class Server:
	def __init__(self, name, ip):
		self.name = name
		self.ip = ip
		self.state = "CLOSED"
		self.clients = []

		self.time = 0

	def AddClient(self, client):
		self.clients.append(client)

	def RemoveClient(self, client):
		self.clients.remove(client)

	def GetClient(self, ip):
		for client in self.clients:
			if (client.ip == ip):
				return client
		return None
	
	def IsActive(self):
		return self.state in ["OPEN", "CLOSED"]

	def SetState(self, state):
		self.state = state

	def Update(self):
		if (self.state in ["REBOOTING", "FLUSHING"]):
			self.time -= 1
			if (self.time == 0):
				self.state = "OPEN"

		for client in self.clients:
			client.Update()

class Client:
	def __init__(self, ip, chance = 0):
		self.ip = ip
		self.chance = chance

	def Update(self):
		pass

	def Flush(self):
		pass

	# still need to figure out what this will do
	def Diagnose(self, num):
		pass

