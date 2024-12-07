from colorama import Fore, Style
import os
def FWEEP_title():
    print(Fore.GREEN + "+" * 149 + Style.RESET_ALL)
    print(Fore.BLUE + "Welcome to my FWEEP Calculator" + Style.RESET_ALL)
    print(Fore.GREEN + "+" * 149 + Style.RESET_ALL)

def main():
    FWEEP_title()
    print("\n\n")
    name = input("Hello there!! What should I call you? ")
    print(f"Good day {name}, welcome to " + Fore.BLUE + "THE FWEEP CALCULATOR" +Style.RESET_ALL)
    while True:
        try:
            answer = input("Would you like to continue?(Y/N): ").upper()
            if answer == "N":
                print(f"Thank you, Goodbye {name}")
                break
            elif answer != "Y":
                print("Please type Y if yes and N if no")
                continue

            print("1. Calculate Force\n2. Calculate Work\n3. Calculate Potential Energy\n4. Calculate Kinetic Energy\n5. Calculate Power")
            choice = int(input("Please select a number: "))
            if choice > 5 or choice < 1:
                os.system("cls")
                print("Please select only from the numbers given above!!")
                continue
            else:
                if choice == 1:
                    ifForce()
                elif choice == 2:
                    ifWork()
                elif choice == 3:
                    ifPE()
                elif choice == 4:
                    ifKE()
                elif choice == 5:
                    ifPower() 
            answer = input("Would you like to ask again?(Y or N): ").upper()
            
        except ValueError:
            os.system("cls")
            print("Input should be a numeric value.. Please try again")
            continue
def ifForce():
    print(Fore.CYAN  + "+"*149 + Style.RESET_ALL)
    mass = float(input("Enter mass(kg): "))
    acc = float(input("Enter acceleration: "))
    forceNum = mass*acc
    print(f"Force = {round(forceNum, 2)} N")
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)

def ifWork():
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)
    force = float(input("Enter Force(N): "))
    distance = float(input("Enter distance(m): "))
    workNum = force*distance
    print(f"Work = {round(workNum, 2)} J")
    print(f"In calories {workNum} J is {round(workNum * 0.238, 2)} calories.")
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)

def ifPE():
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)
    mass = float(input("Enter mass(kg): "))
    distance = float(input("Enter distance(m): "))
    PeNum = mass * distance * 9.81
    print(f"Potential Energy = {round(PeNum, 2)} J")
    print(f"In calories, {PeNum} J is {round(PeNum * 0.238, 2)} calories")
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)

def ifKE():
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)
    mass = float(input("Enter mass(kg): "))
    velocity = float(input("Enter velocity(m/s): "))
    mv = mass * (velocity**2)
    KeNum = mv/2
    print(f"Kinetic Energy = {round(KeNum, 2)} J")
    print(f"In calories, {KeNum} J is {round(KeNum * 0.238, 2)} calories")
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)

def ifPower():
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)
    energy = float(input("Enter Energy(J): "))
    time = float(input("Enter time(s): "))
    PowerNum = energy/time
    print(f"Power = {round(PowerNum, 2)} W")
    print(Fore.CYAN  + "+"* 149 + Style.RESET_ALL)

main()