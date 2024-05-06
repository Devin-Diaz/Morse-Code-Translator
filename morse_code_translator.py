import tkinter as tkinter

# english : morse code
engl_to_morse_map = {
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

# morse code : english
morse_to_engl_map = {morse: char for char, morse in engl_to_morse_map.items()}


# business logic
def translate_to_morse():
    text = text_input_engl_to_morse.get().upper()  # Convert input to uppercase
    translation = ''
    for char in text:
        if char in engl_to_morse_map:
            translation += engl_to_morse_map[char] + ' '
    translation_output_1.config(text=translation)

def translate_to_english():
    text = text_input_morse_to_engl.get().strip().split(' ')  # Split by spaces
    translation = ''
    for morse_char in text:
        if morse_char in morse_to_engl_map:
            translation += morse_to_engl_map[morse_char]
    translation_output_2.config(text=translation)

def clear_text_1():
    text_input_engl_to_morse.delete(0, tkinter.END)
    translation_output_1.config(text='')

def clear_text_2():
    text_input_morse_to_engl.delete(0, tkinter.END)
    translation_output_2.config(text='')


# entire window specs
app = tkinter.Tk()
app.title('English/Morse Code Translator')
app.geometry('1100x600')
app.configure(background='grey26')


# main header
header = tkinter.Label(app, text='Morse Code Translator',
                        background='grey26', 
                        font=('Times New Roman', 35, 'bold'),
                        foreground='hot pink')

header.pack(pady=(70, 0))



# English to Morse Code section
english_to_morse_label = tkinter.Label(app, text='English To Morse Code',
                                      background='grey26', 
                                      font=('Times New Roman', 25, 'bold'),
                                      foreground='white smoke')

english_to_morse_label.place(x=65, y=190)

text_input_engl_to_morse = tkinter.Entry(app, font=('Times New Roman', 14), 
                                         width=40, 
                                         background='bisque')

text_input_engl_to_morse.place(x=50, y=250)

english_to_morse_button = tkinter.Button(app, text='TRANSLATE', 
                                         command=translate_to_morse,
                                         font=('calibri', 10, 'bold', 'underline'), 
                                         background='#4CAF50',
                                         width=11, height=2)

english_to_morse_button.place(x=90, y=300)

clear_button_1 = tkinter.Button(app, text='CLEAR', 
                                command=clear_text_1,
                                font=('calibri', 10, 'bold', 'underline'), 
                                background='#f44336',
                                width=11, height=2)

clear_button_1.place(x=280, y=300)

translation_output_1 = tkinter.Label(app, 
                                     font=('Calibri', 20),
                                     foreground='white smoke',
                                     background='black')

translation_output_1.place(x=70, y=380)


# Morse to English section
morse_to_engl_label = tkinter.Label(app, 
                                    text='Morse Code To English',
                                    background='grey26', font=('Times New Roman', 25, 'bold'),
                                    foreground='white smoke')

morse_to_engl_label.place(x=725, y=190)


text_input_morse_to_engl = tkinter.Entry(app, font=('Times New Roman', 14), width=40, background='bisque')
text_input_morse_to_engl.place(x=710, y=250)

morse_to_engl_button = tkinter.Button(app, text='TRANSLATE', 
                                      command=translate_to_english,
                                      font=('calibri', 10, 'bold', 'underline'), 
                                      background='#4CAF50',
                                      width=11, height=2)

morse_to_engl_button.place(x=725, y=300)

clear_button_2 = tkinter.Button(app, text='CLEAR', 
                                command=clear_text_2,
                                font=('calibri', 10, 'bold', 'underline'), 
                                background='#f44336',
                                width=11, height=2)

clear_button_2.place(x=915, y=300)

translation_output_2 = tkinter.Label(app, 
                                    font=('Calibri', 20),
                                    foreground='white smoke',
                                    background='black')

translation_output_2.place(x=650, y=380)  



# rules labels
rules_label = tkinter.Label(text='for morse code use a space between letters and use / for space between words | . & - chars for morse', 
                            background='black', 
                            foreground='white smoke', 
                            font=('Calibri', 12))

rules_example = tkinter.Label(text='e.g: hi me == .... .. / -- .', 
                            background='black', 
                            foreground='white smoke', 
                            font=('Calibri', 12))

rules_label.pack(pady=(400, 0))  
rules_example.pack(pady=(0, 0))  

#start app
app.mainloop()
