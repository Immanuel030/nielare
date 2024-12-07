import random
import pygame
import csv
import os
import threading
import time

pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Immanuel\\Arithmetic\\bg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)
wrongAnswer = pygame.mixer.Sound("C:\\Users\\Immanuel\\Arithmetic\\wrong.mp3")
correctAnswer = pygame.mixer.Sound("C:\\Users\\Immanuel\\Arithmetic\\correct.mp3")

GREEN = "\033[92m"  
RED = "\033[91m"    
RESET = "\033[0m"

# Load leaderboard from CSV
def load_leaderboard(operation):
    leaderboard = {}
    filename = f"{operation.lower()}_leaderboard.csv"
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                user_id, score = row
                leaderboard[user_id] = int(score)
    return leaderboard

# Save leaderboard to CSV
def save_leaderboard(operation, leaderboard):
    filename = f"{operation.lower()}_leaderboard.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user_id, score in leaderboard.items():
                writer.writerow([user_id, score])
        print(f"Leaderboard for {operation} saved successfully.")
    except Exception as e:
        print(f"Error saving leaderboard for {operation}: {e}")

# Update leaderboard in memory
def update_leaderboard(leaderboard, user_id, score):
    current_score = leaderboard.get(user_id, 0)
    if score > current_score and score <= 10:
        leaderboard[user_id] = score

# Display leaderboard
def display_leaderboard(leaderboard, operation):
    print(f"\nLeaderboard for {operation}:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    if not sorted_leaderboard:
        print("No scores yet.")
    else:
        for user, score in sorted_leaderboard:
            print(f"{user}: {score}")

# Generate a unique pair of numbers for the quiz
def generate_unique_pair(previous_pairs):
    while True:
        num1 = random.randint(2, 10)
        num2 = random.randint(1, num1 - 1)
        pair = (num1, num2)
        if pair not in previous_pairs and (num2, num1) not in previous_pairs:
            previous_pairs.append(pair)
            return num1, num2

# Countdown function
def countdown(t):
    while t:
        print(f"\rTime remaining: {t} seconds", end='', flush=True)
        time.sleep(1)
        t -= 1
    print("\nTime's up!")

# Function to get user input with a timeout
def input_with_timeout(prompt, timeout):
    print(prompt, end=': ', flush=True)
    answer = [None]  # Use a list to allow modification in the inner function

    def get_input():
        answer[0] = input()

    # Start a thread for the input
    thread = threading.Thread(target=get_input)
    thread.start()

    # Start the countdown
    countdown_thread = threading.Thread(target=countdown, args=(timeout,))
    countdown_thread.start()

    thread.join()  # Wait for the input thread to finish countdown_thread.join()  # Wait for the countdown thread to finish

    if answer[0] is None:
        return None  # Return None if no input was given
    else:
        return answer[0]

# Function for addition
def ifAddition(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} + {num2}")
    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    answerNum = num1 + num2
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

# Function for subtraction
def ifSubtraction(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} - {num2}")
    
    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    answerNum = num1 - num2
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

# Function for multiplication
def ifMultiplication(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} * {num2}")
    
    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    answerNum = num1 * num2
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

# Function for division
def ifDivision(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    nums2 = num2 * num1
    print(f"{count}. {nums2} / {num1}")
    
    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    answerNum = nums2 / num1
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

# Function for modulus
def ifModulus(count, score, previous_pairs, user_id, leaderboard):
    num1, num2= generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} % {num2}")
    
    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    answerNum = num1 % num2
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

# Function for mixed operations
def ifMixed(count, score, previous_pairs, user_id, leaderboard):
    operation = random.choice(["Addition", "Subtraction", "Multiplication", "Division", "Modulus"])
    num1, num2 = generate_unique_pair(previous_pairs)

    if operation == "Addition":
        answerNum = num1 + num2
        print(f"{count}. {num1} + {num2}")
    elif operation == "Subtraction":
        answerNum = num1 - num2
        print(f"{count}. {num1} - {num2}")
    elif operation == "Multiplication":
        answerNum = num1 * num2
        print(f"{count}. {num1} * {num2}")
    elif operation == "Division":
        nums2 = num2 * num1  
        answerNum = nums2 / num1
        print(f"{count}. {nums2} / {num1}")
    elif operation == "Modulus":
        answerNum = num1 % num2
        print(f"{count}. {num1} % {num2}")

    sagot = input_with_timeout("What is your answer", 5)
    if sagot is None:
        wrongAnswer.play()
        print(f"{RED}Oops, time's up!{RESET}\n")
        return score  # No score increment for timeout

    try:
        sagot = int(sagot)
    except ValueError:
        wrongAnswer.play()
        print("Invalid input. Please enter a valid number.")
        return score

    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)
        return score

def main():
    choices = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Mixed"]
    prompt = input("Hello there, what should I call you? ")
    print(f"Hello there {prompt}, welcome to the arithmetic game!!!")
    
    previous_pairs = []  
    leaderboard = {choice: load_leaderboard(choice) for choice in choices}

    while True:
        answer = input(" Would you like to continue? (Yes/No) ").capitalize()
        if answer == "No":
            print(f"Thank you, Goodbye {prompt}.")
            for choice in choices:
                save_leaderboard(choice, leaderboard[choice])
            break
        elif answer != "Yes":
            print("Please answer with 'Yes' or 'No'.")
            continue
        
        print("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] Modulus\n[6] Mixed")
        
        try:
            choice = int(input("Please select what you want to try: "))
            if choice not in range(1, 7):
                print("I said 1-6 only, please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        count = 0
        guess = 10
        score = 0
        
        while guess != 0:
            count += 1
            if choice == 1:
                score = ifAddition(count, score, previous_pairs, prompt, leaderboard["Addition"])
            elif choice == 2:
                score = ifSubtraction(count, score, previous_pairs, prompt, leaderboard["Subtraction"])
            elif choice == 3:
                score = ifMultiplication(count, score, previous_pairs, prompt, leaderboard["Multiplication"])
            elif choice == 4:
                score = ifDivision(count, score, previous_pairs, prompt, leaderboard["Division"])
            elif choice == 5:
                score = ifModulus(count, score, previous_pairs, prompt, leaderboard["Modulus"])
            elif choice == 6:
                score = ifMixed(count, score, previous_pairs, prompt, leaderboard["Mixed"])
            guess -= 1
        
        print(f"Congratulations!!, your score is {score}/10, Good job!!")
 
        display_leaderboard(leaderboard[choices[choice - 1]], choices[choice - 1])  
        
        answer = input("Do you want to try it again? (Yes/No) ").capitalize()

main() 