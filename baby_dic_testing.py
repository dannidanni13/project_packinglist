
childlist = {"Entertainment": " ", "Tolietries" : " ", "Baby_Gear" : " ", "Feeding" : "", "Clothing" : " "}

def read_file(filename):
	f = open(filename, 'r')
	new_list = f.readlines()
	new_list =[item.rstrip('\n"') for item in new_list] 
	return new_list
	# print: ['Stroller', 'Car Seat']
	f.close
	

def include():
	include_lists = raw_input ("Would you like to include prepared lists items?  Y or N? ")
	include_lists = include_lists.lower()
	if include_lists == "y":
		which_list = raw_input ("Which list would you like to include? 1 for Entertainment, 2 for Tolietries, 3 for Feeding,  4 for Baby Gear ")
		if which_list ==4:
			read_file("Baby_Gear.txt")
			childlist["Baby_Gear"].append(new_list)
			print childlist # nothing prints
			i = 1
			for entry in childlist:
				print str(i) + ":", entry
				i+=1
		# elif childage >= 7 and childage <=12:
		# 	childlist.extend(age_list_2)
		# 	print "Here is  " + child_name + "'s list: "
		# 	i = 1
		# 	for entry in childlist:
		# 		print str(i) + ":", entry
		# 		i+=1
include()



#create different CSV or text files for each Keys

# the values of each key will be a list 

# create a function that reads the file 
	#opens
	#reads
	#parse - splits on ","
	#return a list

# def read_file():
# 	f = open("Tolietries.txt", 'r')
# 	new_list = f.readlines()
# 	new_list =[item.rstrip('\n"') for item in new_list] 
# 	print new_list
# 	f.close
