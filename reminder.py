import time
from win10toast import ToastNotifier
print('What should I remind you about?')
rem = str(input())
print("In how many minutes?")
local_time = float(input())
local_time *= 60
time.sleep(local_time)
toaster = ToastNotifier()
toaster.show_toast(rem,duration=10)
