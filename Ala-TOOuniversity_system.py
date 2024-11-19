
import os


First_Name = str(input("Enter your first name: "))
Last_Name = str(input("Enter your last name: "))

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    School_education_certificate = int(input("""Do you have an education certificate?(Please enter 1 for Yes or 2 for No. PROGRAM DON'T WORK IF YOU SELECT ANOTHER CHOOSE) 
    Yes -- 1
    No -- 2
    Choose:"""))
    if School_education_certificate == 1 or School_education_certificate == 2:
        break
    else:
        print("Invalid input. Please enter 1 for Yes or 2 for No.")

os.system('cls' if os.name == 'nt' else 'clear')

ORT_score = int(input("Enter your ORT score: "))

os.system('cls' if os.name == 'nt' else 'clear')


while True:
    E_l_p_level = int(input("""Enter your English language proficiency level( Please enter a number between 1 and 6. PROGRAM DON'T WORK IF YOU SELECT ANOTHER CHOOSE):
   Beginner - 1 
   Elementary - 2
   Pre-Intermediate - 3 
   Intermediate - 4 
   Upper-Intermediate - 5
   Advanced - 6
   Choose:"""))
    if 1 <= E_l_p_level <= 6:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 6.")

os.system('cls' if os.name == 'nt' else 'clear')

if School_education_certificate == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {First_Name} {Last_Name}, you cannot be admitted because you don't have a school education certificate.")
elif ORT_score < 110:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {First_Name} {Last_Name}, you cannot be admitted because your ORT score is below 110.")
elif E_l_p_level == 1 or E_l_p_level == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{First_Name} {Last_Name}, your English level is too low for direct admission. "
          "You are recommended to take a one-year preparatory course (Foundation Course AIU).")
else:
    print(f" {First_Name} {Last_Name}, congratulations! You are eligible for admission to Ala-Too University.")
    print("Select your desired specialty:")
    print("1 - Computer Engineering 2500$")
    print("2 - Artificial Intelligence 2200$")
    print("3 - Psychology 1900$")
    print("4 - Journalism 1700$")
    print("5 - International Relations 2200$")
    print("6 - Law 1800$")
    print("7 - Management 2200$")
    print("8 - Medicine 3300$")
    specialty_choice = 0
    selected_specialty = ""
    base_cost = 0

    while specialty_choice < 1 or specialty_choice > 8:
        try:
            specialty_choice = int(input("Enter the number corresponding to your choice: "))
            if specialty_choice == 1:
                selected_specialty = "Computer Engineering"
                base_cost = 2500
            elif specialty_choice == 2:
                selected_specialty = "Artificial Intelligence"
                base_cost = 2200
            elif specialty_choice == 3:
                selected_specialty = "Psychology"
                base_cost = 1900
            elif specialty_choice == 4:
                selected_specialty = "Journalism"
                base_cost = 1700
            elif specialty_choice == 5:
                selected_specialty = "International Relations"
                base_cost = 2200
            elif specialty_choice == 6:
                selected_specialty = "Law"
                base_cost = 1800
            elif specialty_choice == 7:
                selected_specialty = "Management"
                base_cost = 2200
            elif specialty_choice == 8:
                selected_specialty = "Medicine"
                base_cost = 3300
            else:
                print(" don't correct ")
        except ValueError:
            print(" don't correct ")

    free_procent = 0
    if 140 <= ORT_score <= 155:
        free_procent = 5
    elif 156 <= ORT_score <= 174:
        free_procent = 10
    elif 175 <= ORT_score <= 199:
        free_procent = 25
    elif 200 <= ORT_score <= 209:
        free_procent= 50
    elif 210 <= ORT_score <= 218:
        free_procent = 75
    elif 219 <= ORT_score <= 240:
        free_procent = 100
    final_cost = base_cost * (1 - free_procent / 100)

    if free_procent > 0:
        print(f" {First_Name} {Last_Name}, we congratulate you! You have been admitted to the {selected_specialty} "
              f"program at Ala-Too International University. The cost of your tuition with a {free_procent}% discount will "
              f"be {int(final_cost)}$ per year.")
    else:
        print(f" {First_Name} {Last_Name}, we congratulate you! You have been admitted to the {selected_specialty} "
              f"program at Ala-Too International University. The cost of your tuition will be {base_cost}$ per year.")
# I have already done this projcet so it is only for commit
# I see you 