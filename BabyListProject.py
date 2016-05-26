#ask for child's name 
#print "child's packing list" with child's name 

#TO FIGURE OUT:
# should I use dict instead of lists? or tuples since i don't want the age and vacation list edited?
#age_list_1 and age_list_2 have similar items, is there a way to not duplicate items in list? 

age_list_1 = []
#this is ages 0-6 months
age_list_2 = []
#this is ages 6-12 months
vacationlist_warm = ["bathing suit/trunks", "sunscreen", "sunhat"]
#warm weather
vacationlist_cold = ["warm jacket", "boots", "mittens", "rain jacket", "warm hat"]
#cold weather
childlist = []
#custom list for child


def name():
	child_name = raw_input("What is your child's name? ")
	return child_name


# menu function 
def menu ():
	print "0 - Look at prepared lists by age"
	print "1 - Look at prepared lists by vacation weather (hot or cold weather) "
	print "2 - Create a packing list for  " # add child's name here
	#when creating a new list for child - prompt for age of child list and vacation_type list
	print "3 - Add an item to your packing list "
	print "4 - Remove an item from your packing list "
	print "5 - Print child's packing list "
	print "6 - Exit program" # NEED TO figure out how to exit program in main function
	selection = raw_input = ("What would you like to do? ")
	return selection

def add_item():


def remove_item():

def sort_list():
	

# have a function to have list print alphabetically 

def main():

#include welcome/name of list in main
print "This is " ,name(),"'s packing list!"

#if 0, print age_list 1, -- raw_input for age, and print list age_list_1 or age_list_2, then return to menu

#if 1, print age_list 2 -- raw_input for weather type, print vacationlist_warm or vacationlist_cold, then return to menu

#if 2, create a new list childlist -- raw_input for age (return), raw_input for vacation weather (return), add list selections to childlist, then return to menu

#if 3 use add function append to childlist -- raw_input for item, if item not in childlist, append item to list, else "already in list"
# prompt to add more items or return to main menu

#if 4 remove function del from childlist -- raw_input for item, if item not in childlist, del item in list, else "not in list"
# prompt to remove more items or return to main menu

#if 5 print childlist -- alphabetically print childlist, then return to menu

#if 6 exit program --  TBD??? 
