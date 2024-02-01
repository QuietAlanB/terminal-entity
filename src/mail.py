class Mail:
	def __init__(self, author, title, body):
		self.author = author
		self.title = title
		self.body = body

	def Print(self):
		print("-----------------------------------")
		print(f"'{self.title}'")
		print(f"   From {self.author}")
		print("")
		print(f"{self.body}")
		print(f"-----------------------------------")
