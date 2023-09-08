# Import necessary libraries
import googletrans
import textblob
from tkinter import *
from tkinter import ttk,messagebox

# Create the tkinter root window
root = Tk()
root.title("Text translator") 
root.geometry("950x480")
root.config(bg="Gray")

# Define a function to perform translation
def translate_it():

    #Delete any previous translation
    dest_txt.delete(1.0, END)

    # Get Languages from Dictionary Keys
    try:
        # Get the original language key
        for key,value in languages.items():
            if (value == comb_sor.get()):
                original_language_key = key

        # Get the translated language key
        for key,value in languages.items():
            if (value == comb_dest.get()):
                translated_language_key = key

        # Turn original text into Textblob
        words = textblob.TextBlob(sor_txt.get(1.0, END))

        # Translate Text
        words= words.translate(from_lang=original_language_key, to=translated_language_key)

        # Display translated text to screen
        dest_txt.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator",e)

# Function to clear text
def clear():
    sor_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)



# Language list
languages = googletrans.LANGUAGES
languages_list = list(languages.values())

# Labels
lab_txt=Label(root, text="Translate from", font=("Verdana", 15, "bold"), bg="Gray")
lab_txt.place(x=130,y=55,height=55,width=180)

lab_txt1=Label(root,text="Translate to",font=("Verdana", 15, "bold"), bg="Gray")
lab_txt1.place(x=580,y=55,height=55,width=180)

# Frame
frame = Frame(root).pack(side=BOTTOM)

# Combobox for selecting source and destination languages
comb_sor = ttk.Combobox(root,value=languages_list)
comb_sor.place(x=150,y=100)
comb_sor.set("Select Language")

comb_dest = ttk.Combobox(root,value=languages_list)
comb_dest.place(x=600,y=100)
comb_dest.set("Select Language")

# Source text field
sor_txt=Text(root,font="Times",bg="White",wrap=WORD)
sor_txt.place(x=100,y=130,width=290,height=139)

# Destination text field
dest_txt=Text(root,font="Times",bg="White",wrap=WORD)
dest_txt.place(x=550,y=130,width=290,height=139)

# Translate button
translate=Button(root,text="Translate",font=("Roboto",15,"bold"),activebackground="gray", command = translate_it)
translate.place(x=410,y=320)

# Clear button
clear_button = Button(root, text="Clear",font=("Roboto",15,"bold"),activebackground="gray", command = clear)
clear_button.place(x=430,y=380)

# Start the Tkinter main loop
root.mainloop()