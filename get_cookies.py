from selenium import webdriver
import pickle
import sys
import time


driver = webdriver.Chrome()
driver.get('https://accounts.google.com/') #! Enter Your Credentials Here and login
#! If your are getting error on this site i.e Cant log you in the replace upper link  with this link.
"""

https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A2ffd464484c3c38d%2C10%3A1607957090%2C16%3A0977f6e09915f124%2C34e66ed3e9778be3ca3cc287a9745c5090f79c8fff5f0694f00a4221e8904ee2%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%220703ffebb2a74fcebcc35ab3a1c5eb84%22%7D&response_type=code&flowName=GeneralOAuthFlow


"""

check_login = input("Have You Sucessfully Logged in ? (y for yes n for no) : ") #! Enter 'y' for yes 'n' for no

if(check_login.lower() == 'y'):
    pickle.dump(driver.get_cookies(), open("lnme.pkl", "wb"))
    print("Logged in Sucessfully\nExiting in 10 seconds......")
    time.sleep(10)
    driver.quit()

else:
    print("Unsucessfull !!!!\n\
Please Login Again.")
    sys.exit()

