class Guess:

	import random as random

	DELIM = '\n'

	CONST_MIN = 0

	CONST_MAX = 10000

	CONST_MAX_LOWER = 1000

	DEFAULT_FILE = "Saved.dat"

	AI_COUNT = 0

	AI_FILE = "ai.dat"


	def __init__(self, MINIMUM, MAXIMUM, TARGET, FILENAME=None, AI=None):
		self.MINIMUM = MINIMUM
		self.MAXIMUM = MAXIMUM
		if TARGET == -1:
			self.TARGET = self.RNG(self.MINIMUM, self.MAXIMUM)
		else:
			self.TARGET = TARGET

		if MINIMUM == -1:
			self.MINIMUM = self.RNG(self.CONST_MIN, self.CONST_MAX_LOWER)
			self.MAXIMUM = self.RNG(self.MINIMUM, self.CONST_MAX)
			self.TARGET = self.RNG(self.MINIMUM, self.MAXIMUM)

		if FILENAME is None:
			self.FILENAME = self.DEFAULT_FILE
		else: self.FILENAME = FILENAME
		self.TRIES = 0

	def ai_Play(self, MIN=None, MAX=None):
		if MIN is None:
			ai_Min = self.MINIMUM
		else: ai_Min = MIN
		if MAX is None:
			ai_Max = self.MAXIMUM
		else: ai_Max = MAX

		ai_temp = self.RNG(ai_Min, ai_Max)


		self.AI_COUNT += 1

		x = self.is_Answer(ai_temp)
		if x == 1:
			self.AI_COUNT += 1
			return self.ai_Play(ai_Min, ai_temp)
		elif x == 0:
			self.AI_COUNT += 1
			return self.ai_Play(ai_temp, ai_Max)
			#ai_att += 1
		elif x == -1:
			print(f'it took {self.AI_COUNT} tries... the number was {ai_temp}')
			self.saveGame(self.AI_FILE, self.AI_COUNT)
			total, times = self.loadHistory(self.AI_FILE)
			avg = total / times
			print(f'In total you have {total} attempts over the course of {times} Games.\n')
			print(f'On Avg. The AI Takes {avg:.2f}, over {times} Games.')

		return None


	def is_Answer(self, n):
		if n > self.TARGET:
			return 1
		if n < self.TARGET:
			return 0
		if n == self.TARGET:
			return -1

	def playGame(self):
		try:
			userINPUT = int(input(f'Please guess a number between {self.MINIMUM} through {self.MAXIMUM}: '))
		except:
			userINPUT = int(input(f'Please guess a valid number between {self.MINIMUM} through {self.MAXIMUM}: '))
		self.TRIES += 1
		while userINPUT != self.TARGET:
			if userINPUT > self.TARGET:
				try:
					userINPUT = int(input("\nToo High\nTry again: "))
				except:
					userINPUT = int(input("\nInvalid Input: "))
				self.TRIES += 1
			elif userINPUT < self.TARGET:
				try:
					userINPUT = int(input("\nToo Low\nTry again: "))
				except:
					userINPUT = int(input("\nInvalid Input: "))
				self.TRIES += 1
		return self.TRIES


	def Game(self):
		x = self.playGame()
		self.saveGame(self.FILENAME, x)
		total, times = self.loadHistory(self.FILENAME)
		print(f'The number was {self.TARGET}! It took you {x} tries!\n')
		print(f'In total you have {total} attempts over the course of {times} Games.\n')

	def RNG(self, MINIMUM, MAXIMUM):
		return self.random.randint(MINIMUM, MAXIMUM)


	def saveGame(self, filename, attempts):
		with open(filename, 'a') as f:
			f.writelines(str(attempts)+self.DELIM)
			f.close()

	def loadHistory(self, filename):
		array = []
		with open(filename, "r") as f:
			try:
				array = [int(x) for x in f]
			except:
				print("BREAK")
				pass
		f.close()
		
		total = sum(array)
		attempts = len(array)
		return total, attempts



