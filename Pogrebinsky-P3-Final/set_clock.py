__author__ = 'pogrebinsky' 

#This program is a implementation of a GUI and audio interface which allows users to set the day and time
# No AM or PM is implemented

# Sources below were used as reference points essentially came from googling questions
# https://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
# https://stackoverflow.com/questions/18884782/typeerror-worker-takes-0-positional-arguments-but-1-was-given
# https://www.python-course.eu/tkinter_events_binds.php
# https://stackoverflow.com/questions/32936408/python-2-7-tkinter-how-to-change-text-color-of-a-buttons-text
# https://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter-python-2-7
# https://stackoverflow.com/questions/4066202/resizing-pictures-in-pil-in-tkinter
# http://effbot.org/tkinterbook/place.htm

# From http://www.ferg.org/thinking_in_tkinter/tt070_py.txt
# Adapted by A. Hornof 2017 
# Adapted further by T. Pogrebinsky 2017

from tkinter import *
import os
import sound


class MyApp:
	#initial introduction and some instructions on navigation are in the below sound file
	my_path = "my_wav_files/"
	sound.Play(my_path + "intro_wav.wav")
	index_set_settings = 0 #this is an index for the list of voices and list of buttons
	
    #indices below are for displaying labels and playing sounds from sets
	index_days = 0
	index_hours = 0
	index_minutes = 0

	#booleans below are for keeping track of what j and k do for example if setDay is true j and k cycle through days
	setDay = False
	setHour = False
	setMinutes = False
	quit = False

	#booleans below are to keep track of when a user is returning from a sub menu
	day_is_set = False
	minutes_are_set = False
	hour_is_set = False


	def __init__(self, parent):

		self.myParent = parent
		self.main_menu_container = Frame(parent)
		self.main_menu_container.pack()
		self.myParent.bind("<j>", self.keyPress)  # ajh
		self.myParent.bind("<k>", self.keyPress)  # ajh
	#NOTE: the below "magic numbers " are relative to the size of my sets, example hours has 12 numbers, week has 7 days
	def keyPress(self, event):
		if(event.keysym == "k"):
			#if the user has selected the day menu already
			if(MyApp.setDay):
				#if the index reaches the end of my days array i need to restart the index to avoid out of bounds
				#there are 7 days in a week but the index starts at 0
				if(MyApp.index_days < 6):
					MyApp.index_days+=1
					day_labels[MyApp.index_days].configure(fg="red", background="green")
					sound.Play(voiced_days[MyApp.index_days])
					day_labels[MyApp.index_days-1].configure(fg="black", background="white")
				else:
					#if the index reaches the end of my days array i need to restart the index to avoid out of bounds
					MyApp.index_days = 0
					monday_label.configure(fg="red",background="green")
					sound.Play(voiced_days[MyApp.index_days])
					sunday_label.configure(fg="black",background="white")
			#if the user has selected the hour menu item
			elif(MyApp.setHour):
				#similar to above, trying to avoid out of bound errors as my set is only 12 items
				if(MyApp.index_hours < 11):
					MyApp.index_hours+=1
					hour_labels[MyApp.index_hours].configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_hours+1])
					hour_labels[MyApp.index_hours-1].configure(fg="black",background="white")
				else:
					MyApp.index_hours = 0
					one_label_h.configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_hours+1])
					twelve_label_h.configure(fg="black",background="white")
			#if the user selected the minutes menu
			elif(MyApp.setMinutes):
				if(MyApp.setMinutes):
					#using 12 (0-11) numbers for minutes because i will increment by 5 and there is no :60 o clock, if a developer wanted to improve simply change the 12 to 59
					#simply change the label array to all 59 labels and then change the voice array also.
					if(MyApp.index_minutes < 11):
						MyApp.index_minutes+=1
						minute_labels[MyApp.index_minutes].configure(fg="red" ,background="green")
						sound.Play(NUMBERS_WAV[MyApp.index_minutes*5])# this is *5 because I incremented by factors of 5
						minute_labels[MyApp.index_minutes-1].configure(fg="black",background="white")
					else:
						MyApp.index_minutes = 0
						zero_label.configure(fg="red",background="green")
						sound.Play(NUMBERS_WAV[MyApp.index_minutes*5])# this is *5 because I incremented by factors of 5
						fifty_five_label.configure(fg="black",background="white")
			#the user has selected the quit menu item
			elif(MyApp.quit):
				root.destroy()
			#if the user has not selected any menu
			else:
				if(MyApp.index_set_settings < 3):
					MyApp.index_set_settings+=1
					buttons[MyApp.index_set_settings].configure(highlightbackground="green")
					buttons[MyApp.index_set_settings-1].configure(highlightbackground="white")
				else:
					MyApp.index_set_settings = 0
					buttons[0].configure(highlightbackground="green")
					buttons[1].configure(highlightbackground="white")
					buttons[2].configure(highlightbackground="white")
					buttons[3].configure(highlightbackground="white")
				#play which menu item they are on, (these will be the top menus: ie: set day, hour, minute)
				sound.Play(voices[MyApp.index_set_settings])
		elif(event.keysym == "j"):
			#same logic as above only now we are moving left in our visual list
			if(MyApp.setDay):
				if(MyApp.index_days > 0):
					MyApp.index_days-=1
					day_labels[MyApp.index_days].configure(fg="red",background="green")
					sound.Play(voiced_days[MyApp.index_days])
					day_labels[MyApp.index_days+1].configure(fg="black", background="white")
					
				else:
					MyApp.index_days = 6
					monday_label.configure(fg="black",background="white")
					sound.Play(voiced_days[MyApp.index_days])
					sunday_label.configure(fg="red",background="green")
			elif(MyApp.setHour):
				if(MyApp.index_hours > 0):
					MyApp.index_hours-=1
					hour_labels[MyApp.index_hours].configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_hours+1])
					hour_labels[MyApp.index_hours+1].configure(fg="black",background="white")
				else:
					MyApp.index_hours = 11
					twelve_label_h.configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_hours+1])
					one_label_h.configure(fg="black",background="white")
			elif(MyApp.setMinutes):
				if(MyApp.index_minutes > 0):
					MyApp.index_minutes-=1
					minute_labels[MyApp.index_minutes].configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_minutes*5])# this is *5 because I incremented by factors of 5
					minute_labels[MyApp.index_minutes+1].configure(fg="black",background="white")

				else:
					MyApp.index_minutes = 11
					fifty_five_label.configure(fg="red",background="green")
					sound.Play(NUMBERS_WAV[MyApp.index_minutes*5])# this is *5 because I incremented by factors of 5
					zero_label.configure(fg="black", background="white")

			elif(MyApp.quit):
				root.destroy()
			else:
				if(MyApp.index_set_settings > 0):
					MyApp.index_set_settings-=1
					buttons[MyApp.index_set_settings].configure(highlightbackground="green")
					buttons[MyApp.index_set_settings+1].configure(highlightbackground="white")
				else:
					MyApp.index_set_settings = 3
					buttons[0].configure(highlightbackground="white")
					buttons[1].configure(highlightbackground="white")
					buttons[2].configure(highlightbackground="white")
					buttons[3].configure(highlightbackground="green")
				sound.Play(voices[MyApp.index_set_settings])
			
	#user can choose to mouse click main menu buttons
