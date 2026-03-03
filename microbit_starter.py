from microbit import *
import music

# Dictionary for decoding Morse
morse_dict = {
    "dot-dash": "A", "dash-dot-dot-dot": "B", "dash-dot-dash-dot": "C", 
    "dash-dot-dot": "D", "dot": "E", "dot-dot-dash-dot": "F", "dash-dash-dot": "G", 
    "dot-dot-dot-dot": "H", "dot-dot": "I", "dot-dash-dash-dash": "J", 
    "dash-dot-dash": "K", "dot-dash-dot-dot": "L", "dash-dash": "M", 
    "dash-dot": "N", "dash-dash-dash": "O", "dot-dash-dash-dot": "P", 
    "dash-dash-dot-dash": "Q", "dot-dash-dot": "R", "dot-dot-dot": "S", 
    "dash": "T", "dot-dot-dash": "U", "dot-dot-dot-dash": "V", 
    "dot-dash-dash": "W", "dash-dot-dot-dash": "X", "dash-dot-dash-dash": "Y", 
    "dash-dash-dot-dot": "Z"
}

current_symbol = ""
message = []

while True:
    # Task 4: Shake to Show Message
    if accelerometer.was_gesture('shake'):
        full_string = "".join(message)
        display.scroll(full_string)
        # Optional: clear message after showing? 
        # message = [] 

    # Task 1 & 3: Button A (Dot)
    if button_a.was_pressed():
        if current_symbol == "":
            current_symbol = "dot"
        else:
            current_symbol += "-dot"
        
        display.show(Image('00000:00000:36963:00000:00000'))
        music.pitch(200)
        sleep(100)
        music.stop()
        display.clear()

    # Task 1 & 3: Button B (Dash)
    if button_b.was_pressed():
        if current_symbol == "":
            current_symbol = "dash"
        else:
            current_symbol += "-dash"
            
        display.show(Image('00300:03630:36963:03630:00300'))
        music.pitch(300)
        sleep(300)
        music.stop()
        display.clear()

    # Task 2 & 3: Logo Touched (Decode)
    if pin_logo.is_touched():
        if current_symbol != "":
            # Look up the letter
            letter = morse_dict.get(current_symbol, "?")
            message.append(letter)
            
            # Feedback
            display.show(letter)
            music.pitch(500)
            sleep(200) # Prevents the "multiple question mark" issue
            music.stop()
            
            # Reset for next letter
            print("Decoded symbol:", current_symbol, "as:", letter)
            current_symbol = ""
            display.clear()
            
    sleep(10) # Small power save
