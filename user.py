user_info = {}
name = input(" name: ") 
age = int(input(" age: "))  
email = input("email: ") 

user_info["name"] = name
user_info["age"] = age
user_info["email"] = email


print(f"Name: {user_info['name']}")
print(f"Age: {user_info['age']}")
print(f"Email: {user_info['email']}")
