import bs4
import requests
import datetime

# data = requests.get('http://kurstenge.kz/')
#
# # print(data.text)
#
# dom = bs4.BeautifulSoup(data.text)
# print(dom.select('td')[0].getText)


listPeremena = [ '8:00-8:50','9:05-9:55','10:10-11:00','11:15-12:05','12:20-13:10','13:25-14:15','14:30-15:20','15:35-16:25','17:45-18:35']




#
# hourNew = 8
#
# minNew = 50
#
# hour = 8
#
# minute = 0
#
# time = int(time) + minute
# if time > 60:
#     timeNew = int(time) - 60
#     hour = hour + 1
#     print('До конца осталось')
#     print(timeNew)
#
#     print(str(hour) + ':' + str(timeNew))
# minute = minute + time
# minute = minNew - minute
# print( 'До звонка осталось ' + str(minute) + ' минут')

lists = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# # nowHour = datetime.datetime.now()
# # nowHour = nowHour.hour
# nowHour = input('hourss')
# Hours = int(nowHour) - 8
# minute = lists[Hours]
#
# print(minute)
#
# now = datetime.datetime.now()
#
# myTime = now.minute
#
# newTime = myTime - 50 + int(minute)
#
# print('до звонка ' + str(newTime) + ' мин')



listZvonok = ['8:00','9:05' ,'10:10' ,'11:15' ,'12:20' ,'13:25' ,'14:30', '15:35', '16:40', '17:45', '18:50' ]

listMonth = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
now = datetime.datetime.now()
day = now.day
month = now.month
month = listMonth[month - 1]
hour = now.hour
minute = now.minute
year = now.year
retrn = str(day) + ' ' + month.strip()+ ' ' + str(year) + ' года'+ ' ' + str(hour) + ':' + str(minute)
print(retrn)


