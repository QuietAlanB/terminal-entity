import time
import random
from color import COLOR

class Failure:
	def __init__(self, name, code, cost = 0, xp = 0, chance = 0):
		self.name = name
		self.code = code
		self.cost = cost
		self.xp = xp
		self.chance = chance # 1 / chance that this failure occurs when
				     # picked randomly (random pick occurs every
				     # second)

	# called when the player tries to fix the error
	# returns True when the player successfully did the puzzle
	# returns False when the player failed the puzzle
	def Puzzle(self):
		pass

	# this function is called every second
	def Update(self):
		pass


class DOOR_ERROR(Failure):
	def __init__(self, code):
		super().__init__("DOOR_ERROR", code, 5, 15, 15)
		self.time = 40

	def Puzzle(self):
		if (self.name == "DOOR_ERROR"):
			a = random.randint(3, 9)
			b = random.randint(4, 12)
			result = str(a * b)
			print(f"{a} * {b} = ?")
			answer = input(">> ")

			if (answer == result):
				return True
			return False
		
		if (self.name == "DOOR_FAILURE"):
			a = random.randint(3, 6)
			b = random.randint(11, 15)
			result = str(a * b)
			print(f"{a} * {b} = ?")
			answer = input(">> ").strip(" ")

			if (answer != result):
				return False
			
			print("Repeat the character shown:")
			chars = "abcdefghijklmnopqrstuvwxyz0123456789"
			for i in range(7):
				char = random.choice(chars)
				print(f" {char}")
				answer = input(">> ")

				if (char != answer):
					return False
				
			return True

	def Update(self):
		self.time -= 1

		if (self.time <= 0):
			self.name = "DOOR_FAILURE"
			self.cost = 15
			self.xp = 25
			self.chance = 0

class LIGHTS_MALFUNCTION(Failure):
	def __init__(self, code):
		super().__init__("LIGHTS_MALFUNCTION", code, 20, 40, 50)

	def Puzzle(self):
		print("How many dots are shown?")
		amount = random.randint(11, 25)

		for i in range(amount):
			print(".", end="", flush=True)
		print("")

		answer = input(">> ")
		if (answer == str(amount)):
			return True
		
		return False
	
class SITE_BLACKOUT(Failure):
	def __init__(self, code):
		super().__init__("SITE_BLACKOUT", code, 30, 75, 170)

	def Puzzle(self):
		a = random.randint(16, 99)
		b = random.randint(99, 180)
		c = random.randint(11, 140)
		result = a + b - c

		print(f"{a} + {b} - {c} = ?")
		answer = input(">> ").strip(" ")

		if (answer != str(result)):
			return False
		
		d = random.randint(2, 5)
		print(f"Multiply by {d}")
		answer = input(">> ").strip(" ")

		if (answer != str(result * d)):
			return False
		
		return True

class POWER_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("POWER_FAILURE", code, 40, 70, 100)

	def Puzzle(self):
		amount = random.randint(35, 50)
		print(f"Type '00' {amount} times")

		for i in range(amount):
			answer = input("")
			if (answer != "00"):
				return False
			print(f"{amount - i - 1} left")
			
		return True

class REAC_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("REAC_FAILURE", code, 50, 120, 400)

	def Puzzle(self):
		print("Two quick-time events ahead of you, press ENTER to continue", end="")
		input()

		chars = "abcdefghijklmnopqrstuvwxyz0123456789"
		string = ""

		for i in range(12):
			string += random.choice(chars)

		print(f"Quickly rewrite this string of characters in {COLOR.RED}6 seconds{COLOR.WHITE}:")
		print(string)

		startTime = time.time()
		answer = input(">> ").strip(" ")
		endTime = time.time()

		timeTaken = endTime - startTime
		if (timeTaken > 6):
			print(f"Not quick enough (took {round(timeTaken, 2)} seconds)")
			return False
		
		if (answer != string):
			return False
		
		dots = 0
		for x in range(6):
			for y in range(12):
				char = random.choice(". ")
				if (char == "."): dots += 1
				print(char, end="")

			print("")

		print(f"How many dots are shown? You have {COLOR.RED}16 seconds{COLOR.WHITE} to answer.")

		startTime = time.time()
		answer = input(">> ").strip(" ")
		endTime = time.time()

		timeTaken = endTime - startTime

		if (timeTaken > 16):
			print(f"Not quick enough (took {round(timeTaken, 2)} seconds)")
			return False

		if (answer != str(dots)):
			return False
		
		return True

