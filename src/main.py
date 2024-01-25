import time
import os
import sys
import random
import threading
import copy
from color import COLOR
from failures import *
from mail import *
from upgrades import *
from network import *

os.system("")

def ClearScreen():
	print("\x1b[2J")

playStart = False

if (playStart):
	# start
	print("SYSTEM STARTUP")
	time.sleep(0.4)
	print("")
	print("ENTITYLABS-TEC PIL-6")
	print("VERSION 1.1")
	print("DO NOT DISTRIBUTE THIS TECHNOLOGY")
	time.sleep(0.4)
	print("")
	print("Running system check")
	time.sleep(1.2)
	print("MEMORY CHECK ", end="", flush=True)
	time.sleep(0.8)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.2)
	print("    TOP OF RAM IS 7FFFFFFFFFFFFFFF HEX")
	time.sleep(0.4)

	print("CPU CHECK ", end="", flush=True)
	time.sleep(0.6)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.3)
	print("    1.2 GHZ Process speed")
	time.sleep(0.1)
	print("    IOStream check ", end="", flush=True)
	time.sleep(0.9)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.4)

	print("GRAPHICS DISPLAY ", end="", flush=True)
	time.sleep(0.7)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.3)
	print("    60Hz refresh rate")
	time.sleep(0.4)

	print(">> ", end="", flush=True)
	time.sleep(0.8)
	for char in "connect 232.62.99.108:21":
		print(char, end="", flush=True)
		time.sleep(0.02)
	time.sleep(0.4)
	print("")

	time.sleep(0.2)
	print(f"{COLOR.YELLOW}CONNECTING TO ON-SITE NETWORK THROUGH PORT 21...{COLOR.WHITE}")
	time.sleep(2.1)
	print(f"{COLOR.LIGHTGREEN}CONNECTION ESTABLISHED{COLOR.WHITE}")
	time.sleep(0.4)

	print(">> ", end="", flush=True)
	time.sleep(0.6)
	for char in "ping 10.238.44.149 /n 3":
		print(char, end="", flush=True)
		time.sleep(0.02)

	time.sleep(0.2)
	print("")
	time.sleep(0.2)
	print("Pinging 10.238.44.149 with 32 bytes of data:")
	time.sleep(0.75)
	print("    Reply from 10.238.44.149: bytes=32 time=15ms")
	time.sleep(0.75)
	print("    Reply from 10.238.44.149: bytes=32 time=16ms")
	time.sleep(0.75)
	print("    Reply from 10.238.44.149: bytes=32 time=16ms")
	time.sleep(0.75)
	print("")
	time.sleep(3.3)
	print("FTP connection request from 10.238.44.149 at PORT 21")
	time.sleep(0.3)
	print("Accept? y/n")
	time.sleep(0.1)
	print(">> ", end="", flush=True)
	time.sleep(1.1)
	print("y", end="")
	time.sleep(0.2)
	print("")
	time.sleep(0.4)
	
	print(f"{COLOR.LIGHTGREEN}Connection established{COLOR.WHITE}")
	time.sleep(0.2)
	print(f"Downloading data... [1/3]")
	time.sleep(1.8)
	print(f"Downloading data... [2/3]")
	time.sleep(2.2)
	print(f"Downloading data... [3/3]")
	time.sleep(1.3)
	print(f"{COLOR.LIGHTGREEN}Download complete{COLOR.WHITE}")
	time.sleep(0.1)
	
	print(">> ", end="", flush=True)
	time.sleep(0.6)
	for char in "connect_pws.p":
		print(char, end="", flush=True)
		time.sleep(0.02)
	time.sleep(0.3)
	print("")
	time.sleep(1.4)
	print("Connected to PWS_SYS_1 Supply=DC V=13.0 A=4.0")
	time.sleep(0.4)

	print(">> ", end="", flush=True)
	time.sleep(0.2)
	for char in "080.p":
		print(char, end="", flush=True)
		time.sleep(0.02)
	time.sleep(0.1)
	print("")
	time.sleep(0.9)

	print("Checking firmware ", end="", flush=True)
	time.sleep(0.5)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.3)

	print("NETWORK CONNECTION ", end="", flush=True)
	time.sleep(0.6)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.2)

	print("POWER SUPPLY CONNECTION ", end="", flush=True)
	time.sleep(0.7)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.2)

	print("SERVER CONNECTION ", end="", flush=True)
	time.sleep(1.7)
	print(f"[ {COLOR.RED}FAIL{COLOR.WHITE} ]")
	time.sleep(0.2)
	print(f"    {COLOR.YELLOW}CONNECTING TO PORT 22...{COLOR.WHITE}")
	time.sleep(2.1)
	print(f"    {COLOR.LIGHTGREEN}CONNECTION SUCCESSFUL{COLOR.WHITE}")
	time.sleep(0.4)
	print("SERVER CONNECTION ", end="", flush=True)
	time.sleep(0.7)
	print(f"[ {COLOR.LIGHTGREEN}OK{COLOR.WHITE} ]")
	time.sleep(0.3)

	print("Confirming connection with USB_P1_SEND...")
	time.sleep(1.8)
	print(f"    {COLOR.LIGHTGREEN}Confirmed. Heartbeat recieved{COLOR.WHITE}")
	time.sleep(0.7)
	print(f"    080 online")
	time.sleep(0.1)

	print(">> ", end="", flush=True)
	time.sleep(0.5)
	for char in "kc7_terminal.p":
		print(char, end="", flush=True)
		time.sleep(0.02)
	time.sleep(0.3)
	print("")
	time.sleep(0.2)
	print("Starting KILO-CHARLIE-7 MANAGEMENT TERMINAL...")
	time.sleep(1.6)

