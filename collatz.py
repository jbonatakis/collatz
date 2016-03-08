while True:
	try:
		print("Please enter an integer below.")
		number = input(">> ")
		number = int(number)
		break
	except ValueError:
		print(number, " is not an integer. Try again.")

def collatz(number):
	while number != 1:
		if number % 2 == 0:
			number = number / 2
			print(number)
		elif number % 2 == 1:
			number = (number * 3) + 1
			print(number)

collatz(number)

print("You got it!")
