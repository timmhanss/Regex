 # Regex inputs: First import re
 # . means any character except newline
 # * means 0 or more repetitions
 # + means 1 or more repetitions
 # ? means 0 or 1 repetitions
 # {m} means m amounts of repetitions
 # {m,n} means m-n amounts of repetitions
 # Exact match uses ^ to start a statement and $ to end the statement
 
import re

def main(): # Validates email and tells the username & domain based on the email given.
    email = input("What is your email? ").strip()
    if re.search(r"^.+@.+\..{2,3}$", email): # It has to have a username, a "@", a "." before the domain, and has to end with a 2-3 charlen TLD
        print("Valid email")
        username, domain = email.split("@")
        print(f"The username is {username} and uses {domain} as the domain.")
    else:
        print("Invalid email")
     
main()