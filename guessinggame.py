import random, sys
count=0
print("Guess the number that i am thinking. Its between 1 and 20. you have six chances")
think= random.randint(1,20)

for i in range(1,7):
	
	try:
		guess = int(input())	
	except ValueError:
		print('you did not enter a valid number, try again')
		continue
	
	if guess == think:
		print(" You pyschic you")
		sys.exit()
	elif guess > think:
		print("too high")
	elif guess < think:
		print("too low")

	


print("the number was "+ str(think))