def setDayButtonClick(self):
	set_day_button.configure(highlightbackground="green")
	set_hour_button.configure(highlightbackground="white")
	set_minute_button.configure(highlightbackground="white")
	MyApp.index_set_settings = 0
	setDay = True
	setHour = False
	setMinutes = False
	sound.Play(voices[0])
	#user can choose to mouse click main menu buttons
def setHourButtonClick(self):
	set_day_button.configure(highlightbackground="white")
	set_hour_button.configure(highlightbackground="green")
	set_minute_button.configure(highlightbackground="white")
	setDay = False
	setHour = True
	setMinutes = False
	MyApp.index_set_settings = 1
	sound.Play(voices[1])
	#user can choose to mouse click main menu buttons

def setMinuteButtonClick(self):
	set_day_button.configure(highlightbackground="white")
	set_hour_button.configure(highlightbackground="white")
	set_minute_button.configure(highlightbackground="green")
	setDay = False
	setHour = False
	setMinutes = True
	MyApp.index_set_settings = 2
	sound.Play(voices[2])
	#user can choose to mouse click main menu buttons
def quitButtonClick(self):
	root.destroy()

root = Tk()
# I use this to capture the space bar press
def key(event):
	
	char_pressed = repr(event.char)
	# if the user pressed the space bar
	if(char_pressed == "' '"):
		sound.Play(voices[MyApp.index_set_settings])

		#we can determine if the user selected day hour or minute by the index 0 1 or 2
		if(MyApp.index_set_settings == 0):
			if(MyApp.setDay):
				#this initial step is a way to escape from the submenu, we need to keep track of whether or not
				# this is there first time pressing the space bar on said menu, as space bar will also be the
				# users escape
				day_is_set = True
				MyApp.setDay = False
				current_day_label.configure(text=day_labels[MyApp.index_days].cget("text"))
				sound.Play("my_wav_files/day_set.wav")
			else:
				day_labels[MyApp.index_days].configure(background="green", fg="red")
				sound.Play("my_wav_files/set_day_with_description.wav")
				MyApp.setDay = True

		elif(MyApp.index_set_settings == 1):
			if(MyApp.setHour):
				hour_is_set = True
				MyApp.setHour = False
				current_hour_label.configure(text=hour_labels[MyApp.index_hours].cget("text"))
				sound.Play("my_wav_files/hour_set.wav")
			else:
				hour_labels[MyApp.index_hours].configure(background="green", fg="red")
				sound.Play("my_wav_files/set_hour_with_description.wav")
				MyApp.setHour = True
		elif(MyApp.index_set_settings == 2):
			if(MyApp.setMinutes):
				minutes_are_set = True
				MyApp.setMinutes = False
				#need to add an extra zero for single digit numbers in the time
				# in this case there is only two single option numbers since we increment minutes by 5.
				# 2 because index 0 = 0 and index 1 = 5 whereas index 2 = 10 (2 digit number)
				if(MyApp.index_minutes < 2):
					current_minute_label.configure(text="0" + "" + minute_labels[MyApp.index_minutes].cget("text"))
				else:
					current_minute_label.configure(text=minute_labels[MyApp.index_minutes].cget("text"))
				sound.Play("my_wav_files/minutes_are_set.wav")

			else:
				minute_labels[MyApp.index_minutes].configure(background="green", fg="red")
				sound.Play("my_wav_files/set_minutes_with_description.wav")
				MyApp.setMinutes = True
				
			
		elif(MyApp.index_set_settings == 3):
			sound.Play("my_wav_files/quit.wav")
			root.destroy()
	else:
		#this menu would mean the user did not press space bar, j or k
		print("Please press valid key")

