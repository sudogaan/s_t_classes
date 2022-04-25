class User:
	pass

user1 = User() # user1 is an instance or an object of the user class

user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name)
print(user1.last_name)

first_name = "Arhtur"
last_name = "Clarke"

print(first_name, last_name)

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"


print(user2.first_name, user2.last_name)

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

import datetime
class User:
	"""A member of Friendface. For now we are only storing their name and birthday"""
	def __init__(self, full_name, birthday): #is used every time a new class is made
		self.name = full_name #providing value to the user object, full_name is the value and name is the field that stores the value
		self.birthday = birthday #yyyymmdd

		# extract first and last names
		name_pieces = full_name.split(" ")
		self.first_name = name_pieces[0]
		self.last_name = name_pieces[-1] 

	def age(self):
		"""Return the age of the user in years"""
		today = datetime.date(2001, 5, 12)
		yyyy = int(self.birthday[0:4])
		mm = int(self.birthday[4:6])
		dd = int(self.birthday[6:8])
		dob = datetime.date(yyy, mmi dd) #date of birth
		age_in_days = (today - dob).days
		age_in_years = age_in_days / 365
		return int(age_in_years)

user = User("Dave Bowman", 19712009):
print(user.name, user.first_name, user.last_name, user.birthday)
print(user.age())



