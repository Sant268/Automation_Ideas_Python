import time
from win10toast import ToastNotifier
print('What should I remind you about?')
rem = str(input())
print("In how many minutes?")
local_time = float(input())
local_time *= 60
print('I will remind you for ' + rem + ' in ' + str(local_time) + ' seconds ')
time.sleep(local_time)
toaster = ToastNotifier()
toaster.show_toast(rem, "Here is your reminder!", duration=10)
