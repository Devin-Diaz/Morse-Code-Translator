import tkinter as tkinter

# english : morse code
morse_code_map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
    ' ': '/'
}


def translate_to_morse():
    text = user_text_input.get().upper()  # Convert input to uppercase since our dictionary is in uppercase
    translation = ''
    for char in text:
        if char in morse_code_map:
            translation += morse_code_map[char] + ' '
    translation_output.config(text=translation)

def clear_text():
    user_text_input.delete(0, tkinter.END)
    translation_output.config(text='')

# entire window specs
app = tkinter.Tk()
app.title('English/Morse Code Translator')
app.geometry('1100x600')
app.configure(background = 'deep sky blue4')


english_to_morse_label = tkinter.Label(app, 
                        text = 'English To Morse Code',
                        background = 'grey65',
                        font = ('Times New Roman', 20, 'bold'))


english_to_morse_label.place(x = 100, y = 110)


user_text_input = tkinter.Entry(app, font = ('Times New Roman', 14) , width = 40, background = 'bisque2')
user_text_input.place(x = 50, y= 175)



translate_button = tkinter.Button(app, text = 'TRANSLATE', 
                   command = translate_to_morse,
                   font = ('calibri', 10, 'bold', 'underline'),
                   background = 'green3')

translate_button.place(x = 90, y = 230)


clear_button = tkinter.Button(app, text='CLEAR', 
                command=clear_text,
                font = ('calibri', 10, 'bold', 'underline'),
                background = 'hot pink')


clear_button.place(x = 200, y = 230)

# Label to display the translation
translation_output = tkinter.Label(app, text='', font=('Arial', 14))
translation_output.pack(pady=20)






app.mainloop()

