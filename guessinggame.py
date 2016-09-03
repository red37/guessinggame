import random, sys
count=0
print("Guess the number that i am thinking. Its between 1 and 20. you have six chances")
think= random.randint(1,20)

for i in range(1,7):

	guess = int(input())
	try:
		if guess == think:
			print(" You pyschic you")
			sys.exit()
		elif guess > think:
			print("too high")
		elif guess < think:
			print("too low")

	except ValueError:
		print('you did not enter a valid number')


print("the number was "+ str(think))