################################################################################
# set_clock.py
# Talaba Pogrebinsky - OCT 2017
# SITATIONS: Anthony Honof's Sample_menu.py gave the basic layout for how my program is structured. 
#            Along with entire functions from that program.
################################################################################
__author__ = 'pogrebinsky'

# Package imports
import readchar
import time         # for time.sleep()

# Local imports
import sound        # sound.py accompanies this file

################################################################################
# main()
################################################################################
# Written by Anthony Hornof
def main():
    create_sound_filenames()
    # can use below function for testing
    #verify_sound_filenames()
    create_menu_globals()
    run_menu()

################################################################################
# Create the sound objects for the auditory menus and display.
################################################################################
# named by Anthony Hornof, extended by Talaba Pogrebinsky
def create_sound_filenames():

    # Declare global variables.
    global PAUSING_BETWEEN_AUDIO_FILE_DURATION, INTRO_WAV, SET_DAY_WAV, SET_HOUR_WAV, YOU_SELECTED_WAV, NUMBERS_WAV, DAYS_WAV, AM_WAV, PM_WAV, PRESS_AGAIN_TO_QUIT_WAV,\
        EXITING_PROGRAM_WAV, PRESS_TO_QUIT_WAV, EXITING_PROGRAM_WAV_DURATION, TMP_FILE_WAV, DAY_SET_WAV, HOUR_SET_WAV

    # Create  sounds.
    nav_path = "wav_files_provided/miscellaneous_m/"
    num_path = "wav_files_provided/numbers_m/"
    day_path = "wav_files_provided/days_of_week_m/"
    # directory included in submission
    my_files_path = "my_wav_files/"


    INTRO_WAV = my_files_path + "Intro.wav"
    YOU_SELECTED_WAV = nav_path + "you_selected_m.wav"
    
    # Included all 60 in case further development wanted to be done to add minutes
    NUMBERS_WAV = [num_path + "01_m.wav", num_path + "02_m.wav",
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

    PRESS_TO_QUIT_WAV = my_files_path + "Press_to_quit.wav"
    AM_WAV = nav_path + "AM_m.wav"
    PM_WAV = nav_path + "PM_m.wav"
    SET_HOUR_WAV = my_files_path + "Set_hour.wav"
    SET_DAY_WAV = nav_path + "Set_day_of_week_m.wav"
    DAYS_WAV = day_path + "monday_m.wav", day_path + "tuesday_m.wav", day_path + "wednesday_m.wav", day_path + "thursday_m.wav", day_path + "friday_m.wav", day_path + "saturday_m.wav", day_path + "sunday_m.wav"
    PRESS_AGAIN_TO_QUIT_WAV = nav_path + "Press_again_to_quit_m.wav"
    EXITING_PROGRAM_WAV = nav_path + "Exiting_program_m.wav"
    EXITING_PROGRAM_WAV_DURATION = 1.09 # in s. 1.09 is accurate but 0.45 saves time.
    PAUSING_BETWEEN_AUDIO_FILE_DURATION = 1.40  # arbitrary but sounds fluent 
    DAY_SET_WAV = my_files_path + "Day_set.wav"
    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename  for output
    HOUR_SET_WAV = my_files_path + "Hour_set.wav"
################################################################################
# Verify all files can be loaded and played.
# Play all sound files to make sure the paths and filenames are correct and valid.
# The very last sound tested/played should be the sound that plays at startup.
################################################################################
# Written by Anthony Hornof
def verify_sound_filenames():
    sound.Play(PRESS_AGAIN_TO_QUIT_WAV)
    sound.Play(EXITING_PROGRAM_WAV)
    sound.Play(YOU_SELECTED_WAV)
    sound.Play(NUMBERS_WAV[0])
    sound.Play(NUMBERS_WAV[1])
    sound.Play(NUMBERS_WAV[2])
    sound.Play(NUMBERS_WAV[3])
    sound.Play(AM_WAV)
    sound.Play(PM_WAV)
    sound.Play(INTRO_WAV)


################################################################################
# Create some global constants and variables for the menu.
################################################################################
# Written by Anthony Hornof extended by Talaba Pogrebinsky
def create_menu_globals():

    # Declare global variables as such.
    global HELP_KEY, REPEAT_KEY, SET_KEY, FORWARD_KEY, BACKWARD_KEY, QUIT_KEY, MINIMAL_HELP_STRING, CURRENT_TIME, CURRENT_DAY 

    # Constants
    # Keystrokes for the keyboard interaction.
    FORWARD_KEY = 'j' 
    BACKWARD_KEY = 'k'
    SET_KEY = '\x20' # 'space bar'
    QUIT_KEY = ';'
    HELP_KEY = 'h'
    REPEAT_KEY = 'r'

    # A bare minimum of text to display to guide the user.
    MINIMAL_HELP_STRING = "Press " + QUIT_KEY + " to quit."

    # Global variables
    CURRENT_TIME = 0    # The current time that is set. (Just an integer for now.)
    
    CURRENT_DAY  = 0     # the current day is set. (Just an integer for now.)

    CURRENT_HOUR = 0      # the current hour is set. (Just an integer for now.)

    CURRENT_MINUTE = 0    # the current minute is set. (Just an integer for now.)

################################################################################
# Run the menu in an endless loop until the user exits.
################################################################################
# Written by Anthony Hornof extended by Talaba Pogrebinsky
def run_menu():

    global CURRENT_TIME
    global CURRENT_DAY 
    global CURRENT_HOUR
    global CURRENT_MINUTE

    #boolean for switching from days to hours
    days_selection = True

    #boolean for switching from hours to minutes if a developer should extend program for minutes
    hour_selection = False

    #booleans for switching from am to pm
    am = True
    pm = False
    
    # Provide a minimal indication that the program has started.
    print(MINIMAL_HELP_STRING)
    # Indicate program has started and list options for user
    sound.Play(INTRO_WAV)
     
    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the QUIT_MENU_KEY or SET_KEY the second time.
    while True:
        
        #this now should loop though days
        if c == BACKWARD_KEY and days_selection == True:
            if CURRENT_DAY == 0:
                CURRENT_DAY = len(DAYS_WAV)-1
            else:
                CURRENT_DAY -= 1
           

            # Concatenate three audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    DAYS_WAV[CURRENT_DAY])
            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Respond to the user's input. If the day selection is true
        # means if the user has not yet selected a day.
        if c == FORWARD_KEY and days_selection == True:

            # Advance the time, looping back around to the start.
            CURRENT_DAY += 1
            if CURRENT_DAY == len(DAYS_WAV):
                CURRENT_DAY = 0

            # Concatenate three audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    DAYS_WAV[CURRENT_DAY])
            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)
        
        # repeat intro if the user hasnt set the day yet
        if c == REPEAT_KEY and days_selection == True:
            sound.Play(INTRO_WAV)
        # repeat set time instruction if days have been selected
        if c == REPEAT_KEY and days_selection == False:
            sound.Play(SET_HOUR_WAV)
        

        # this now should loop though hours
        # since day selection is false the user already selected a day.
        if c == BACKWARD_KEY and days_selection == False:
            
            # boolean variable for converting am to pm and vice versa
            convert = False

            if CURRENT_TIME == 0:
                CURRENT_TIME = 11

                # change from am to pm or vice versa
                convert = True

            else:
                CURRENT_TIME -= 1
         
            #configure am and pm
            if(convert):
                if am == True:
                    am = False
                    pm = True
                    convert = False
                else:
                    am = True
                    pm = False
                    convert = False

            if am == True:
                # Concatenate three audio files to generate the message.
                sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    NUMBERS_WAV[CURRENT_TIME], AM_WAV)
            else:
                # Concatenate three audio files to generate the message.
                sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    NUMBERS_WAV[CURRENT_TIME], PM_WAV)

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)   
        # selecting hour
        if c == FORWARD_KEY and days_selection == False:

            # variable for converting am to pm and vice versa
            convert = False
            
            # Advance the time, looping back around to the start.
            if (CURRENT_TIME) > 10:
                CURRENT_TIME = 0
                # change from am to pm or vice versa
                convert = True
            else:
                CURRENT_TIME += 1
            

            #configure am and pm
            if(convert):
                if am == True:
                    am = False
                    pm = True
                    convert = False
                else:
                    am = True
                    pm = False
                    convert = False

            if am == True:
                # Concatenate three audio files to generate the message.
                sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    NUMBERS_WAV[CURRENT_TIME], AM_WAV)
            else:
                # Concatenate three audio files to generate the message.
                sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    NUMBERS_WAV[CURRENT_TIME], PM_WAV)

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)    
        

        if c == SET_KEY:

            # third time being pressed
            if hour_selection == False:

                # audio recognition of minutes being selected
                #(sound not created yet >> )sound.Play(MIN_SET_WAV)
                print("hello motto")
                # pause to play next sound
                time.sleep(PAUSING_BETWEEN_AUDIO_FILE_DURATION)
                # informing exit
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break
           

            # second time being pressed
            if days_selection == False:
                # so if day selection is false then program went through hour cycle already and came back
                hour_selection = False
                # audio recognition of hours being selected
                sound.Play(HOUR_SET_WAV)
                
            else:
                # disable day conditions
                days_selection = False
                hour_selection = True
                sound.Play(DAY_SET_WAV)
                time.sleep(PAUSING_BETWEEN_AUDIO_FILE_DURATION)
                #indicate switch from days to hours
                sound.Play(SET_HOUR_WAV)
                        
                #listen for user input
                c = readchar.readchar() 

        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()


        

            
        

################################################################################
main()
################################################################################
