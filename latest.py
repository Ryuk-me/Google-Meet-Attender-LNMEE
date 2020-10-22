from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, datetime
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pause
import re
import sys


#!####### TIME #########################
now = datetime.now()

startTime = f'{now.year} {now.month} {now.day} 09 27 00'
endTime = f'{now.year} {now.month} {now.day} 10 00 00'
day_name = now.strftime("%A")

saturday_startTime = f'{now.year} {now.month} {now.day} 23 08 00'

#!#######################################

#! USER DETAILS ##########################

email = "csk709120@gmail.com"
password = "friend55"
meetingcode = 'bce-bnpb-ohv'
full_name_with_roll = "Shyam Kumar Roll number 193712"

# meetingcode = 'bic-hmju-wxq'  #class CODE


# * ADMIT TIMEOUT = 10 min

#! #######################################

url = r"https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A105e562d5a68f86b%2C10%3A1603179928%2C16%3A14a70df4be2b8d00%2Ca24ec09a79ffacd8305947481c8b994a209093040a1196a8ddd7b25a5c77d9b3%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22a12f4d2d47444ebb8dc94213b97cc927%22%7D&response_type=code&flowName=GeneralOAuthFlow"


# if(re.match('\w\w\w[-.]\w\w\w\w[-.]\w\w\w', meetingcode) == False or meetingcode == ""):
#     print('Please Check Your meeting CODE')
#     sys.exit()


def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--window-size=800,800")
    chromeOptions.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                    "profile.default_content_setting_values.media_stream_camera": 2,
                                                    "profile.default_content_setting_values.geolocation": 2,
                                                    "profile.default_content_setting_values.notifications": 2
                                                    })

    driver = webdriver.Chrome(chrome_options=chromeOptions)
    return driver


def login():
    driver.get(url)
    usernameSend = wait.until(
        when.element_to_be_clickable((by.ID, "identifierId")))
    sleep(1)
    usernameSend.send_keys(email)
    next_button = wait.until(
        when.element_to_be_clickable((by.ID, 'identifierNext')))
    next_button.click()
    password_send = wait.until(when.element_to_be_clickable(
        (by.NAME, "password")))
    sleep(1)
    password_send.send_keys(password)

    passwordNextButton = wait.until(
        when.element_to_be_clickable((by.ID, "passwordNext")))
    passwordNextButton.click()
    sleep(5)


def meet_redirect():
    driver.get(f'https://meet.google.com/{meetingcode}')
    sleep(5)
    try:

        if(check_exists_by_xpath("//*[@id=\"yDmH0d\"]/div[3]/div/div[2]/div[3]/div/span/span")) == True:

            #! DISMISS BUTTON
            dismiss = wait.until(when.element_to_be_clickable(
                (by.XPATH, "//*[@id=\"yDmH0d\"]/div[3]/div/div[2]/div[3]/div/span/span")))
            dismiss.click()
            sleep(2)
    except:
        pass

    try:
        # ! mic option closed
        if(check_exists_by_css("[aria-label='Close']") == True):

            close_mic_option = wait.until(when.element_to_be_clickable(
                (by.CSS_SELECTOR, "[aria-label='Close']")))
            close_mic_option.click()
            sleep(2)
    except NoSuchElementException:
        pass

    # ! TURNED OFF VIDEO OPTION JUST TO BE SURE
    if(check_exists_by_css("[aria-label='Turn off camera (CTRL + E)']") == True):

        video_hide_btn = wait.until(when.element_to_be_clickable(
            (by.CSS_SELECTOR, "[aria-label='Turn off camera (CTRL + E)']")))
        video_hide_btn.click()
        sleep(1)
    else:
        pass

    try:
        driver.find_element_by_xpath(
            "//span[contains(text(),'Ask to join')]").click()
        sleep(60)  # !change it to 5-6 minutes e.g 300-360 sec
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//span[contains(text(),'Join now')]").click()
        sleep(60)
    try:
        if(check_exists_by_xpath("//span[contains(text(),'Join now')]") == True):
            print("available")
            driver.find_elements_by_xpath(
                "//span[contains(text(),'Join now')]").click()
            sleep(5)

    except NoSuchElementException:
        pass


def end_meet():
    click_on_body = wait.until(
        when.element_to_be_clickable((by.CSS_SELECTOR, 'body')))  # ! It will click on a body tag i.e Hom

    click_on_body.click()
    sleep(1)
    end_call_btn = wait.until(when.element_to_be_clickable(
        (by.CSS_SELECTOR, "[aria-label='Leave call']")))  # ! It will End the call
    end_call_btn.click()


def send_roll():

    select_chat_btn = wait.until(when.element_to_be_clickable(
        (by.CSS_SELECTOR, "[aria-label='Chat with everyone']")))
    select_chat_btn.click()

    sleep(60)  # ! It will wait for 60 sec after clicking chat button


def send_roll_direct():
    driver.find_elements_by_css_selector(
        "[aria-label='Send a message to everyone']")[0].send_keys(full_name_with_roll, Keys.ENTER)


def check_exists_by_css(css_Selector):
    try:
        driver.find_element_by_css_selector(css_Selector)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":
    if(day_name != 'Saturday' or day_name != 'Sunday'):
        driver = browser()
        wait = webdriver.support.ui.WebDriverWait(driver, 5)
        startTime = list(map(int, startTime.split()))
        endTime = list(map(int, endTime.split()))
        print(
            f"Waiting until Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...")
        pause.until(datetime(*startTime))
        login()
        try:
            meet_redirect()
            while(check_exists_by_css("[aria-label='Chat with everyone']") != True):
                meet_redirect()
            send_roll()
            for i in range(2):
                send_roll_direct()
                sleep(30)
            print(
                f"Waiting until meet End time [{endTime[-3]:02}:{endTime[-2]:02}:{endTime[-1]:02}]...")
            if(datetime.now().strftime("%H:%M:%S") >= '10:01:00'):
                print("Exiting")
                try:
                    end_meet()
                except:
                    driver.quit()
                    sys.exit()
            else:
                pause.until(datetime(*endTime))
            try:
                end_meet()
                driver.quit()
            except:
                driver.quit()
        except:
            pass
    else:
        print('I wont Run Today HueHueHue 😈')