# function that was used in an example i found for capturing key clicks including special characters
def callback(event):
    root.focus_set()
   
#change size of the GUI
root.geometry("800x480")
# change the background color of GUI
root.configure(bg="light blue")
# part of how i capture keys pressed that are special characters
root.bind("<Key>", key)
root.bind("<Button-1>", callback)

main_menu_container = Frame()
#display the menu
main_menu_container.pack()
#button for setting the day and displaying the day submenu
set_day_button = Button(main_menu_container)
set_day_button.configure(text="SET DAY", highlightbackground="green")
set_day_button.pack(side=LEFT)
set_day_button.bind('<Button-1>', setDayButtonClick)

#button for setting the hour and displaying the hour menu
set_hour_button = Button(main_menu_container)
set_hour_button.configure(text="SET HOUR")
set_hour_button.pack(side=LEFT)
set_hour_button.bind('<Button-1>', setHourButtonClick)
#button for setting the minutes and displaying the minutes menu
set_minute_button = Button(main_menu_container)
set_minute_button.configure(text="SET MINUTES")
set_minute_button.pack(side=LEFT)
set_minute_button.bind('<Button-1>', setMinuteButtonClick)
#button for exiting the program
quit_button = Button(main_menu_container)
quit_button.configure(text="QUIT")
quit_button.pack(side=LEFT)
quit_button.bind('<Button-1>', quitButtonClick)

#label of days
monday_label = Label()
monday_label.configure(text="Monday", fg="red")

tuesday_label = Label()
tuesday_label.configure(text="Tuesday")

wednesday_label = Label()
wednesday_label.configure(text="Wednesday")

thursday_label = Label()
thursday_label.configure(text="Thursday")

friday_label = Label()
friday_label.configure(text="Friday")

saturday_label = Label()
saturday_label.configure(text="Saturday")

sunday_label = Label()
sunday_label.configure(text="Sunday")

