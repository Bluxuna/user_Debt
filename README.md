# user_Debt

This Python code uses Flask, a micro web framework, to create a web application that interacts with a SQLite database. The application has the following functionalities:

A user can join the database by providing their name, surname, phone number, debt, and currency. This information is added to the USERS table in the database.
A user can search for other users by name, and the application returns the name, debt, and currency of the user they searched for.
The application can read the search results aloud using the text_to_speech() function from the vc module.
All users in the database can be displayed on a page using the /participants route.
Users can be deleted from the database using the /delete/<name> route.
The application listens on the local machine's IP address and port 5000, and it runs in debug mode.

# Dependencies
Flask
sqlite3
vc
requests
pyttsx3

# Usage
Clone the repository and navigate to the directory.
Install the dependencies by running pip install -r requirements.txt.
Run the app by executing python app.py.
Navigate to http://localhost:5000/ in a web browser to interact with the application.
