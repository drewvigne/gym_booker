# Gym Booker

### About
Script to automatically sign up for gym access at the University of Central Florida. Due to Covid, the gym is limited to 30 person capacity every 30 minutes. The gym allows users to book an appointment 24 hours in advance, but due to low supply and high demand these appointments are sold out quickly. 

This script books an appointment as soon as its available and sends a text message notification to confirm. The appointment is then automatically added to the user's calendar.   

Note that gym hours may vary, but appointments can generally be booked in 30 minute increments (e.g. 7:00, 7:30, 8:00, ...)

Beats the humans every time...  

### Requirements
- [Python 3.8.5](https://www.python.org/downloads/)
- [Spyder IDE (preffered)](https://www.spyder-ide.org/) 
- Some sort of Python script server, perhaps a Raspberry Pi or online service
- Or Windows Task Scheduler if hosting on your Windows PC
- [PyText Module](https://github.com/drewvigne/pytext)
- Chromedriver.exe

## Installation
You will of course need to install Python and your IDE with standard settings. To install PyText, refer to its GitHub repository. Add the Gym Booker script to wherever you store your Python Scripts.  

Install Chromedriver.exe by placing it into preferably your program files like so:  
```
C:\Program Files (x86)\chromedriver.exe'
```  

Until I get my hands on a Linux server, I will be employing Windows Task Scheduler to automate this script to run every other day. Plenty of tutorials are out there that talk about how to schedule Python Scripts with Windows Task Scheduler. You can set your interval to whatever you'd like.  

## Running the script
Open gym_booker.py in Spyder and configure your desired parameters.
 - my_username is your NID
 - my_password is your NID password
 - start_time is when your gym appointment starts
 - end_time is when your gym appointment ends
 - Make sure to also configure fmt_start_time as that is the parameter that is texted to you via PyText  
 
To test out the script simply press play. It uses selenium to automate the entire webbrowser experience. Kick back, relax, and never worry about scheduling your gym appointment again.  

## To do
- Need to add implicit wait function as time.sleep(2) is very inefficient
- Possibly create separate function for the onclick search procedure in the book_appt() function
