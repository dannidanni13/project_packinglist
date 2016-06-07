
# V3 - adds global variables such as temp and child age I could elminate some of the repetitive questions.
# V3 - added while loops to add and del functions
# V3 - added save list function
# V3 - valid lists to child age and temp questions

# #TO FIGURE OUT:
# # should I use dict instead of lists? or tuples since i don't want the age and vacation list edited?
# #age_list_1 and age_list_2 have similar items, is there a way to not duplicate items in list? 
# do i divide up the list in groups? such as: 
#(technology, entertainment, tolietries/bath, feeding, clothing/accesorries, diapering, baby gear, bedding, medicine)?? 
# could these be imported?
# all_ages_list --- INCLUDE THIS SOMEWHERE


child_name = "0"
temp = "" 
childage = ""
age_list_1 = ["formula", "bottles", "pacifiers"] #this is ages 0-6 months
age_list_2 = ["feeding utensils", "sippy-cup"] #this is ages 7-12 months
all_ages_list = ["stroller", "carseat", "first-aid kit"] #this items that kids of all ages need
vacationlist_warm = ["bathing suit/trunks", "sunscreen", "sunhat"] #warm weather
vacationlist_cold = ["warm jacket", "boots", "mittens", "rain jacket", "warm hat"] #cold weather
childlist = []  # this custom list for child

def child_age_question():	#stores this in global so I can access it later		
	valid_ages = [0,1, 2,3,4,5,6,7,8,9,10,11,12]
	global childage
	while (True):
		childage = int(raw_input ("How old is your child (in months)? "))
		if childage in valid_ages:
			return childage
			break
		else:
			print "Sorry, packing list only for children 0-12 months old. " 

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
			print "Sorry, only warm or cold weather selections available. "

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

