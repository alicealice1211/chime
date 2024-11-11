Chime Automation Script
Description:
This script automates the process of logging into a Chime bank account and scraping the balance information using the Selenium WebDriver. 
It handles steps such as entering credentials, dealing with two-factor authentication, and navigating through the user interface to retrieve the balance from a checking account.

Requirements:
Python 3.x
Selenium WebDriver
ChromeDriver compatible with the installed Chrome version

Setup:
Python Installation: Ensure Python 3.x is installed on your system.
ChromeDriver: Download and install ChromeDriver from ChromeDriver - WebDriver for Chrome. Ensure it’s in your PATH or specify the path in the script.


Run: 
Open your terminal or command prompt.
Navigate to the directory containing the script.
python chime2.py

You will be prompted to enter the verification code manually during the execution if two-factor authentication is enabled.


Functions: 
setup(): Initializes the WebDriver and navigates to the Chime login page.
login(): Enters the user credentials and logs into the account.
enter_code(): Handles the manual entry of the verification code for two-factor authentication.
scrape_balance(): Navigates to the checking account page and retrieves the balance.