class BACKUP_REAC_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("BACKUP_REAC_FAILURE", code, 35, 90, 380)

	def Puzzle(self):
		a = random.randint(1, 9) + random.choice([0.5, 0])
		b = a + 0.5

		print(f"Type '0' between {a} and {b} seconds")
		print("Press ENTER when you want to begin", end="")
		input("")

		startTime = time.time()
		input(">> ")
		endTime = time.time()

		timeTaken = endTime - startTime

		if (timeTaken < a or timeTaken > b):
			print(f"Incorrect (you stopped it at {round(timeTaken, 2)} seconds)")
			return False
		
		return True

class COOLER_ERROR(Failure):
	def __init__(self, code):
		super().__init__("COOLER_ERROR", code, 30, 55, 150)
		self.time = 120
		self.explode = False

	def Puzzle(self):
		number = random.randint(0, 1000)
		guesses = 10
		print("Guess a random number from 1 to 1000")
		print(f"You have {guesses} guesses")

		while True:
			guess = input(">> ").strip(" ")

			if (not guess.isdecimal()):
				return False
			
			guesses -= 1
			if (guesses == 0): 
				if (int(guess) == number): break
				return False

			if (int(guess) < number): print(f"Higher - {guesses} guess(es) left")
			elif (int(guess) > number): print(f"Lower - {guesses} guess(es) left")
			elif (int(guess) == number): break

		return True
	
	def Update(self):
		if (self.time > 0): self.time -= 1

		if (self.time == 0):
			self.explode = True
			self.time -= 1

		# warning
		if (self.time == 60):
			print(f"{COLOR.DARKRED}WARNING! MAIN REACTOR CORE AT DANGEROUS TEMPERATURES! RESOLVE IMMEDIATELY.{COLOR.WHITE}")

		if (self.time == 10):
			print(f"{COLOR.DARKRED}WARNING! MAIN REACTOR CORE AT CRITICAL STATE! REACTOR MELTDOWN IMMINENT.{COLOR.WHITE}")

class BOILER_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("BOILER_ERROR", code, 10, 25, 80)

	def Puzzle(self):
		a = random.randint(15, 30)
		print(f"Use this character (┅) to draw a line that is {a} long")
		answer = input(">> ")

		if (answer != "┅" * a): return False
		
		a = random.randint(15, 30)
		print(f"Now use this character (╼) to draw a line that is {a} long")
		answer = input(">> ")

		if (answer != "╼" * a): return False

		return True

class SCANNER_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("SCANNER_FAILURE", code, 25, 75, 90)

	def Puzzle(self):
		chars = "abcdefghijklmnopqrstuvwxyz"
		possibleNames = [
			"john", "michael", "jacob", "alex", "dmitrii", "joshua", "kenzo", "kaison", "zain", "saul", "rocco",
			"emma", "maximilian", "mia", "sophie", "zoey", "lucy", "rose", "aubrey", "rachel", "scarlet", "lexi"
		]
		names = []

		# choose names
		for i in range(2):
			chosenName = random.choice(possibleNames)
			names.append(chosenName)
			possibleNames.remove(chosenName)

		print("There are 2 names below that have been encrypted with a cipher.")
		print("This cipher flips letters of the alphabet to the other side (So A -> Z, B -> Y, C -> X, etc.)")
		print("Alphabet for reference: 'abcdefghijklmnopqrstuvwxyz'")
		print("Decode what the 2 names actually are:")

		# print ciphered names
		for name in names: 
			for char in name:
				charIndex = chars.index(char)
				newIndex = len(chars) - 1 - charIndex

				print(chars[newIndex], end="")

			print(" ", end="")
		print("")

		answer = input(">> ").split(" ")

		if (answer[0] != names[0] or answer[1] != names[1]):
			return False
		
		return True

