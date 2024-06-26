import string

# This function takes input from a user and checks to see if it 
# can be used as a password and how strong it is if so.
def password_Strength_Checker():
    password = input("Enter your password: \n"
                    "> ")

    # checks for upper, lower, special and digit characters
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    char = [ upper_case, lower_case, special, digits]
    length = len(password)

    score = 0

    # Checks input against commmon password list
    with open('pswd.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        print("Password found in common list. Score: 0/7\n"
              "-----------------------------------------------\n")
        check_another_password()

    # Awards points for password length
    if length >= 8:
        score += 1
    if length >= 10:
        score += 1
    if length >= 12:
        score += 1
    if length >= 14:
        score += 1

    print(f"Password length is {str(length)}, adding {str(score)} points!\n")

    # Displays password strength based upon score
    if sum(char) > 1:
        score += 1
    if sum(char) > 2:
        score += 1
    if sum(char) > 3:
        score += 1

    print(f"Password has {str(sum(char))} different characters, adding {str(sum(char) -1 )} points!\n")

    if score < 4:
        print(f"This password is weak! Score: {str(score)} / 7\n"
              "-----------------------------------------------\n")
        check_another_password()
    elif score == 4:
        print(f"This password is below average strength! Score: {str(score)} / 7\n"
              "-----------------------------------------------\n")
        check_another_password()
    elif 4 < score < 6:
        print (f"This password is average strength! Score: {str(score)} / 7\n"
               "-----------------------------------------------\n")
        check_another_password()
    elif score > 6:
        print (f"The password is strong! Score: {str(score)} / 7\n"
               "-----------------------------------------------\n")
        check_another_password()

# This function checks if the user wished to check another password or not
def check_another_password():
    checkAnother = input("Do you want to a different password?"
                         "> ")
    if checkAnother.lower() == "y" or checkAnother.lower() == "yes":
        password_Strength_Checker()
    elif checkAnother.lower() == "n" or checkAnother.lower() == "no":
        quit()

# Main function to start the program
def main():
    print("Welcome to the password checker!\n")
    userInput = input("Do you want to check if your password is valid?\n"
                      "> ")
    if userInput.lower() == "y" or userInput.lower() == "yes":
        password_Strength_Checker()
    elif userInput.lower() == "n" or userInput.lower() == "no":
        quit()
    
if __name__ == "__main__":
  main()