# terminal commands
def Check():
	percent = round(power / maxPower * 100, 2)
	print("POWER STATUS:", end=" ", flush=True)
	if (percent >= 100): print(f"{COLOR.BLUE}FULL{COLOR.WHITE}")
	elif (percent >= 60): print(f"{COLOR.LIGHTGREEN}HIGH{COLOR.WHITE}")
	elif (percent >= 30): print(f"{COLOR.YELLOW}MEDIUM{COLOR.WHITE}")
	elif (percent >= 10): print(f"{COLOR.ORANGE}LOW{COLOR.WHITE}")
	elif (percent >= 0): print(f"{COLOR.DARKRED}CRITICAL{COLOR.WHITE}")
	print(f"[ {power} / {maxPower} ]")
	print("")
	print(f"ACCESS TIER: {accessTier}")
	print(f"[ {xp} / {maxXP} ]")

def Scan():
	if (IsFailure("SCANNER_FAILURE")):
		failure = GetFailure("SCANNER_FAILURE")
		print(f"{COLOR.RED}SCANNER_FAILURE ERROR, CODE {failure.code}{COLOR.WHITE}")
		return

	print("Scanning for failures...")

	duration = 8
	scannerUpgradeLevel = GetUpgrade("Facility Scanner").level

	match scannerUpgradeLevel:
		case 2: duration = 5
		case 3: duration = 3
		case 4: duration = 1

	# power failure makes systems run slower
	if (IsFailure("POWER_FAILURE")): 
		duration *= 2

	time.sleep(duration)

	if (len(failures) <= 0):
		print(f"{COLOR.LIGHTGREEN}No failures found{COLOR.WHITE}")
		return
	
	print(f"{COLOR.RED}{len(failures)} failure(s) found{COLOR.WHITE}")
	time.sleep(0.3)
	for failure in failures:
		print(f"    {COLOR.RED}{failure.name}, CODE {failure.code}{COLOR.WHITE}")
		time.sleep(0.1)

