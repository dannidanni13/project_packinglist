#option 4 is not working after creating a packing list - works before i create it but not after
#DIDN't work: wanted to put all the i=1 / for entry in childlist: / print str(i) + ":", entry/ i += 1 in sorted instead of in the main function
# what if a letter is entered not a number?  - ValueError: invalid literal for int() with base 10: 'd'

child_name = " "
temp = " " 
childage = " "
childlist = [ ]
baby_list = ["Bottles", "Bibs", "Formula", "Burp cloths", "Bottle brush", "Pack n play" ,"Baby monitor", "Sound machine", "Pack n play sheet", "Blanket(s)", "Pajamas", "Onesies/shirts", "Pants", "Outfits for daily outings", "Shoes","Socks", "Soap/shampoo", "Lotion", "Towels", "Rince cup", "Comb/brush", "Nail clipper" , "Sunblock", "Tylenol" , "Diapers", "Wipes", "Diaper rash cream", "Nose aspirator", "First-aid kit", "Favorite toy(s)", "Stuffed animals", "Stroller", "Car Seat", "Pacifiers", "Travel changing pad", "Diaper bag", "Baby carrier", "Boppy pillow", "Bath tub"]
toddler_list = ["Bibs", "Pouches", "Sippy cup", "Favorite snack(s)", "Utensils", "Bowls/plates", "Pack n play" ,"Baby monitor", "Sound machine", "Pack n play sheet", "Blanket(s)", "Pajamas", "Onesies/shirts", "Pants", "Outfits for daily outings", "Shoes","Socks", "Underwear", "Soap/shampoo", "Lotion", "Towels", "Rince cup", "Comb/brush", "Nail clipper" , "Sunblock", "Tylenol" , "Diapers", "Wipes", "Diaper rash cream", "Toothbrush", "Toothpaste", "First-aid kit", "Favorite toy(s)", "Stuffed animals", "Coloring books/crayons", "Favorite book(s)", "iPad or DVD", "Stroller", "Car seat", "Traveling changing pad", "Traveling high-chair", "Diaper Bag"]


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
	valid_weathertemp = ["w", "c"]
	global temp
	while (True):
		temp = raw_input("Is the destination's weather warm or cold? Enter W for warm and C for cold. ")
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

def read_file(filename):
	f = open(filename, 'r')
	new_list = f.readlines()
	new_list =[item.rstrip('\n"') for item in new_list] 
	return new_list
	f.close	
		
def save_file():
	f = open('packinglist.txt', 'w') 
	for item in childlist:
		f.write(item+'\n')
	f.close()
	print "Packing list saved!"

def sorted_list():
	childlist.sort()
	return childlist

def include():
	warm_list = read_file("Clothing_warm_both.txt")
	cold_list = read_file("Clothing_cold_both.txt")
	if childage == "B":
		childlist.extend(baby_list)
		if temp == "w":
			childlist.extend(warm_list)
		else: 
			childlist.extend(cold_list)
		sorted_list()
		print "Here is  " + child_name + "'s list: "
		i = 1
		for entry in childlist:
			print str(i) + ":", entry
			i+=1
	elif childage == "T":
		childlist.extend(toddler_list)
		if temp == "w":
			childlist.extend(warm_list)
		else:
			childlist.extend(cold_list)
		sorted_list()
		print "Here is  " + child_name + "'s list: "
		i = 1
		for entry in childlist:
			print str(i) + ":", entry
			i+=1
	else: 
		print childlist

def add_item(): # raw_input for item, if item not in childlist, append item to list, else "already in list"
	while (True):
		new_item = raw_input('What would you like to add to the packing list? Type Menu to return to main menu. ')
		new_item = new_item.capitalize()
		if new_item == "Menu":
			break
		elif new_item not in childlist:
			childlist.append(new_item)
			print "Item added!"
		else:
			print "Item is already in packing list. "

def remove_item(): #remove item from childlist 
	while (True):
		del_item = raw_input ("What would you like to remove from packing list? Type Menu to return to main menu. ")
		del_item = del_item.capitalize()
		if del_item == "Menu":
			break
		elif del_item in childlist:
			childlist.remove(del_item)
			print "Item removed. "
		else:
			print "Item not in list. "

def save_file():
	f = open('packinglist.txt', 'w') # CAN the txt file be the name of child?
	for item in childlist:
		f.write(item+'\n')
	f.close()
	print "Packing list saved!"

def menu ():
	valid_inputs = [1,2,3,4,5,6]
	while (True):
		print "1 - Create a packing list for " + child_name + ". "
		print "2 - Add an item to " + child_name + "'s packing list. "
		print "3 - Remove an item from " +child_name + "'s packing list. "
		print "4 - Print " + child_name + "'s packing list. "
		print "5 - Save " + child_name + "'s packing list. "
		print "6 - Exit program" 
		user_selection = int(raw_input("What would you like to do? Please enter a number from the menu. "))
		if user_selection in valid_inputs:
			return user_selection
		elif user_selection != valid_inputs:
			print "Enter try entering a number 1 - 6"

def main():
	print "Hello! Let's get ready for vacation by making a packing list for your little one! "
	child = name()	
	child_age = child_age_question()
	temperature = temp_question()

	while True:
		user_selection = menu() 	
		if user_selection == 1 and len(childlist) == 0: 
			include()
		elif user_selection == 2: 
			add_item()
			i=1
			for entry in childlist:
				print str(i) + ":", entry
				i += 1
		elif user_selection == 3:
			remove_item()
			i=1
			for entry in childlist:
				print str(i) + ":", entry
				i += 1
		elif user_selection == 4: 
			sorted_list()
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
		elif user_selection == 5:
			save_file()
		elif user_selection == 6: 
			exit()	
		else:
			print "Packing list already created. "

if __name__ == '__main__':
	main()

