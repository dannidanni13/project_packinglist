#CHANGES
#V4 - changed child_age_question to be Baby or Toddler
#V4 - dict with lists - added sleeping and changed Baby_Gear to Gear


child_name = " "
temp = " " 
childage = " "
childlist = {"Entertainment": [ ], "Toiletries" : [ ], "Gear" : [ ], "Feeding" : [ ], "Clothing" : [ ], "Sleeping" : [ ]}

childlist = []  # this custom list for child

def child_age_question():	#stores this in global so I can access it later		
	valid_ages = ["B", "T"]
	global childage
	while (True):
		childage = raw_input ("How old is your child? Enter B for under 12 months and T for 1 -3yrs old. ")
		childage = childage.upper()
		if childage in valid_ages:
			return childage
			break
		else:
			print "Sorry, that operation is not supported. Packing list for babies (0-12m) and toddlers (1-3yrs). " 

def temp_question():  #stores this in global variable temp
	valid_weathertemp = ["warm", "cold"]
	global temp
	while (True):
		temp = raw_input("Is the destination's weather warm or cold? ")
		temp = temp.lower()
		if temp in valid_weathertemp:
			return temp 
			break
		else:
			print "Sorry, only warm or cold weather selections available at this time. "

def name():
	global child_name
	child_name = raw_input("What is your child's name? ")
	child_name = child_name.upper()
	print "Let's get started on creating a packing list for", child_name + "!"

def include():
	include_lists = raw_input ("Would you like to include the prepared age lists items?  Y or N? ")
	include_lists = include_lists.lower()
	if include_lists == "y":
		if childage <=6:
			childlist.extend(age_list_1)
			print "Here is  " + child_name + "'s list: "
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
		elif childage >= 7 and childage <=12:
			childlist.extend(age_list_2)
			print "Here is  " + child_name + "'s list: "
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
	include_weatherlist = raw_input ("Would you like to include the prepared weather list items?  Y or N? ")
	include_weatherlist = include_weatherlist.lower()
	if include_weatherlist == "y":
		if temp == "warm":
			childlist.extend(vacationlist_warm)
			print "Here is  " + child_name + "'s list: "
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
		elif temp == "cold":
			childlist.extend(vacationlist_cold)
			print "Here is  " + child_name + "'s list: "
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
	else: 
		print childlist

def add_item(): # raw_input for item, if item not in childlist, append item to list, else "already in list"
	while (True):
		new_item = raw_input('What would you like to add to the packing list? Type menu to return to main menu. ')
		new_item = new_item.lower()
		if new_item == "menu":
			break
		elif new_item not in childlist:
			childlist.append(new_item)
		else:
			print "Item is already in packing list. "

def remove_item(): #remove item from childlist 
	while (True):
		del_item = raw_input ("What would you like to remove from packing list? Type menu to return to main menu. ")
		del_item = del_item.lower()
		if del_item == "menu":
			break
		elif del_item in childlist:
			childlist.remove(del_item)
		else:
			print "Item not in list. "

def sorted_list():
	childlist.sort()
	return childlist

def save_file():
	f = open('packinglist.txt', 'w') # CAN the txt file be the name of child?
	for item in childlist:
		f.write(item+'\n')
	f.close()
	print "Packing list saved!"

def menu ():
	print "1 - Look at prepared lists by age."
	print "2 - Look at prepared lists by vacation weather (warm or cold weather). "
	print "3 - Create a packing list for " + child_name + ". "
	print "4 - Add an item to " + child_name + "'s packing list. "
	print "5 - Remove an item from " +child_name + "'s packing list. "
	print "6 - Print " + child_name + "'s packing list. "
	print "7 - Save " + child_name + "'s packing list. "
	print "8 - Exit program" 
	user_selection = int(raw_input("What would you like to do? "))
	return user_selection

def main():
	print "Hello! Let's get ready for vacation by making a packing list for your little one! "
	child = name()	
	child_age = child_age_question()
	temperature = temp_question()

	while True:
		user_selection = menu() #moved user selections to in the while loop and changed ifs to elif 
		if user_selection == 1: # this looks at the list by age 
			if childage <=6:
				print age_list_1
			elif childage>= 7 and childage <=12:
				print age_list_2
			else:
				print "Sorry, packing list only for children 0-12 months old."
		elif user_selection == 2: # this looks at the weather lists
			if temp == "warm":
				print vacationlist_warm
			elif temp == "cold":
				print vacationlist_cold
		elif user_selection == 3: # creates a new packing list for child
			include()
		elif user_selection == 4: # calls add_item function to add single item to  childlist
			add_item()
			i=1
			for entry in childlist:
				print str(i) + ":", entry
				i += 1
		elif user_selection == 5: #call del_item function to delete item
			remove_item()
			i=1
			for entry in childlist:
				print str(i) + ":", entry
				i += 1
		elif user_selection == 6: #call sorted function to alphabetically print childlist
			sorted_list()
			i=1
			for entry in childlist:
				print str(i) + ":", entry
				i += 1
		elif user_selection == 7:
			save_file()
		elif user_selection == 8: 
			exit()	

if __name__ == '__main__':
	main()

