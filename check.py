from datetime import date, datetime
import re

today = date.today()

todays_data = today.strftime("%B %d, %Y").replace(',', '').split(' ')
day_name= datetime.now().strftime("%A")

current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)
todays_data.append(current_time)
todays_data.append(day_name)

[month,date,year,time,day_name] = todays_data

startTime = "27 11 12"
startTime = list(map(int, startTime.split()))
print(startTime)
print(datetime(*startTime))
print(f"Waiting until first Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...",end="")
# import datetime
now = datetime.now()
print('f')
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
print(datetime.now().hour)
print(f'{now.year} {now.month} {now.day} 23 05 00')
print(now.strftime("%A"))


for i in range(2):
    print(i)

# print(current_time)
# print(month)
# print(date)
# print(year)
# print(time)
# print(day_name)

# def timeStamp():
#     timeNow = str(datetime.now())
#     timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeNow)
#     return(timeRegEx[0])

# print(timeStamp())

