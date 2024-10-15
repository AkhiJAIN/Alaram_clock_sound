import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\vanak\OneDrive\Desktop\NEW PYTH\projeect\Every Night Of The Week - Everet Almond.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")

      
        if current_time == alarm_time:
            print("Time to wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

        time.sleep(1)  

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)







#with explanantion need if

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\vanak\OneDrive\Desktop\NEW PYTH\projeect\Every Night Of The Week - Everet Almond.mp3"
    
    pygame.mixer.init()  # Initialize the mixer for sound
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        
        if current_time == alarm_time:
            print("Time to wake up!")
            pygame.mixer.music.load(sound_file)  # Load the sound file
            pygame.mixer.music.play()  # Play the sound
            
            # Wait for the sound to finish playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
