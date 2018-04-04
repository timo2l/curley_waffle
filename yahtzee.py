import random
import os

#result = []
roll_score = []

roll_Choice = {'three of a kind': {
					'CHOICE: ': 1,
					'score: ': 0 ,
					'received': False
					}, 
			'four of a kind' :{
					'CHOICE: ': 2,
					'score: ' : 0,
					'received': False
					},
			'YAHTZEE!' :{
					'CHOICE: ': 3,
					'score: ' : 0,
					'received': False
					}
			}

def roll(n):
	result = []
	for x in range(n):
		result.append(int(random.randrange(1,6)))
	return result
	

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

roll_score = [] 

def display_choice(roll_score):
	os.system("cls")

	while len(roll_score) < 3:
		
		print ("____________________________________")
		def display_options(roll_score):
			print (str(len(roll_score)))
			#displays options for the user to choose
			for choices, roll_Choice_dict in roll_Choice.items():
				if roll_Choice_dict['received'] == False:
					print ("\nChoices: " + choices + " CHOOSE: " + str(roll_Choice_dict['CHOICE: ']))

			#Lets the user choose what that want to use for the hand
			print ("____________________________________")
		display_options(roll_score)
		user_choice = input("WHAT DO YOU WANT TO CHOOSE? ")
		
		roll_score_start = len(roll_score)
		while len(roll_score) == roll_score_start:
			for choices, roll_Choice_dict in roll_Choice.items():
				if str(roll_Choice_dict['CHOICE: ']) == int(user_choice): # and roll_Choice_dict['received'] == False:
					roll_score.append([roll_Choice_dict['score: ']])
					roll_Choice_dict['received'] = True
				else:
					display_options(roll_score)
					user_choice = input("CHOOSE AGAIN: ")



print ("__________________")
roll_list = roll(5)


for r in roll_list:

	print(str(r), end=' ')

print ("\n")
# dup_list = (list_duplicates(roll_list))
# dup_set = set()
# if dup_list:
	# for l in dup_list:
		# print(str(l), end=' - ')
		# print (roll_list.count(int(l)))
		# dup_set.add(l)
# else:
	# print ("NO DUPS")
	# dup_rolls = dup_rolls + 1
# if len(dup_set)	>= 1:
	# print (dup_set)
countr = 0
while countr != 3:
	countr = countr + 1
	remove_Die = input("\n" + "WHICH DO YOU WANT TO REMOVE? (TYPE NONE OR VALUES OF DIE) ")

	if remove_Die.upper() not in ("NONE"):
		remove_Die = [i for i in remove_Die]
		for i in remove_Die:
			try:
				roll_list.remove(int(i))
				roll_list.append(int(random.randrange(1,6)))
				#roll_list.append(str(roll(1)))
			except ValueError:
				print (str(i) + " is not in the list")
			
		for r in roll_list:
			print(str(r), end=' ')
	else:
		break
		

display_choice(roll_score)
	