#labels for minutes
zero_label = Label(text="0")
one_label = Label(text="1")
two_label = Label(text="2")
three_label = Label(text="3")
four_label = Label(text="4")
five_label = Label(text="5")
six_label = Label(text="6")
seven_label = Label(text="7")
eight_label = Label(text="8")
nine_label = Label(text="9")
ten_label = Label(text="10")
eleven_label = Label(text="11")
twelve_label = Label(text="12")
thirteen_label = Label(text="13")
fourteen_label = Label(text="14")
fifteen_label = Label(text="15")
sixteen_label = Label(text="16")
seventeen_label = Label(text="17")
eighteen_label = Label(text="18")
nineteen_label = Label(text="19")
twenty_label = Label(text="20")
twenty_one_label = Label(text="21")
twenty_two_label = Label(text="22")
twenty_three_label = Label(text="23")
twenty_four_label = Label(text="24")
twenty_five_label = Label(text="25")
twenty_six_label = Label(text="26")
twenty_seven_label = Label(text="27")
twenty_eight_label = Label(text="28")
twenty_nine_label = Label(text="29")
thirty_label = Label(text="30")
thirty_one_label = Label(text="31")
thirty_two_label = Label(text="32")
thirty_three_label = Label(text="33")
thirty_four_label = Label(text="34")
thirty_five_label = Label(text="35")
thirty_six_label = Label(text="36")
thirty_seven_label = Label(text="37")
thirty_eight_label = Label(text="38")
thirty_nine_label = Label(text="39")
forty_label = Label(text="40")
forty_one_label = Label(text="41")
forty_two_label = Label(text="42")
forty_three_label = Label(text="43")
forty_four_label = Label(text="44")
forty_five_label = Label(text="45")
forty_six_label = Label(text="46")
forty_seven_label = Label(text="47")
forty_eight_label = Label(text="48")
forty_nine_label = Label(text="49")
fifty_label = Label(text="50")
fifty_one_label = Label(text="51")
fifty_two_label = Label(text="52")
fifty_three_label = Label(text="53")
fifty_four_label = Label(text="54")
fifty_five_label = Label(text="55")
fifty_six_label = Label(text="56")
fifty_seven_label = Label(text="57")
fifty_eight_label = Label(text="58")
fifty_nine_label = Label(text="59")

#labels for hours
one_label_h = Label(text="1")
two_label_h = Label(text="2")
three_label_h = Label(text="3")
four_label_h = Label(text="4")
five_label_h = Label(text="5")
six_label_h = Label(text="6")
seven_label_h = Label(text="7")
eight_label_h = Label(text="8")
nine_label_h = Label(text="9")
ten_label_h = Label(text="10")
eleven_label_h = Label(text="11")
twelve_label_h = Label(text="12")
#labeling the labels for readability to the user
hour_label = Label(text="Hour:")
minute_label = Label(text="Minute:")
day_label = Label(text="Day:")
# I made sets of labels and buttons for indexing for the percieved flipping through menus
day_labels = [monday_label, tuesday_label, wednesday_label, thursday_label, friday_label, saturday_label, sunday_label]
buttons = [set_day_button, set_hour_button, set_minute_button, quit_button]
hour_labels = [one_label_h, two_label_h, three_label_h, four_label_h, five_label_h, six_label_h, seven_label_h, eight_label_h, nine_label_h, ten_label_h, eleven_label_h, twelve_label_h]
minute_labels = [zero_label, five_label, ten_label, fifteen_label, twenty_label, twenty_five_label, thirty_label, thirty_five_label, forty_label, forty_five_label, fifty_label, fifty_five_label, fifty_nine_label]
#day and time final label

current_day_label = Label(text="Monday")
current_hour_label = Label(text="12")
current_colon_label = Label(text=":")
current_minute_label = Label(text="00")

myapp = MyApp(root)
# I made sets of voices and wavs for indexing the percieved verbal indications
voices = ["my_wav_files/set_day.wav", "my_wav_files/set_hour.wav", "my_wav_files/set_minutes.wav", "my_wav_files/quit.wav"]
voiced_days = ["wav_files_provided/days_of_week_m/monday_m.wav", "wav_files_provided/days_of_week_m/tuesday_m.wav", "wav_files_provided/days_of_week_m/wednesday_m.wav", "wav_files_provided/days_of_week_m/thursday_m.wav", "wav_files_provided/days_of_week_m/friday_m.wav", "wav_files_provided/days_of_week_m/saturday_m.wav", "wav_files_provided/days_of_week_m/sunday_m.wav"]
num_path ="wav_files_provided/numbers_m/"
NUMBERS_WAV = [num_path + "00_m.wav", num_path + "01_m.wav", num_path + "02_m.wav",
           num_path + "03_m.wav", num_path + "04_m.wav", num_path + "05_m.wav", num_path + "06_m.wav",
           num_path + "07_m.wav", num_path + "08_m.wav", num_path + "09_m.wav", num_path + "10_m.wav",
           num_path + "11_m.wav", num_path + "12_m.wav", num_path + "13_m.wav", num_path + "14_m.wav",
           num_path + "15_m.wav", num_path + "16_m.wav", num_path + "17_m.wav", num_path + "18_m.wav",
           num_path + "19_m.wav", num_path + "20_m.wav", num_path + "21_m.wav", num_path + "22_m.wav",
           num_path + "23_m.wav", num_path + "24_m.wav", num_path + "25_m.wav", num_path + "26_m.wav",
           num_path + "27_m.wav", num_path + "28_m.wav", num_path + "29_m.wav", num_path + "30_m.wav",
           num_path + "31_m.wav", num_path + "32_m.wav", num_path + "33_m.wav", num_path + "34_m.wav",
           num_path + "35_m.wav", num_path + "36_m.wav", num_path + "37_m.wav", num_path + "38_m.wav",
           num_path + "39_m.wav", num_path + "40_m.wav", num_path + "41_m.wav", num_path + "42_m.wav",
           num_path + "43_m.wav", num_path + "44_m.wav", num_path + "45_m.wav", num_path + "46_m.wav",
           num_path + "47_m.wav", num_path + "48_m.wav", num_path + "49_m.wav", num_path + "50_m.wav",
           num_path + "51_m.wav", num_path + "52_m.wav", num_path + "53_m.wav", num_path + "54_m.wav",
           num_path + "55_m.wav", num_path + "56_m.wav", num_path + "57_m.wav", num_path + "58_m.wav",
           num_path + "59_m.wav"]

