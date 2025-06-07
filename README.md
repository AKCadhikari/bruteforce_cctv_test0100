# bruteforce_cctv_test0100 

#Step 1: Get the CCTV IP/login URL#
You need the IP address of your CCTV or local test web login URL.

Example: http://192.168.1.100/login or http://localhost/login

#Step 2: Check how the login works#
Open the login page in your browser.
Use browser DevTools (Right-click → Inspect → Network tab).
Try logging in with any password.
See what HTTP request is sent (usually POST request with username & password fields).

Note:
The URL of the POST request
The field names for username and password (e.g., username, password or user, pass)

#Step 3: Interpret output#
The script prints tried passwords.

When password is found, it prints [+] Password found: ...

Important notes:
You must change URL and form field names according to your CCTV login page.
Sometimes, login uses JavaScript or tokens — script may need to be adapted.
Use only on devices/networks you own or have permission for!