def Fix(code):
	global power
	global xp

	failure = None
	for failure_ in failures:
		if (failure_.code == code.upper()):
			failure = failure_

	if (failure == None):
		print(f"{COLOR.RED}Code not found{COLOR.WHITE}")
		return
	
	if (power < failure.cost):
		print(f"{COLOR.RED}Not enough power ({failure.cost} needed) {COLOR.WHITE}")
		return

	power -= failure.cost
	fixed = failure.Puzzle()
	if (fixed):
		print(f"{COLOR.LIGHTGREEN}Failure {failure.code} fixed{COLOR.WHITE}")
		AddXP(failure.xp)
		failures.remove(failure)
		return
	
	print(f"{COLOR.RED}Fix was not successful, {failure.code} could not be fixed{COLOR.WHITE}")

def Mails():
	if (IsFailure("NO_CONNECTION")):
		failure = GetFailure("NO_CONNECTION")
		print(f"{COLOR.RED}NO_CONNECTION ERROR, CODE {failure.code}{COLOR.WHITE}")
		return

	if (len(mails) == 0):
		print("No mail in your inbox")
		return

	for i, mail in enumerate(mails):
		print(f"{i + 1} | {mail.author} - {mail.title}")
		
	mailCommand = input("Mail >> ")
	mailArgs = mailCommand.split(" ")

	if (len(mailArgs) <= 1):
		# case for just a number
		if (mailArgs[0].isdecimal()):
			mailArgs.append(f"{mailArgs[0]}")
			mailArgs[0] = "open"
		else:
			return

	if (not mailArgs[1].isdecimal()):
		print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
		return

	index = int(mailArgs[1]) - 1

	if (index > len(mails) - 1 or index < 0):
		print(f"{COLOR.RED}Mail not found{COLOR.WHITE}")
		return

	if (mailArgs[0] in ["open", "read"]):
		mails[index].Print()

	elif (mailArgs[0] in ["del", "delete"]):
		print(f"Deleted mail '{mails[index].title}' by '{mails[index].author}'")
		mails.remove(mails[index])

def UpgradeSystem():
	global power
	constructionSystem = GetUpgrade("Construction System")
	if (constructionSystem.upgrading):
		print(f"{COLOR.RED}CONSTRUCTION SYSTEM CURRENTLY UNDER MAINTENANCE{COLOR.WHITE}")

	for upgrade in upgrades:
		print("---------------")
		if (len(upgrade.powerLevels) == upgrade.level - 1):
			print(f"{COLOR.BLUE}{upgrade.name}{COLOR.WHITE} LEVEL {upgrade.level}")
			print(f"    UPGRADE AT MAX LEVEL")
			continue

		print(f"{COLOR.BLUE}{upgrade.name}{COLOR.WHITE} LEVEL {upgrade.level} -> LEVEL {upgrade.level + 1}")
		if (upgrade.upgrading):
			print(f"    {COLOR.ORANGE}CURRENTLY UPGRADING{COLOR.WHITE}")
			print(f"    TIME LEFT: {upgrade.time} seconds")
			continue

		print(f"    COST: {upgrade.power} power")
		print(f"    TIME: {upgrade.time} seconds")
		if (accessTier < upgrade.access):
			print(f"{COLOR.RED}    ACCESS TIER {upgrade.access} REQUIRED{COLOR.WHITE}")

	print("Type the name of a system to upgrade it")
	upgradeInput = input("Upgrade >> ")

	for upgrade in upgrades:
		if (upgrade.name.lower() != upgradeInput.lower()):
			continue

		if (IsFailure("CONSTRUCT_SYS_FAILURE")):
			failure = GetFailure("CONSTRUCT_SYS_FAILURE")
			print(f"{COLOR.RED}CONSTRUCT_SYS_FAILURE ERROR, CODE {failure.code}{COLOR.WHITE}")
			break

		if (IsFailure("NO_CONNECTION")):
			failure = GetFailure("NO_CONNECTION")
			print(f"{COLOR.RED}NO_CONNECTION ERROR, CODE {failure.code}{COLOR.WHITE}")
			break

		if (len(upgrade.powerLevels) == upgrade.level - 1):
			print(f"{COLOR.RED}Upgrade at max level{COLOR.WHITE}")
			break

		if (power < upgrade.power):
			print(f"{COLOR.RED}Not enough power{COLOR.WHITE}")
			break

		if (upgrade.upgrading):
			print(f"{COLOR.RED}Currently upgrading{COLOR.WHITE}")
			break
		
		if (constructionSystem.upgrading):
			print(f"{COLOR.RED}Construction system currently under maintenance{COLOR.WHITE}")
			break

		upgradeSystemLevel = constructionSystem.level

		maxUpgrades = upgradeSystemLevel
		currentUpgrades = 0
		for upgrade_ in upgrades:
			if (upgrade_.upgrading):
				currentUpgrades += 1

		currentUpgrades += 1

		if (currentUpgrades > maxUpgrades):
			print(f"{COLOR.RED}Maximum concurrent upgrades ({maxUpgrades} upgrades){COLOR.WHITE}")
			break

		power -= upgrade.power

		print(f"Begun upgrading: {upgrade.name}")
		upgrade.StartUpgrade()

		# power failure causes systems to run slower
		if (IsFailure("POWER_FAILURE")): upgrade.time *= 2

