################################################################################
# set_clock.py
# Talaba Pogrebinsky - OCT 2017
# SITATIONS: Honof's Sample_fenu.py gave the basic layout for how my program is structured.
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
def main():
    create_sound_filenames()
    # can use below function for testing
    #verify_sound_filenames()
    create_fenu_globals()
    run_fenu()

################################################################################
# Create the sound objects for the auditory menus and display.
################################################################################
def create_sound_filenames():

    # Declare global variables.
    global INTRO_WAV, SET_DAY_WAV, SET_HOUR_WAV, YOU_SELECTED_WAV, NUMBERS_WAV, DAYS_WAV, AM_WAV, PM_WAV, PRESS_AGAIN_TO_QUIT_WAV,\
        EXITING_PROGRAM_WAV, EXITING_PROGRAM_WAV_DURATION, TMP_FILE_WAV

    # Create  sounds.
    nav_path = "wav_files_provided/miscellaneous_f/"
    num_path = "wav_files_provided/numbers_f/"
    day_path = "wav_files_provided/days_of_week_f/"

    INTRO_WAV = "my_wav_files/Set_day_and_time_f"
    YOU_SELECTED_WAV = nav_path + "you_selected_f.wav"

    NUMBERS_WAV = [num_path + "01_f.wav", num_path + "02_f.wav",
           num_path + "03_f.wav", num_path + "04_f.wav"]

    AM_WAV = nav_path + "AM_f.wav"
    PM_WAV = nav_path + "PM_f.wav"
    SET_HOUR_WAV = nav_path + "Set_hour_f.wav"
    SET_DAY_WAV = nav_path + "Set_day_of_week_f.wav"
    DAYS_WAV = day_path + "monday_f.wav", day_path + "tuesday_f.wav", day_path + "wednesday_f.wav", day_path + "thursday_f.wav", day_path + "friday_f.wav", day_path + "saturday_f.wav", day_path + "sunday_f.wav"
    PRESS_AGAIN_TO_QUIT_WAV = nav_path + "Press_again_to_quit_f.wav"
    EXITING_PROGRAM_WAV = nav_path + "Exiting_program_f.wav"
    EXITING_PROGRAM_WAV_DURATION = 1.09 # in s. 1.09 is accurate but 0.45 saves time.

    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename  for output

################################################################################
# Verify all files can be loaded and played.
# Play all sound files to make sure the paths and filenames are correct and valid.
# The very last sound tested/played should be the sound that plays at startup.
################################################################################
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
def create_fenu_globals():

    # Declare global variables as such.
    global SET_KEY, FORWARD_KEY, BACKWARD_KEY, QUIT_KEY, MINIMAL_HELP_STRING, CURRENT_TIME, CURRENT_DAY 

    # Constants
    # Keystrokes for the keyboard interaction.
    FORWARD_KEY = 'j' 
    BACKWARD_KEY = 'k'
    SET_KEY = '\x20' # space bar
    QUIT_KEY = ';'

    # A bare minimum of text to display to guide the user.
    MINIMAL_HELP_STRING = "Press " + QUIT_KEY + " to quit."

    # Global variables
    CURRENT_TIME = 0    # The current time that is set. (Just an integer for now.)
    
    CURRENT_DAY  = 0     # the current day is set. (Just an integer for now.)

################################################################################
# Run the menu in an endless loop until the user exits.
################################################################################
def run_fenu():

    global CURRENT_TIME
    global CURRENT_DAY 

    #boolean for switching from days to hours
    days_selection = True

    #boolean for switching from hours to minutes
    hours_selection = False

    #booleans for switching from am to pm
    am = True
    pm = False
    
    # Provide a minimal indication that the program has started.
    print(MINIMAL_HELP_STRING)

    
    # Concatenate three audio files to generate the message.
    sound.combine_wav_files(TMP_FILE_WAV, INTRO_WAV, SET_DAY_WAV)
    # Play the concatenated file.
    sound.Play(TMP_FILE_WAV)

    # Get the 2nd keystroke.
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

        # Respond to the user's input.
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


        

        # this now should loop though hours
        if c == BACKWARD_KEY and days_selection == False:

            hours_selection = True
            
            # variable for converting am to pm and vice versa
            convert = False

            if CURRENT_TIME == 0:
                CURRENT_TIME = len(NUMBERS_WAV)-1

                # change from am to pm or vice versa
                convert = True

            else:
                CURRENT_TIME -= 1
           

            print(CURRENT_TIME)
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

        if c == FORWARD_KEY and days_selection == False:

            hours_selection = True

            # variable for converting am to pm and vice versa
            convert = False
            
            # Advance the time, looping back around to the start.
            if (CURRENT_TIME+1) == len(NUMBERS_WAV):
                CURRENT_TIME = 0
                # change from am to pm or vice versa
                convert = True
            else:
                CURRENT_TIME += 1
            
            print(CURRENT_TIME)

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

            if days_selection == True:
                # day is selected 
                days_selection = False

                hours_selection = True

                #indicate switch from days to hours
                sound.Play(SET_HOUR_WAV)

                #listen for user input
                c = readchar.readchar() 

            elif hours_selection = True:

                hours_selection = False

            else:
                sound.Play(EXITING_PROGRAM_WAV)
                break

            # second time being pressed
            if days_selection == False:
                sound.Play(EXITING_PROGRAM_WAV)
                break
            else:
                # disable day conditions
                days_selection = False

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
