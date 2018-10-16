"""
CALENDER
ADD/UPDATE/DEL EVENTS
"""
from time import sleep, strftime
import sys
calendar = {}

def welcome():
  animation = "|/-\\"
  for i in range(24):
    sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
  print ('welcome to your calendar .^.')
  sleep(1)
  print ("\\"+"date: "+ (strftime('%A %B %d, %Y')).lower())
  sleep(1)
  print ("\\"+'time: '+strftime("%H:%M:%S"))
  sleep(1)
  print()

def start_calendar():
  welcome()
  start = True
  while start:
    sleep(1.5)
    choice = input("\n(a)dd | (u)pdate | (v)iew | (d)el | e(x)it\n\n")
    if choice == 'v':
      if len(calendar.keys()) < 1:
        print ('the calendar is empty\n')
      else:
        for y in calendar:
          print (y, calendar[y])
    elif choice == 'u':
      date = input('date(M/D/Y): ')
      update = input('info: ')
      calendar[date] = update
      print ('update successful\n')
    elif choice == 'a':
      date = input('date(M/D/Y): ')
      event = input('event: ')
      calendar[date] = event
      print ('event added')
    elif choice == 'd':
      event = input("delete: ")
      for date in calendar.keys():
        if event == calendar[date]:
          del calendar[date]
      print ('event deleted =_=\n')
    elif choice == 'x':
      start = False
    else:
      continue
  sleep(1)


start_calendar()