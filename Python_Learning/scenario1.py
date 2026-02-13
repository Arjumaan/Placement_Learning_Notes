''' 
An online shopping platform displays a personalized greeting message when a customer logs into the website.
A function is defined using the def keyword to generate the welcome message dynamically based on the username entered during login
'''

def welcome_message(username):
    return f"Welcome, {username}!"

username = input("Login username: ")
print(welcome_message(username))