def Network():
	global monitoringPort
	inNetworkInterface = True
	
	while inNetworkInterface:
		networkInput = input("Network >> ")
		args = networkInput.split(" ")

		if (args[0].lower() in ["exit", "leave"]):
			inNetworkInterface = False
			break

		elif (args[0].lower() != "port"):
			continue

		# all of the next code is for the "port" command
		if (len(args) <= 1):
			print(f"{COLOR.RED}Unknown arguments{COLOR.WHITE}")
			continue

		# view port
		if (args[1].isdecimal()):
			port = GetPort(int(args[1]))
			print(f"PORT {port.num}")

			openText = "OPEN"
			stateText = port.state
			if (not port.open): 
				openText = "CLOSED"
				stateText = "CLOSED"

			openTextColorDict = {
				"CLOSED": COLOR.RED,
				"OPEN": COLOR.LIGHTGREEN
			}

			stateTextColorDict = {
				"IDLE": COLOR.BLUE,
				"LISTENING": COLOR.YELLOW,
				"CONNECTED": COLOR.LIGHTGREEN,
				"NOT_BOUND": COLOR.RED,
				"CLOSED": COLOR.RED
			}

			print(f"{openTextColorDict[openText]}{openText}{COLOR.WHITE}, ", end="")
			print(f"{stateTextColorDict[stateText]}{stateText}{COLOR.WHITE}")

			print("CONNECTIONS:")
			if (not port.open): print(f"    Port closed")
			elif (port.internalConnection == None): print(f"    No internal IP connected")
			elif (port.state == "IDLE"): print(f"    {port.internalConnection.ip} <-> NO EXT. CONNECTION")
			else: print(f"    {port.internalConnection.ip} <-> {port.connection.ip}")

		# view all ports of a certain type
		elif (args[1].lower() == "list"):
			portType = "open"
			if (len(args) >= 3):
				portType = args[2].lower()

			if (portType not in ["open", "closed", "connected", "idle", "listening", "not_bound"]):
				print(f"{COLOR.RED}Invalid port type{COLOR.WHITE}")
				continue

			print(f"LIST OF {portType.upper()} PORTS:")

			for port in ports:
				if (portType == "open" and port.open):
					print(f"PORT {port.num} | {port.state} | ", end="")
					if (port.state == "NOT_BOUND"): print(f"No internal IP connected")
					else: print(f"{port.internalConnection.ip} <-> {port.connection.ip}")

				elif (portType == "closed" and not port.open):
					print(f"PORT {port.num} | CLOSED")

				elif (portType.upper() == port.state):
					print(f"PORT {port.num} | {port.state} | ", end="")
					if (port.state == "NOT_BOUND"): print(f"No internal IP connected")
					else: print(f"{port.internalConnection.ip} <-> {port.connection.ip}")
						
		# open / close / disconnect a specific port
		elif (args[1].lower() in ["open", "close", "disconnect", "dc"]):
			if (not args[2].isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			action = args[1].lower()
			port = ports[int(args[2]) - 1]

			if (action == "open"): port.Open()
			if (action == "close"): port.Close()
			if (action in ["dc", "disconnect"]): port.Disconnect()
			
		elif (args[1].lower() == "scan"):
			# finish later
			pass

		elif (args[1].lower() == "monitor"):
			if (len(args) <= 2):
				print(f"{COLOR.RED}Please specify a port{COLOR.WHITE}")
				continue

			if (not args[2].isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			port = int(args[2])

			monitorPortThread = threading.Thread(target=MonitorPort, args=[port])
			monitoringPort = True
			monitorPortThread.start()

			input("Press ENTER to stop monitoring")

			monitoringPort = False
			monitorPortThread.join()

# game mechanics
def PowerUpdate():
	global power
	global maxPower
	global powerRegen
	
	while True:
		global endGame
		if (endGame): break

		power += 1

		if (IsFailure("REAC_FAILURE") and IsFailure("BACKUP_REAC_FAILURE")):
			power -= 1

		if (power > maxPower):
			power = maxPower

		# powerRegen changes based on access tier
		regen = powerRegen

		# for nuclear reactor upgrade
		nuclearReactor = GetUpgrade("Nuclear Reactor")

		nuclearReactorRegenLT = (1, 0.9, 0.75, 0.65, 0.5)
		nuclearReactorLevel = nuclearReactor.level
		regen *= nuclearReactorRegenLT[nuclearReactorLevel - 1]

		# if nuclear reactor is being upgraded
		if (nuclearReactor.upgrading):
			regen *= 2

		# for failures that affect power gain
		if (IsFailure("POWER_FAILURE")):
			regen *= 1.5
		if (IsFailure("REAC_FAILURE")):
			regen *= 2
		if (IsFailure("COOLER_ERROR")):
			if (GetFailure("COOLER_ERROR").time > 60):
				regen *= 0.8
			else:
				regen *= 0.6

		time.sleep(regen)

def FailureUpdate():
	global endGame
	global gracePeriod 

	while True:
		if (endGame): break

		# update loop
		for failure in failures:
			if (failure.name == "CONTAINMENT_ERROR" and failure.breach):
				failure.breach = False
				addedFailure = AddFailure(random.choice(failureTypes))

				maxIteration = 200
				while (not addedFailure):
					addedFailure = AddFailure(random.choice(failureTypes))
					maxIteration -= 1

					if (maxIteration == 0): break

			if (failure.name == "COOLER_ERROR" and failure.explode):
				failure.explode = False
				endGame = True
				# make proper end later

			failure.Update()

		# 30 seconds given at the start of the game
		if (gracePeriod > 0):
			gracePeriod -= 1
			time.sleep(1)
			continue

		failure = random.choice(failureTypes)

		randNum = 0
		if (failure.chance >= 1):
			chance = failure.chance

			# these are all for failures that cause other failures more common
			if (failure.name == "POWER_FAILURE" and IsFailure("LIGHTS_MALFUNCTION")):
				chance = int(chance * 0.75)
			if (failure.name == "POWER_FAILURE" and IsFailure("SITE_BLACKOUT")):
				chance = int(chance * 0.4)
			if (failure.name == "LIGHTS_MALFUNCTION" and IsFailure("SITE_BLACKOUT")):
				chance = int(chance * 0.65)
			if (failure.name == "SITE_BLACKOUT" and IsFailure("POWER_FAILURE")):
				chance = int(chance * 0.5)
			if (failure.name == "POWER_FAILURE" and IsFailure("REAC_FAILURE")):
				chance = int(chance * 0.45)
			if (failure.name == "POWER_FAILURE" and IsFailure("BACKUP_REAC_FAILURE")):
				chance = int(chance * 0.6)

			if (failure.name == "CONTAINMENT_ERROR" and IsFailure("BOILER_FAILURE")):
				chance = int(chance * 0.4)

			if (failure.name == "NO_CONNECTION" and IsFailure("NETWORK_PROBLEM")):
				chance = int(chance * 0.2)
			if (failure.name == "FIREWALL_ERROR" and IsFailure("NETWORK_PROBLEM")):
				chance = int(chance * 0.2)

			randNum = random.randint(1, chance)
			
		if (randNum == 1):
			added = AddFailure(failure)
			if (not added):
				time.sleep(1)
				continue

		time.sleep(1)

def UpgradeUpdate():
	while True:
		global endGame
		if (endGame): break

		for upgrade in upgrades:
			if (IsFailure("CONSTRUCT_SYS_FAILURE")):
				upgrade.upgrading = False
				upgrade.UpdateValues()

			upgrade.Update()

		time.sleep(1)

# used to manage leveling up
def AddXP(addXP, reason = "Failure fixed"):
	global xp
	global maxXP
	global accessTier
	global powerRegen
	global maxPower

	xp += addXP

	print(f"{COLOR.WHITE}+{addXP} EXP - {reason}{COLOR.WHITE}")

	if (xp >= maxXP):
		leftoverXP = xp % maxXP
		xp = leftoverXP

		accessTier += 1

		print(f"{COLOR.BLUE}ACCESS TIER {accessTier}{COLOR.WHITE} - UNLOCKED")

		maxXPLT = (200, 350, 500, 780, 1000, 1750)
		maxPowerLT = (110, 130, 150, 200, 250, 300)
		powerRegenLT = (1.2, 0.7, 0.4, 0.2, 0.1, 0.05)

		maxXP = maxXPLT[accessTier - 2]
		maxPower = maxPowerLT[accessTier - 2]
		powerRegen = powerRegenLT[accessTier - 2]

		match accessTier:
			case 2:
				print(f"   {COLOR.WHITE}- {COLOR.BLUE}Maximum power{COLOR.WHITE} increased to {maxPower}")
				print(f"   {COLOR.WHITE}- {COLOR.BLUE}CONSTRUCTION SYSTEM{COLOR.WHITE} available - use with 'upgrade' command")
				print(f"   {COLOR.WHITE}- Check mail for more information")

				mails.append(CreateMail("tier2"))

def MonitorPort(port):
	port = ports[port - 1]

	while monitoringPort:
		if (port.data != ""):
			print(f"[{port.connection.ip} -> {port.internalConnection.ip}] {port.data}")
		if (port.internalData != ""):
			print(f"[{port.internalConnection.ip} -> {port.connection.ip}] {port.data}")
		time.sleep(1)

# utility functions
def IsFailure(failureName):
	for failure in failures:
		if (failure.name == failureName):
			return True
	return False

def GetFailure(failureName):
	for failure in failures:
		if (failure.name == failureName):
			return failure
	return None

# returns True if successfully added
# return False if not added
def AddFailure(failureType):
	if (GetFailure(failureType.name) != None):
		return False

	chars = "ABCDEF0123456789"
	f = copy.deepcopy(failureType)
	f.code = ""
	for i in range(random.randint(6, 10)):
		f.code += random.choice(chars)
	failures.append(f)
	return True

def CreateMail(filename):
	file = open(f"res/mail/{filename}.txt", "r")
	lines = file.readlines()
	file.close()

	author = lines[0].strip("\n")
	subject = lines[1].strip("\n")

	content = ""
	for i in range(3, len(lines)):
		content += lines[i]

	return Mail(author, subject, content)

def GetUpgrade(name):
	for upgrade in upgrades:
		if (upgrade.name == name):
			return upgrade
		
	return None

def GetPort(num):
	return ports[num - 1]

endGame = False

gracePeriod = 30

power = 100
maxPower = 100
xp = 0
maxXP = 100
accessTier = 3
powerRegen = 2 # the higher this is, the slower it is
	       # (seconds between power regens)

failures = []

mails = [CreateMail("start")]

upgrades = [
	Upgrade("Facility Scanner", 1, [80, 120, 135], [30, 45, 80], [1, 3, 4]),
	Upgrade("Nuclear Reactor", 1, [95, 120, 190, 230], [60, 90, 120, 180], [1, 3, 5, 6]),
	Upgrade("Construction System", 1, [100, 110], [60, 150], [3, 4])
]

monitoringPort = False
ports = []
for i in range(1024):
	ports.append(
		Port(i + 1, False, "", None, None)
	)

ports[0].Open()
ports[0].ConnectInternal(Connection("192.168.2.205", ""))
ports[0].Connect(Connection("243.8.98.102", ""))
ports[0].Connect(test("24.4.4.2"))


powerUpdate = threading.Thread(target=PowerUpdate)
failureUpdate = threading.Thread(target=FailureUpdate)
upgradeUpdate = threading.Thread(target=UpgradeUpdate)
powerUpdate.start()
failureUpdate.start()
upgradeUpdate.start()

print("---------- SITE KILO-CHARLIE-7 MANAGEMENT TERMINAL ----------")
print(f"{COLOR.BLUE}Please type 'mail' to view your current emails{COLOR.WHITE}")
print(f"{COLOR.BLUE}Type '1' in the mail interface to view your first mail{COLOR.WHITE}")

while True:
	try:
		inText = input(">> ")
		args = inText.split(" ")
	except KeyboardInterrupt:
		endGame = True

	if (endGame): break
	
	if (args[0].lower() == "check"):
		Check()

	elif (args[0].lower() == "scan"):
		if (power < 5):
			print(f"{COLOR.RED}Not enough power{COLOR.WHITE}")
			continue
		
		power -= 5
		Scan()

	elif (args[0].lower() == "fix"):
		if (len(args) == 1):
			Fix("")
		else:
			Fix(args[1])

	# mails, used to directly inform the player, sort of like a 'help' command
	# also used to inform the player about other issues and some files to recieve using 'request'
	# player may also be able to earn XP from completing tasks in emails
	elif (args[0].lower() in ["email", "mail"]):
		Mails()

	elif (args[0].lower() in ["req", "request"]):
		if (IsFailure("NO_CONNECTION")):
			failure = GetFailure("NO_CONNECTION")
			print(f"{COLOR.RED}NO_CONNECTION, CODE {failure.code}{COLOR.WHITE}")
			continue

		if (IsFailure("SERVER_ERROR")):
			failure = GetFailure("SERVER_ERROR")
			print(f"{COLOR.RED}SERVER_ERROR, CODE {failure.code}{COLOR.WHITE}")
			continue
	
		if (len(args) <= 1):
			print(f"{COLOR.RED}No file specified{COLOR.WHITE}")
			continue

		filePath = "res/files/" + args[1]
		try:
			file = open(filePath, "r")
		except FileNotFoundError:
			print(f"{COLOR.RED}File doesn't exist{COLOR.WHITE}")
			continue
		print("---------------------------")
		print(file.read())
		print("---------------------------")
		file.close()

	# upgrading is explained in my document, but this will allow
	# the player to upgrade some systems (like the scanner)
	elif (args[0].lower() in ["construction", "upgrade"] and accessTier >= 2):
		UpgradeSystem()

	elif (args[0].lower() == "endgrace"):
		gracePeriod = 0

	elif (args[0].lower() == "network" and accessTier >= 3):
		Network()

print("GAME ENDED")

powerUpdate.join()
failureUpdate.join()
upgradeUpdate.join()