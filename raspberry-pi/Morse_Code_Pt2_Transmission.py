#type:ignore
import board
import time
import digitalio

# Dictionary representing the morse code chart
MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}

# Define LED pin
led_pin = board.GP15  # LED PIN = GP15
led = digitalio.DigitalInOut(led_pin)  # Define LED on Board
led.direction = digitalio.Direction.OUTPUT

# Morse code timing
modifier = 0.25
dot_time = 1 * modifier
dash_time = 3 * modifier
between_taps = 1 * modifier
between_letters = 3 * modifier
between_words = 7 * modifier

# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = ""
    for letter in text:
        if letter == " ":
            morse_code += "/"
        elif letter == "-q":
            return "-q"
        elif letter.upper() in MORSE_CODE:
            morse_code += MORSE_CODE[letter.upper()] + " "
        else:
            morse_code += letter + " "
    return morse_code

# Function to flash LED based on Morse code
def flash_morse_code(morse_message):
    for character in morse_message:
        if character == '.':
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        elif character == '-':
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        elif character == ' ':
            time.sleep(between_letters)
        elif character == '/':
            time.sleep(between_words)

while True:
    user_input = input("Enter text to translate to Morse code or type -q to Exit: ")
    if user_input == "-q":
        print("Exiting the Morse code translator.")
        break
    else:
        morse_result = text_to_morse(user_input)
        print("Morse Code:", morse_result)
        flash_morse_code(morse_result)
