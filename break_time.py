import webbrowser
import time

total_break_time = 3
count_break_time= 1

while (count_break_time <= total_break_time):
	time.sleep(10)
	webbrowser.open("https://google.com")
	count_break_time=count_break_time+1
	