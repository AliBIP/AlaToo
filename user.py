user_info = {}
name = input("What is the user's name? ")  
age = int(input("What is the user's age? ")) 
country_of_birth = input("What is the user's country of birth? ") 
known_for = input("What is the user known for? ")  

user_info["name"] = name
user_info["age"] = age
user_info["country_of_birth"] = country_of_birth
user_info["known_for"] = known_for

print(f"Name: {user_info['name']}")
print(f"Age: {user_info['age']}")
print(f"Country of Birth: {user_info['country_of_birth']}")
print(f"Known For: {user_info['known_for']}")
