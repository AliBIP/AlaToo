import random
import os

leaderboard = []

field = [['.' for _ in range(7)] for _ in range(7)]
display_field = [['.' for _ in range(7)] for _ in range(7)]

player_name = input("Enter your name: ")

sizes = [3, 2, 2, 1, 1, 1, 1]

for size in sizes:
    while True:
        direction = random.choice(['H', 'V'])
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        if direction == 'H' and col + size <= 7:
            if all(field[row][col + i] == '.' for i in range(size)):
                for i in range(size):
                    field[row][col + i] = 'S'
                break
        elif direction == 'V' and row + size <= 7:
            if all(field[row + i][col] == '.' for i in range(size)):
                for i in range(size):
                    field[row + i][col] = 'S'
                break

shots = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(f"\n{player_name}'s current field:")
    for row in display_field:
        print(" ".join(row))

    print("\nEnter your shot (e.g., A 4) or type 'give up' to quit:")
    shot = input().split()

    if shot[0].lower() == "give" and shot[1].lower() == "up":
        print(f"\n{player_name} has given up!")
        leaderboard.append((player_name, shots))
        break  

    if len(shot) != 2 or not shot[0].isalpha() or not shot[1].isdigit():
        print("Invalid input. Please enter a letter and a number (e.g., A 4).")
        continue

    row = ord(shot[0].upper()) - ord('A')  
    col = int(shot[1]) - 1  

    if row < 0 or row >= 7 or col < 0 or col >= 7:
        print("Out of bounds! Try again.")
        continue

    if display_field[row][col] != '.':
        print("You already shot here! Try again.")
        continue

    if field[row][col] == 'S':
        print("You hit a ship!")
        display_field[row][col] = 'X'
        field[row][col] = '.'  
    else:
        print("You missed!")
        display_field[row][col] = 'O'

    shots += 1
    if all('S' not in row for row in field):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nCongratulations! You sank all the ships!")
        print(f"It took you {shots} shots.")
        print("\nFinal field:")
        for row in display_field:
            print(" ".join(row))
        break

    input("\nPress Enter to continue...") 


play_again = input("\nDo you want to play again? (y/n): ").lower()
if play_again == 'y':
    print("Thanks for playing!")
    print("\nLeaderboard:")

    for i in range(len(leaderboard)):
        for j in range(i + 1, len(leaderboard)):
            if leaderboard[i][1] > leaderboard[j][1]:  
                leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
    
    for player, score in leaderboard:
        print(f"{player}: {score} shots")
