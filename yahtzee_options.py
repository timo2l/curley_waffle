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
			
roll_score = []
while len(roll_score) < 3:
	
	print ("____________________________________")
	def display_options():
		print (str(len(roll_score)))
		#displays options for the user to choose
		for choices, roll_Choice_dict in roll_Choice.items():
			if roll_Choice_dict['received'] == False:
				print ("\nChoices: " + choices + " CHOOSE: " + str(roll_Choice_dict['CHOICE: ']))

		#Lets the user choose what that want to use for the hand
		print ("____________________________________")
	display_options()
	user_choice = input("WHAT DO YOU WANT TO CHOOSE? ")
	
	roll_score_start = len(roll_score)
	while len(roll_score) == roll_score_start:
		for choices, roll_Choice_dict in roll_Choice.items():
			if str(roll_Choice_dict['CHOICE: ']) == int(user_choice): # and roll_Choice_dict['received'] == False:
				roll_score.append([roll_Choice_dict['score: ']])
				roll_Choice_dict['received'] = True
			else:
				display_options()
				user_choice = input("CHOOSE AGAIN: ")
				
	#for choices, roll_Choice_dict in roll_Choice.items():
	#	if roll_Choice_dict['received'] == False:
	#		print ("\nChoices: " + choices + " CHOOSE: " + str(roll_Choice_dict['CHOICE: ']))