class CONSTRUCT_SYS_FAILURE(Failure):
	def __init__(self, code):
		super().__init__("CONSTRUCT_SYS_FAILURE", code, 35, 65, 135)

	def Puzzle(self):
		lines = ["", "", "", "", ""]
		for i in range(len(lines)):
			for j in range(11):
				choices = ["x", "."]
				if (i == 0 or i == 4): choices = ["-", "="]

				lines[i] += random.choice(choices)

		print("Recreate this shape:")
		for line in lines:
			print(line)
		print("")

		answerLines = [input(), input(), input(), input(), input()]

		for i in range(len(lines)):
			if (lines[i] != answerLines[i]):
				return False
			
		return True

class CONTAINMENT_ERROR(Failure):
	def __init__(self, code):
		super().__init__("CONTAINMENT_ERROR", code, 15, 50, 105)
		self.time = random.randint(60, 90)
		self.breach = False

	def Puzzle(self):
		print("You have 10 seconds to type 12 numbers")
		print("Press ENTER when you would like to begin", end="")
		input()
		
		chars = "0123456789"
		
		startTime = time.time()

		for i in range(12):
			char = random.choice(chars)
			print(f"  {char}")
			answer = input(">> ")
			
			if (answer != char):
				return False
	
		endTime = time.time()

		timeTaken = endTime - startTime

		if (timeTaken > 10):
			print(f"Not quick enough (took {round(timeTaken, 2)} seconds)")
			return False

		return True
	
	def Update(self):
		if (self.time > 0): self.time -= 1

		if (self.time == 0):
			self.breach = True
			self.time -= 1

class NO_CONNECTION(Failure):
	def __init__(self, code):
		super().__init__("NO_CONNECTION", code, 5, 20, 35)

	def Puzzle(self):
		chars = "abcdefghijklmnopqrstuvwxyz0123456789"
		stringList = []
		string = ""
		reverseString = ""

		for i in range(random.randint(15, 25)):
			stringList += random.choice(chars)
		for char in stringList:
			string += char

		stringList.reverse()
		for char in stringList:
			reverseString += char

		print("Write the following string in reverse:")
		print(f"{string}")

		answer = input(">> ").strip(" ")
		
		if (answer != reverseString):
			return False
		
		return True

