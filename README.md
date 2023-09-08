# Language-Translation-System-Using-Python
This code creates a GUI application for translating text from one language to another using Google Translate. Users can select source and destination languages, enter text, and click the "Translate" button to get the translation. They can also clear the text fields using the "Clear" button. The translation process is handled by the `googletrans` and `textblob` libraries.

Explanation:

1. **Importing Libraries**: The code starts by importing the necessary libraries:

    - `googletrans` is used for language translation using the Google Translate API.
    - `textblob` is used for processing and translating text.
    - `tkinter` is the standard Python interface for creating GUI applications.
    - `ttk` is used for creating themed tkinter widgets.
    - `messagebox` is used for displaying message boxes in the GUI.

2. **Creating the GUI Window**:
    - `Tk()` creates the main tkinter window.
    - `title` sets the window title to "Text translator."
    - `geometry` sets the dimensions of the window to 950 pixels wide and 480 pixels tall.
    - `config` configures the background color of the window to gray.

3. **Defining Translation Function (`translate_it`) and Clear Function (`clear`)**:
    - `translate_it()` is called when the "Translate" button is clicked. It performs the translation process.
        - It retrieves the selected source and destination languages from the comboboxes.
        - It translates the text entered in the source text field using the `googletrans` library.
        - It displays the translated text in the destination text field.
        - If any errors occur during the translation process, it displays an error message box using `messagebox`.

    - `clear()` is called when the "Clear" button is clicked. It clears the text from both the source and destination text fields.

4. **Creating a Dictionary of Languages**:
    - `googletrans.LANGUAGES` contains language codes as keys and language names as values. It's used to populate the comboboxes with language options.

5. **Creating Labels for Translation Direction**:
    - Labels are created and placed on the GUI to indicate the translation direction (from and to).

6. **Creating a Frame**:
    - A frame is created and packed at the bottom of the root window. Frames are often used to organize and group widgets, but in this code, it's not assigned to a variable.

7. **Creating Comboboxes for Language Selection**:
    - Two comboboxes are created for selecting the source and destination languages.
    - `languages_list` contains a list of available languages to populate the comboboxes.
    - The `set` method sets the default selection in both comboboxes to "Select Language."

8. **Creating Source and Destination Text Fields**:
    - Two text fields are created for entering the source text and displaying the translated text.

9. **Creating Translate and Clear Buttons**:
    - The "Translate" and "Clear" buttons are created with specific text and formatting.
    - The "Translate" button is configured to call the `translate_it` function when clicked.
    - The "Clear" button is configured to call the `clear` function when clicked.

10. **Starting the Tkinter Main Loop**:
    - `root.mainloop()` starts the main event loop of the tkinter application, which handles user interactions and keeps the GUI running.



