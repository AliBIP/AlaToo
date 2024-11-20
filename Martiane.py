import random

def random_boxes():
    return [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

print("Help the Martians find their cargo")
box_locations = random_boxes()
total_weight = 713  
print(f"The total weight of the boxes is {total_weight} kg.")

attempts = 0

while True:
    attempts += 1
    print("\nGuess the 3 locations of the boxes (1-10):")
    
    try:
        guess1 = int(input("Enter location 1: "))
        guess2 = int(input("Enter location 2: "))
        guess3 = int(input("Enter location 3: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    guesses = [guess1, guess2, guess3]

    if guesses[0] == box_locations[0] and guesses[1] == box_locations[1] and guesses[2] == box_locations[2]:
        print("\nYou found all the boxes!")
        print(f"Success! Total weight is {total_weight} kg. Attempts: {attempts}")
        print(f"Final locations of the boxes: {box_locations}")
        break
    else:
        print("Wrong locations! The boxes moved!")
        print(f"Previous guess: {guesses}, Correct locations were: {box_locations}")
        box_locations = random_boxes()  

#vncx,vnx,zcvn,xcv
    
    