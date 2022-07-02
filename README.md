# Login_Test_Cases
Evaluation test for SQAE from 10 pearls

# Installation
Install the following tools
- Python3.8
- Python IDE (Pycharm)
- Python Pytest

# Adding Dependencies
Use the requirements.txt file to install all the dependencies required for this project using the following command.
cat requirements.txt | xargs -n 1 pip install

I have covered Basic test flows of Login page which includes
1. Valid username and Valid Password
2. InValid username and Valid Password
3. Valid username and InValid Password
4. InValid username and InValid Password

Created 3 separate repositories for Objects, Functions and Driver
Create class for LoginPage where i stored all the Locators for objects and their Functions in Pages repo
Created class login to write test cases to verify our scenarios by passing different values our functions in LoginPage class
