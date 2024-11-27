import random
import os

leaderboard = []

field = [['.' for _ in range(7)] for _ in range(7)]
display_field = [['.' for _ in range(7)] for _ in range(7)]

player_name = input("Enter your name: ")

sizes = [3, 2, 2, 1, 1, 1, 1]

def can_place_ship(row, col, size, direction, field):
    if direction == 'H':
        if col + size > 7:
            return False
        for i in range(size):
            if field[row][col + i] != '.':
                return False
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + i + dc
                    if 0 <= nr < 7 and 0 <= nc < 7 and field[nr][nc] == 'S':
                        return False
    elif direction == 'V':
        if row + size > 7:
            return False
        for i in range(size):
            if field[row + i][col] != '.':
                return False
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + i + dr, col + dc
                    if 0 <= nr < 7 and 0 <= nc < 7 and field[nr][nc] == 'S':
                        return False
    return True

def is_ship_sunk(row, col, field, display_field):
    ship_cells = [(row, col)]
    visited = set()

    while ship_cells:
        r, c = ship_cells.pop()
        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 7 and 0 <= nc < 7 and (nr, nc) not in visited:
                if field[nr][nc] == 'S':
                    return False  
                if display_field[nr][nc] == 'X':
                    ship_cells.append((nr, nc))
    for r, c in visited:
        display_field[r][c] = 'S'
    return True


for size in sizes:
    while True:
        direction = random.choice(['H', 'V'])
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        if can_place_ship(row, col, size, direction, field):
            if direction == 'H':
                for i in range(size):
                    field[row][col + i] = 'S'
            elif direction == 'V':
                for i in range(size):
                    field[row + i][col] = 'S'
            break

shots = 0
misses = 0  
max_misses = 5  

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(f"\n{player_name}'s current field:")
    for row in display_field:
        print(" ".join(row))

    print("\nEnter your shot (e.g., A 4) or type 'give up' to quit:")
    shot = input().split()

    if len(shot) == 2 and shot[0].lower() == "give" and shot[1].lower() == "up":
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
        if is_ship_sunk(row, col, field, display_field):
            print("You sank a ship!")
    else:
        print("You missed!")
        display_field[row][col] = 'O'
        misses += 1 

    shots += 1

    if misses >= max_misses:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nYou lost! You missed too many times.")
        print(f"It took you {shots} shots.")
        print("\nFinal field:")
        for row in display_field:
            print(" ".join(row))
        break

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
