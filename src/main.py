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

	# for KILLBOT cyberattack
	if (code.upper() == "KILLBOT.EXE"):
		print(f"{COLOR.RED}Code not found{COLOR.WHITE}")
		return
	if (code.upper() == f"{COLOR.RED}KILLBOT.EXE{COLOR.WHITE}"):
		print(f"{COLOR.RED}yeah nice try{COLOR.WHITE}")
		return

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
	
	if (GetCyberattack(FIX_KILL)):
		print(f"{COLOR.RED}RklYIEVSUk9SIEVSUk9SIENPREUgTk9UIEZPVU5E{COLOR.WHITE}")
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
	global networkInterface

	networkInterface = True

	while networkInterface:
		if (IsFailure("NO_CONNECTION")):
			failure = GetFailure("NO_CONNECTION")
			print(f"{COLOR.RED}NO_CONNECTION, CODE {failure.code}{COLOR.WHITE}")
			networkInterface = False
			break

		networkInput = input("Network >> ")
		args = networkInput.split(" ")

		if (args[0].lower() in ["exit", "leave"]):
			networkInterface = False
			break

		elif (args[0].lower() != "port"):
			continue

		# all of the next code is for the "port" command
		if (len(args) <= 1):
			print(f"{COLOR.RED}Unknown arguments{COLOR.WHITE}")
			continue

		# view port
		if (args[1].isdecimal()):
			if (int(args[1]) > 1024):
				print(f"{COLOR.RED}Port doesn't exist{COLOR.WHITE}")
				continue

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
			elif (port.state == "LISTENING"): print(f"    {port.internalConnection.ip} <-> NO EXT. CONNECTION")
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
				# has code for a NOT_BOUND type port
				if (portType == "open" and port.open):
					print(f"PORT {port.num} | {port.state} | ", end="")
					if (port.state == "NOT_BOUND"): print(f"No internal IP connected")
					elif (port.state == "LISTENING"): print(f"{port.internalConnection.ip} <-")
					else: print(f"{port.internalConnection.ip} <-> {port.connection.ip}")

				elif (portType == "closed" and not port.open):
					print(f"PORT {port.num} | CLOSED")

				elif (portType.upper() == port.state):
					print(f"PORT {port.num} | {port.state} | ", end="")
					if (port.state == "NOT_BOUND"): print(f"No internal IP connected")
					else: print(f"{port.internalConnection.ip} <-> {port.connection.ip}")
						
		# open / close / disconnect a specific port
		elif (args[1].lower() in ["open", "close", "disconnect", "dc"]):
			if (len(args) <= 2):
				print(f"{COLOR.RED}No port specified{COLOR.WHITE}")
				continue

			if (not args[2].isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			if (int(args[2]) > 1024):
				print(f"{COLOR.RED}Port doesn't exist{COLOR.WHITE}")
				continue

			action = args[1].lower()
			port = ports[int(args[2]) - 1]

			if (action == "open"): 
				port.Open()
				print(f"{COLOR.LIGHTGREEN}Port {port.num} opened{COLOR.WHITE}")
				
			if (action == "close"):
				connection = port.connection
				port.Close()
				print(f"{COLOR.RED}Port {port.num} closed{COLOR.WHITE}")

				if (type(connection) == BAIT):
					AddFailure(NO_CONNECTION(""))
					failure = GetFailure("NO_CONNECTION")
					print(f"{COLOR.RED}NO_CONNECTION ERROR, CODE {failure.code}{COLOR.WHITE}")
					
					networkInterface = False
					break

			if (action in ["dc", "disconnect"]): 
				print(f"Port {port.num} disconnected, disconnected {port.connection.ip}")
				port.Disconnect()

		elif (args[1].lower() == "scan"):
			# finish when i have actual dangers from the network
			pass

		elif (args[1].lower() == "monitor"):
			if (len(args) <= 2):
				print(f"{COLOR.RED}No port specified{COLOR.WHITE}")
				continue

			if (not args[2].isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			port = int(args[2])

			if (port > 1024):
				print(f"{COLOR.RED}Port doesn't exist{COLOR.WHITE}")
				continue

			print("Press ENTER to stop monitoring")

			monitorPortThread = threading.Thread(target=MonitorPort, args=[port])
			monitoringPort = True
			monitorPortThread.start()

			input("")

			monitoringPort = False
			monitorPortThread.join()

def Request(fileName):
	if (IsFailure("NO_CONNECTION")):
		failure = GetFailure("NO_CONNECTION")
		print(f"{COLOR.RED}NO_CONNECTION, CODE {failure.code}{COLOR.WHITE}")
		return

	if (IsFailure("SERVER_ERROR")):
		failure = GetFailure("SERVER_ERROR")
		print(f"{COLOR.RED}SERVER_ERROR, CODE {failure.code}{COLOR.WHITE}")
		return

	filePath = "res/files/" + fileName

	try:
		file = open(filePath, "r")
	except FileNotFoundError:
		print(f"{COLOR.RED}File doesn't exist{COLOR.WHITE}")
		return
	except OSError:
		print(f"{COLOR.RED}File doesn't exist{COLOR.WHITE}")
		return

	text = file.read()	

	corruptor = GetCyberattack(CORRUPTOR)
	if (corruptor != None):
		corruptAmountLUT = (0, 0.01, 0.05, 0.15, 0.3, 0.8)
		text = CorruptText(text, corruptAmountLUT[corruptor.phase])

	print("---------------------------")	
	print(text)
	print("---------------------------")
	file.close()

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

		# cyberattacks that effect power gain	
		powerFeeder = GetCyberattack(POWER_FEEDER)
		overLoader = GetCyberattack(OVERLOADER)
		if (powerFeeder != None):
			if (powerFeeder.uploaded):
				print("a")
				regen *= 1.35

		if (overLoader != None):
			if (overLoader.phase >= 1):
				regen *= 0.5
				preventFailures = [
					"REAC_FAILURE",
					"BACKUP_REAC_FAILURE",
					"COOLER_ERROR"
		       			]
			
				for failure in preventFailures:
					curFailure = GetFailure(failure)
					if (curFailure != None): failures.remove(curFailure)

		time.sleep(regen)

def FailureUpdate():
	global endGame
	global grace

	while True:
		if (endGame): break

		# update loop
		for failure in failures:
			if (failure.name == "CONTAINMENT_ERROR" and failure.breach):
				failure.breach = False
				AddRandomFailure(100)

			if (failure.name == "COOLER_ERROR" and failure.explode):
				failure.explode = False
				endGame = True
				# make proper end later

			failure.Update()

		# player needs to input 'request help.txt' to end grace period
		if (grace):
			grace = False
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
				chance = int(chance * 0.3)
			if (failure.name == "FIREWALL_ERROR" and IsFailure("NETWORK_PROBLEM")):
				chance = int(chance * 0.3)

			randNum = random.randint(1, chance)
			
		if (randNum == 1):
			added = AddFailure(failure)
			if (not added):
				time.sleep(1)
				continue

		time.sleep(1)

def UpgradeUpdate():
	global endGame
	while True:
		if (endGame): break

		for upgrade in upgrades:
			if (IsFailure("CONSTRUCT_SYS_FAILURE")):
				upgrade.upgrading = False
				upgrade.UpdateValues()

			upgrade.Update()

		time.sleep(1)
		
def PortUpdate():
	global endGame
	global xp
	global monitoringPort
	global networkInterface

	while True:
		if (accessTier < 3):
			continue

		for port in ports:
			# for opening ports automatically
			if (not port.open):
				openPort = random.randint(1, 19000) == 1
				if (openPort): port.Open()

			if (port.open):
				closePort = random.randint(1, 1000) == 1
				if (closePort and port.state in ["LISTENING", "IDLE"]): port.Close()

			# adding/modifying connections
			if (port.open):
				internalConnection = random.randint(1, 10) == 1
				if (port.internalConnection == None and internalConnection): 
					connection = copy.deepcopy(random.choice(safeInternalConnections))
					ip = GenerateIP()
					connection.ip = ip
					
					randNum = random.randint(1, connection.chance)

					# changes for special types of connections
					if (type(connection) == BROADCAST):
						broadcastMessages = [
							"Don't forget to stay hydrated!"
						]
						connection.interval = random.randint(10, 40) 
						connection.broadcastText = random.choice(broadcastMessages)

					if (randNum == 1): 
						port.ConnectInternal(connection)
					else: port.ConnectInternal(Connection(ip, ""))

				elif (port.internalConnection != None and internalConnection):
					connection.internalConnection = None

			# for cyberattack updating
			if (type(port.connection) == BUG):
				attack = port.connection
				if (attack.complete): 
					AddRandomFailure(100)
					attack.complete = False

			elif (type(port.connection) == POWER_FEEDER):
				if (port.connection.time == 0):
					CheckAddFailure(REAC_FAILURE(""))
					CheckAddFailure(POWER_FAILURE(""))

			elif (type(port.connection) == DOOR_SHUTDOWN):
				if (port.connection.time == 0):
					for i in range(port.connection.amount): AddFailure(DOOR_FAILURE)

			elif (type(port.connection) == OVERLOADER):
				if (port.connection.phase == 2):
					if (port.connection.time == 59): print(f"{COLOR.RED}WARNING! NUCLEAR REACTOR OVERLOAD DETECTED. RESOLVE IMMEDIATELY! {COLOR.WHITE}")
					if (port.connection.time == 25): print(f"{COLOR.RED}WARNING! NUCLEAR REACTOR IN CRITICAL STATE. RESOLVE IMMEDIATELY! {COLOR.WHITE}")
					if (port.connection.time == 5): print(f"{COLOR.RED}WARNING! NUCLEAR REACTOR MELTDOWN IMMINENT. EVACUATE. {COLOR.WHITE}")

				if (port.connection.phase == 3):
					endGame = True

			elif (type(port.connection) == BAIT):
				xp -= 2
				if (xp < 0):
					xp = 0

			elif (type(port.connection) == BREACHER):
				if (port.connection.time == 0):
					for i in range(port.connection.amount): 
						AddFailure(CONTAINMENT_ERROR(""))
				
				if (port.connection.time == 0):
					port.Disconnect()
					monitoringPort = False
					continue

			elif (type(port.connection) == KILLBOT):
				if (port.connection.time == 0):
					port.Disconnect()
					monitoringPort = False
					networkInterface = False

					AddFailure(NO_CONNECTION(""))
					failures[len(failures) - 1].code = f"{COLOR.RED}KILLBOT.EXE{COLOR.WHITE}"
					print(f"{COLOR.RED}NO_CONNECTION ERROR{COLOR.WHITE}")
					break

			elif (type(port.connection) == REQUEST_FILE):
				if (port.connection.done):
					port.Disconnect()

			port.Update()
			
		time.sleep(1)

def CyberattackUpdate():
	while True:
		# cyberattacks
		cyberattack = copy.deepcopy(random.choice(cyberattacks))
		addAttack = random.randint(1, cyberattack.chance) == 1
			
		port = GetRandomOpenPort(1000)
		if (addAttack and port != None and port.state != "NOT_BOUND"):
			ip = GenerateIP()

			cyberattack.ip = ip
			port.Connect(cyberattack)

		# non malicious connections
		connection = copy.deepcopy(random.choice(safeConnections))
		addConnection = random.randint(1, connection.chance) == 1

		port = GetRandomOpenPort(1000)
		if (addConnection and port != None and port.state != "NOT_BOUND"):
			ip = GenerateIP()
			connection.ip = ip

			if (type(connection) == REQUEST_FILE):
				connection.fileName = "a.txt"
				connection.lifetime = 60

			port.Connect(connection)

		# adds a regular connection if a custom one isnt added
		if (not addConnection and port != None and port.state != "NOT_BOUND"):
			addConnection = random.randint(1, 40) == 1
			if (addConnection):
				ip = GenerateIP()
				port.Connect(Connection(ip, ""))

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

		print(f"   {COLOR.WHITE}- {COLOR.BLUE}Maximum power{COLOR.WHITE} increased to {maxPower}")

		match accessTier:
			case 2:
				print(f"   - {COLOR.BLUE}CONSTRUCTION SYSTEM{COLOR.WHITE} available - use with 'upgrade' command")
				print(f"   - Check mail for more information")

				mails.append(CreateMail("tier2"))

			case 3:
				print(f"   - {COLOR.BLUE}NETWORK SYSTEM{COLOR.WHITE} available - use with 'network' command")
				print(f"   - New threat: {COLOR.BLUE}CYBERATTACKS{COLOR.WHITE}")
				print(f"   - Check mail for more information")

				mails.append(CreateMail("tier3"))
				

def MonitorPort(port):
	port = ports[port - 1]

	while monitoringPort:
		internalConnectionStr = "--"
		if (port.internalConnection != None): internalConnectionStr = port.internalConnection.ip
		connectionStr = "--"
		if (port.connection != None): connectionStr = port.connection.ip

		if (port.data != ""):
			print(f"[{connectionStr} -> {internalConnectionStr}] {port.data}")
		if (port.internalData != ""):
			print(f"[{internalConnectionStr} -> {connectionStr}] {port.internalData}")
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

def AddFailure(failureType):
	chars = "ABCDEF0123456789"
	f = copy.deepcopy(failureType)
	f.code = ""
	for i in range(random.randint(6, 10)):
		f.code += random.choice(chars)
	failures.append(f)

# same as above, but cant add duplicate failures
def CheckAddFailure(failureType):
	if (IsFailure(failureType.name)):
		return
	
	AddFailure(failureType)

def AddRandomFailure(maxIterations):
	failure = random.choice(failureTypes)

	while (IsFailure(failure.name)):
		failure = random.choice(failureTypes)
		maxIterations -= 1

		if (maxIterations == 0): break

	AddFailure(failure)

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

def GetCyberattack(cyberattackType):
	for port in ports:
		if (type(port.connection) == cyberattackType):
			return port.connection
		
	return None

def CorruptText(text, corruptAmount):
	chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()[]{}/|\\'\"+_-="
	textList = []
	doneIndexes = []

	for char in text:
		textList.append(char)

	maxIndex = len(text) - 1
	corruptChars = int(len(text) * corruptAmount)

	for i in range(corruptChars):
		randomIndex = random.randint(0, maxIndex)
		textList[randomIndex] = random.choice(chars)

	text = ""
	for char in textList:
		text += char

	return text

def GenerateIP():
	ipString = ""
	for i in range(4):
		ipString += str(random.randint(1, 255))
		if (i != 3): ipString += "."	
	return ipString

def GetRandomOpenPort(maxIterations):
	port = random.choice(ports)

	while (port.state != "LISTENING"):
		port = random.choice(ports)
		maxIterations -= 1
		if (maxIterations == 0):
			break

	if (port.state != "LISTENING"):
		time.sleep(1)
		return None
	
	return port

endGame = False

grace = True

power = 100
maxPower = 100
xp = 0
maxXP = 100
accessTier = 5
powerRegen = 2 # the higher this is, the slower it is
	       # (seconds between power regens)

failures = []

mails = [CreateMail("start")]

upgrades = [
	Upgrade("Facility Scanner", 1, [80, 120, 135], [30, 45, 80], [1, 3, 4]),
	Upgrade("Nuclear Reactor", 1, [95, 120, 190, 230], [60, 90, 120, 180], [1, 3, 5, 6]),
	Upgrade("Construction System", 1, [100, 110], [60, 150], [3, 4])
]

networkInterface = False
monitoringPort = False
ports = []
for i in range(1024):
	ports.append(
		Port(i + 1, False, "", None, None)
	)

powerUpdate = threading.Thread(target=PowerUpdate)
failureUpdate = threading.Thread(target=FailureUpdate)
upgradeUpdate = threading.Thread(target=UpgradeUpdate)
portUpdate = threading.Thread(target=PortUpdate)
cyberattackUpdate = threading.Thread(target=CyberattackUpdate)
powerUpdate.start()
failureUpdate.start()
upgradeUpdate.start()
portUpdate.start()
cyberattackUpdate.start()

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
		if (len(args) <= 1):
			print(f"{COLOR.RED}No file specified{COLOR.WHITE}")
			continue

		Request(args[1])

	# upgrading is explained in my document, but this will allow
	# the player to upgrade some systems (like the scanner)
	elif (args[0].lower() in ["construction", "upgrade"] and accessTier >= 2):
		UpgradeSystem()

	elif (args[0].lower() == "endgrace"):
		gracePeriod = 0

	elif (args[0].lower() == "network" and accessTier >= 3):
		if (IsFailure("NO_CONNECTION")):
			failure = GetFailure("NO_CONNECTION")
			print(f"{COLOR.RED}NO_CONNECTION, CODE {failure.code}{COLOR.WHITE}")
			continue

		Network()

print("GAME ENDED")

powerUpdate.join()
failureUpdate.join()
upgradeUpdate.join()
portUpdate.join()
cyberattackUpdate.join()