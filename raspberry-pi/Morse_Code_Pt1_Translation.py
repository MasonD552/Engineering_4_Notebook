# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = ""
    for letter in text:
        if letter == " ":
            morse_code += "/"  # Use '/' to represent word breaks
        elif letter == "-":
            return "-q"  # If the user types '-q', exit the program
        elif letter.upper() in MORSE_CODE:
            morse_code += MORSE_CODE[letter.upper()] + " "  # Translate letters to Morse code with spaces
        else:
            morse_code += letter + " "  # Keep non-alphabet characters as they are with a space
    return morse_code

# Main loop to accept user input and display Morse code
while True:
    user_input = input("Enter text to translate to Morse code or type -q to Exit: ")
    morse_result = text_to_morse(user_input)
    
    if morse_result == "-q":
        print("Exiting the Morse code translator.")
        break
    else:
        print("Morse Code:", morse_result)
