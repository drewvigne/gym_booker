"""
Author: Drew Vigne

Script to automatically sign up for gym access at
the University of Central Florida. Due to Covid,
the gym is limited to 30 person capacity every 30
minutes. The gym allows users to book an appointment
24 hours in advance, but due to low supply and high
demand these appointments are sold out quickly.

This script books an appointment as soon as its 
available and sends a text message notification 
to confirm. The appointment is then automatically
added to the user's calendar. 

Note that gym hours may vary, but appointments 
can generally be booked in 30 minute increments
(e.g. 7:00, 7:30, 8:00, ...)

Beats the humans every time...

Created: 8/26/2020
"""

from selenium import webdriver
import time
import datetime
import pytext

##############################################################################

# Replace with your own credentials
my_username = 'xxxxxxxx' 
my_password = 'xxxxxxxx'

# Replace with the hour interval you want to go to the gym
start_time = " 12:00:00 PM"
end_time = " 1:00:00 PM"

fmt_start_time = "12pm" # Your start time without 00:00:00 formatting

# Sets appointment date to 24 hours from when the script runs
appt_date = datetime.date.today() + datetime.timedelta(days=1)
# Formats the string into m/d/yyyy without preceding 0's
fmt_appt_date = appt_date.strftime("%#m/%#d/%Y")
# Set up list to scan for matching onclick event
onclick_str_match = [fmt_appt_date + start_time, fmt_appt_date + end_time]
    
##############################################################################

def book_appt():
    # Opens webbrowser, accepts cookies, and begins login procedure
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
    
    # Uncomment this to book RWC Main Facility Access Reservations
    driver.get("https://ucfrwc.org/Program/GetProgramDetails?courseId"\
               "=294d066b-156c-4189-9fc4-f29e66389683&semesterId=7ff5a89d"\
               "-3a20-4609-a315-cca04ecedf16")
    # Uncomment this to book Lap Pool Reservations
    #driver.get("https://ucfrwc.org/Program/GetProgramDetails?courseId"\
               #"=900973fc-a5ee-46b9-9c1b-8a532b273c2d&semesterId=7ff5a89d"\
               #"-3a20-4609-a315-cca04ecedf16")
    
    driver.find_element_by_id("gdpr-cookie-accept").click()    
    driver.find_element_by_id("loginLink").click()
    
    time.sleep(2) # Need to make this into implicit wait function
    
    driver.execute_script("submitExternalLoginForm('Shibboleth')")
   
    # Logs in using user's UCF credentials
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(my_username)
    password.send_keys(my_password)
    driver.find_element_by_class_name("form-element-wrapper").click()
    
    # Scrolls down to bottom of register page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Locates and stores all available gym appointments
    elements = driver.find_elements_by_xpath("(//button[@class='btn btn-primary'])")
    
    # Searches for valid appointments based on start_time, end_time, and appt_date
    x = 0
    onclick_str = []
    # Create a list for each available appointment
    print("List of available onclick functions:\n")
    for element in elements:
        onclick_str.append(element.get_attribute("onclick"))
        print(element.get_attribute("onclick"))
        print("=============================================================")
        x = x + 1
    # Loop through the list and book appointment if onclick strings match
    for y in range(0,x):
        if onclick_str[y].find(onclick_str_match[0]) != -1:
            if onclick_str[y].find(onclick_str_match[1]) != -1: 
                print("\nValid appointment found. Booking now.")
                
                driver.execute_script(onclick_str[y])
    
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
                driver.find_element_by_id("checkoutButton").click()
    
                driver.execute_script("Submit()")
                
                driver.close()
                
                return True
            
            else:
                print("\nSearching...")
        else:
            print("\nSearching...")

    driver.close()

    return False

##############################################################################
    
# Main function
print("Gym Booker Started.\n")
if book_appt() == True:
    print("\nGym Booker Success.")
    # Customize this message to be sent to you. Requires pytext configuration.
    my_message = "Drew, you have a gym appointment tomorrow at " + fmt_start_time + "."
    pytext.send(my_message)
else:
    print("\nGym Booker Failed.")
    # Customize this message to be sent to you. Requires pytext configuration.
    my_message = "Sorry Drew, your gym appointment could not be booked."
    pytext.send(my_message)
    





