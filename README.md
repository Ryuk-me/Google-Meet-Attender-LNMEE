# Google-Meet-Attender-LNMEE

> This BOT will attend your online google meet classes on your behalf.
---

### Clone this repo
```sh
$ git clone https://github.com/Ryuk-me/Google-Meet-Attender-LNMEE

```
---

## Installation for localhost
Make sure your have `python3` and chrome browser installed.</br>
```sh
$ pip install -r requirements.txt
```
#### Run command
<i>To get Cookies</i>
```sh 
python get_cookies.py
```

<i> To start BOT</i>
```sh
python main.py
```


---
# How to get cookies 
```sh
 after cloning the repo run `get_cookies.py`
 and login to your google account
```

---

# How to Deploy it on Heroku

> Why do we need it to deploy on heroku ?

```sh
1. If we run it on localhost we have to always manually start it.</br>(And if we do that then why we should call it a BOT)</br>
2. It will consume our cpu usage, data usage and our time.

```
> Why we use heroku ?

Heroku provides free server hosting and 500hrs monthly usage which will be more than enough for us.
If you havent created account on heroku create one.

#### So Coming to the main point How to deploy it on heroku

```sh
0. First of all get your cookies.
1. go to heroku and create a new app and enter a unique name for your app.
2. Choose region united states.
3. Now go to settings.
4. Click on add buildpack and add the following one by one and save changes.
  $ python
  $ https://github.com/heroku/heroku-buildpack-google-chrome
  $ https://github.com/heroku/heroku-buildpack-chromedriver

5. Click on reveal configs vars

6. Add following vars one by one 

    KEY                       VALUES
    CHROMEDRIVER_PATH         /app/.chromedriver/bin/chromedriver
    GOOGLE_CHROME_BIN         /app/.apt/usr/bin/google-chrome
    TZ                        Asia/Kolkata

7. Now go to Deploy Option Heroku.
8. Install heroku CLI and enter following commands one by one.
    $ heroku login
9. Open command prompt or any terminal in your current directory where all files are located.
    $ git init
    $ heroku git:remote -a your-app-name
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master

10. Then go to resource option and turn on the bot.

```
You can also watch this video of heroku deployment. 

[Heroku Deployment Video](https://www.youtube.com/watch?v=rfdNIOYGYVI) Skip to 11:00

---

# Tips
```sh
Turn off BOT after class is completed (to save heroku dyno hours).
Turn on BOT Before Sleeping so it can attend your class while your are asleep.
```
---

# SOME IMPORTANT NOTES

```sh

This bot will only work with `B SEE A 2019 Batch`
if you are not from this batch then do some changes in python file it should work for you as well.

Turn Off two step verification if enabled.

Dont use your primary gmail account.

First run get_cookie.py and get your gmail account cookies. ( NECESSARY i repeat it is NECESSARY )

Dont share these cookies with anyone.

```
---

# DISCLAIMER

<i>This <strong>BOT</strong> is created for educational purposes only.</br></i>
<i>The usage of this <strong>BOT</strong> is at the own risk of the User.</br></i>
<i>The Creator shall not be held responsible for any  misconduct on your behalf.</br></i>
<i>You are <strong>agreeing</strong> to all these <strong>conditions</strong> before dowloading or cloning this <strong>repository<strong>.</i>

#### <i>“Education is the most powerful weapon which you can use to change the world.”</i><strong> ― Nelson Mandela</strong></br>
<i> Attend all classes <strong>sincerely</i>.</br></br>


#### License

MIT © [Neeraj Kumar](https://github.com/Ryuk-me)