class NETWORK_PROBLEM(Failure):
	def __init__(self, code):
		super().__init__("NETWORK_PROBLEM", code, 20, 50, 100)

	def Puzzle(self):
		nums = []
		for i in range(10):
			nums.append(random.randint(1, 150))

		print("Sort this list in order from smallest to largest")
		print("You can type '<index 1> <index 2>' to swap 2 elements at those indices")
		print("Keep in mind they are numbered 1 -> 5   ! NOT 0 -> 4 !")
		print(f"[ ", end="")
		for num in nums:
			print(f"{num}", end=" ")
		print("]")
			
		sorted = False
		while (not sorted):
			action = input(">> ")
			indexes = action.split(" ")

			if (len(indexes) <= 1):
				print(f"{COLOR.RED}Input 2 indexes to swap{COLOR.WHITE}")
				continue

			if (not indexes[0].isdecimal() or not indexes[1].isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			try:
				temp = nums[int(indexes[0]) - 1]
				nums[int(indexes[0]) - 1] = nums[int(indexes[1]) - 1]
				nums[int(indexes[1]) - 1] = temp

			except IndexError:
				print(f"{COLOR.RED}Out of list bounds{COLOR.WHITE}")
				continue

			print(f"[ ", end="")
			for num in nums:
				print(f"{num}", end=" ")
			print("]")

			sorted = True
			for i in range(1, len(nums)):
				if (nums[i - 1] > nums[i]):
					sorted = False

		return True

class SERVER_ERROR(Failure):
	def __init__(self, code):
		super().__init__("SERVER_ERROR", code, 15, 50, 110)

	def Puzzle(self):
		print("Write the X and Y coordinates of a faded block to fix it")
		print("in the format of '<x coordinate> <y coordinate>'")
		print("Coordinates start from 1")
		blocks = [
			["█","█","█","█","█","█","█","█","█","█"],
			["█","█","█","█","█","█","█","█","█","█"],
			["█","█","█","█","█","█","█","█","█","█"],
			["█","█","█","█","█","█","█","█","█","█"],
			["█","█","█","█","█","█","█","█","█","█"],
			["█","█","█","█","█","█","█","█","█","█"]
		]

		for i in range(len(blocks)):
			for j in range(len(blocks[i])):
				blocks[i][j] = random.choice(["█", "█", "▒"])
				print(blocks[i][j], end="")
			
			print("")

		clear = False

		while (not clear):
			coordinates = input(">> ")
			coordinates = coordinates.split(" ")

			if (len(coordinates) <= 1):
				print(f"{COLOR.RED}Input an X and Y coordinate seperated by a space{COLOR.WHITE}")
				continue

			x, y = coordinates

			if (not x.isdecimal() or not y.isdecimal()):
				print(f"{COLOR.RED}Not a number{COLOR.WHITE}")
				continue

			x = int(x)
			y = int(y)

			try:
				blocks[y - 1][x - 1] = "█"
			except IndexError:
				print(f"{COLOR.RED}Out of bounds coordinates{COLOR.WHITE}")
				continue

			# show grid
			for block in blocks:
				for cell in block:
					print(cell, end="")
				print("")

			# ending while loop
			clear = True
			for block in blocks:
				for cell in block:
					if (cell != "█"): clear = False

		return True

class FIREWALL_ERROR(Failure):
	def __init__(self, code):
		super().__init__("FIREWALL_ERROR", code, 25, 40, 125)

	def Puzzle(self):
		chars = "roygbp"

		colorString = ""
		for i in range(random.randint(15, 27)):
			colorString += random.choice(chars)

		displayString = ""
		for colorChar in colorString:
			if (colorChar == "r"): displayString += f"{COLOR.RED}█{COLOR.WHITE}"
			elif (colorChar == "o"): displayString += f"{COLOR.ORANGE}█{COLOR.WHITE}"
			elif (colorChar == "y"): displayString += f"{COLOR.YELLOW}█{COLOR.WHITE}"
			elif (colorChar == "g"): displayString += f"{COLOR.LIGHTGREEN}█{COLOR.WHITE}"
			elif (colorChar == "b"): displayString += f"{COLOR.LIGHTBLUE}█{COLOR.WHITE}"
			elif (colorChar == "p"): displayString += f"{COLOR.PURPLE}█{COLOR.WHITE}"

		print("Type the first letter of all of these colors")
		print(displayString)
		answer = input(">> ").strip(" ")

		if (answer != colorString):
			return False
		
		return True

DOOR_FAILURE = DOOR_ERROR("")
DOOR_FAILURE.time = 0
DOOR_FAILURE.Update()

failureTypes = [
	DOOR_ERROR(""),
	DOOR_FAILURE,
	LIGHTS_MALFUNCTION(""),
	SITE_BLACKOUT(""),
	POWER_FAILURE(""),
	REAC_FAILURE(""),
	BACKUP_REAC_FAILURE(""),
	COOLER_ERROR(""),
	BOILER_FAILURE(""),
	SCANNER_FAILURE(""),
	CONSTRUCT_SYS_FAILURE(""),
	CONTAINMENT_ERROR(""),
	NO_CONNECTION(""),
	NETWORK_PROBLEM(""),
	SERVER_ERROR(""),
	FIREWALL_ERROR("")
]