#This will display all labels for day, hours and minutes and it will display them when the program begins
day_label.place(relx=1, x= -700, y=75, anchor=NE)
monday_label.place(relx=1, x= -600, y=75, anchor=NE)
tuesday_label.place(relx=1, x= -500, y=75, anchor=NE)
wednesday_label.place(relx=1, x= -400, y=75, anchor=NE)
thursday_label.place(relx=1, x= -300, y=75, anchor=NE)
friday_label.place(relx=1, x= -200, y=75, anchor=NE)
saturday_label.place(relx=1, x= -100, y=75, anchor=NE)
sunday_label.place(relx=1, x= 0, y=75, anchor=NE)

#hour labels
hour_label.place(relx=1, x= -700, y=150, anchor=NE)
one_label_h.place(relx=1, x= -600, y=150, anchor=NE)
two_label_h.place(relx=1, x= -550, y=150, anchor=NE)
three_label_h.place(relx=1, x= -500, y=150, anchor=NE)
four_label_h.place(relx=1, x= -450, y=150, anchor=NE)
five_label_h.place(relx=1, x= -400, y=150, anchor=NE)
six_label_h.place(relx=1, x= -350, y=150, anchor=NE)
seven_label_h.place(relx=1, x= -300, y=150, anchor=NE)
eight_label_h.place(relx=1, x= -250, y=150, anchor=NE)
nine_label_h.place(relx=1, x= -200, y=150, anchor=NE)
ten_label_h.place(relx=1, x= -150, y=150, anchor=NE)
eleven_label_h.place(relx=1, x= -100, y=150, anchor=NE)
twelve_label_h.place(relx=1, x= -50, y=150, anchor=NE)
hour_labels[MyApp.index_hours].configure(fg="red")

#minute labels
minute_label.place(relx=1, x=-700, y= 250, anchor=NE)
zero_label.place(relx=1, x= -600, y=250, anchor=NE)
five_label.place(relx=1, x= -550, y=250, anchor=NE)
ten_label.place(relx=1, x= -500, y=250, anchor=NE)
fifteen_label.place(relx=1, x= -450, y=250, anchor=NE)
twenty_label.place(relx=1, x= -400, y=250, anchor=NE)
twenty_five_label.place(relx=1, x= -350, y=250, anchor=NE)
thirty_label.place(relx=1, x= -300, y=250, anchor=NE)
thirty_five_label.place(relx=1, x= -250, y=250, anchor=NE)
forty_label.place(relx=1, x= -200, y=250, anchor=NE)
forty_five_label.place(relx=1, x= -150, y=250, anchor=NE)
fifty_label.place(relx=1, x= -600, y=300, anchor=NE)
fifty_five_label.place(relx=1, x= -550, y=300, anchor=NE)
minute_labels[MyApp.index_minutes].configure(fg="red")

# make a labels for displaying current settings
current_day_label.place(relx=1, x=-350, y= 450, anchor=NE)
current_hour_label.place(relx=1, x=-312, y= 450, anchor=NE)
current_colon_label.place(relx=1, x=-300, y=450, anchor=NE)
current_minute_label.place(relx=1, x=-275, y=450, anchor=NE)

root.mainloop()
