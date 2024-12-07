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

def countdown(t, stop_event):
    while t and not stop_event.is_set():
        print(f"\rTime remaining: {t} : ", end='', flush=True)
        time.sleep(1)
        t -= 1
    if t == 0:
        wrongAnswer.play()
        print(f"\n{RED}Time's Up{RESET}\n")

def input_with_timeout(prompt, timeout):
    print()  
    print(prompt, end=': ', flush=True)
    answer = [None]  
    stop_event = threading.Event()  

    def get_input():
        answer[0] = input()
        stop_event.set()  

    countdown_thread = threading.Thread(target=countdown, args=(timeout, stop_event))
    countdown_thread.start()

    thread = threading.Thread(target=get_input)
    thread.start()

    thread.join()  
    countdown_thread.join()  

    if answer[0] is None:
        return None  
    else:
        return answer[0]

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

def update_leaderboard(leaderboard, user_id, score):
    current_score = leaderboard.get(user_id, 0)
    if score > current_score and score <= 10:
        leaderboard[user_id] = score

def display_leaderboard(leaderboard, operation):
    print(f"\nLeaderboard for {operation}:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    if not sorted_leaderboard:
        print("No scores yet.")
    else:
        for user, score in sorted_leaderboard:
            print(f"{user}: {score}")

def generate_unique_pair(previous_pairs):
    while True:
        num1 = random.randint(2, 10)
        num2 = random.randint(1, num1 - 1)
        pair = (num1, num2)
        if pair not in previous_pairs and (num2, num1) not in previous_pairs:
            previous_pairs.append(pair)
            return num1, num2

def ifAddition(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} + {num2}")

    while True:
        sagot = input_with_timeout("What is your answer:\n ", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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

def ifSubtraction(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} - {num2}")

    while True:
        sagot = input_with_timeout("What is your answer\n", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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

def ifMultiplication(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} * {num2}")

    while True:
        sagot = input_with_timeout("What is your answer\n", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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

def ifDivision(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    nums2 = num2 * num1
    print(f"{count}. {nums2} / {num1}")

    while True:
        sagot = input_with_timeout("What is your answer\n", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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

def ifModulus(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} % {num2}")

    while True:
        sagot = input_with_timeout("What is your answer\n", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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

    while True:
        sagot = input_with_timeout("What is your answer\n", 5)
        if sagot is None:
            wrongAnswer.play()
            print(f"{RED}Oops, time's up!{RESET}\n")
            return score  

        try:
            sagot = int(sagot)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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
        if answer == "No":
            print(f"Thank you, Goodbye {prompt}.")
            for choice in choices:
                save_leaderboard(choice, leaderboard[choice])
            break
        elif answer != "Yes":
            print("Please answer with 'Yes' or 'No'.")
            continue
        elif answer == "Yes":
            continue

main()