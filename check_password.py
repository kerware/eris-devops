# Script Name   : Password Strength Checker
# Author        : Olivier CHARLES
# Created       : 06/11/2025
# Version       : 1.0
# Description   : Check if password is too worst

user_password = input("Enter the password to check \n")

def worst_500_passwords( password):
    # Download SecList
    import requests
    print('Beginning check in 500 passwords')
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/500-worst-passwords.txt"
    response = requests.get(url)
    content = response.content

    if str(password) in str(content):
        print("The password is too worst, change it immediatly\n")
        exit(0)

def worst_10k_passwords( password):
    # Download SecList
    import requests
    print('Beginning check in 10k passwords')
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-worst-passwords.txt"
    response = requests.get(url)
    content = response.content

    if str(password) in str(content):
        print("The password is too worst, change it immediatly\n")
        exit(0)

if __name__ == "__main__":
    worst_500_passwords(user_password)
    worst_10k_passwords(user_password)
    print("The password is not in the worst 10k passwords list\n")
    
