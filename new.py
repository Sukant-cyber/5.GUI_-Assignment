# Install Required Libraries
import tkinter as tk
# from tkinter import *
from tkinter import ttk

def on_button_click():
    label.config(text="Button Clicked!")

def on_radio_change():
    radio_state = radio_var.get()
    label.config(text=f"Radio state: {radio_state}")

def on_dropdown_select(event):
    selected_item = dropdown_var.get()
    label.config(text=f"Selected item: {selected_item}")

# Create main application window
root = tk.Tk()
root.title("GUI Prototype")

# Set Window-Size
root.geometry("400x200")

# Create a style for the Notebook
# style = ttk.Style()
# style.configure("TNotebook", tabposition="wn", padding=5)

# Create tab control
tab_control = ttk.Notebook(root)

# Tab 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")



# Add widgets to Tab 1
button = tk.Button(tab1, text="Click Me!", command=on_button_click, fg="Black", bg="Light Blue", font=("Ariel", 10))
button.pack(pady=10)

# Tab 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")

# Add widgets to Tab 2
radio_var = tk.StringVar()
radio_var.set("Off")

radio_button1 = tk.Radiobutton(tab2, text="On", variable=radio_var, value="On", command=on_radio_change)
radio_button1.pack()

radio_button2 = tk.Radiobutton(tab2, text="Off", variable=radio_var, value="Off", command=on_radio_change)
radio_button2.pack()

# Tab 3
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Tab 3")

# Add widgets to Tab 3
dropdown_var = tk.StringVar()
dropdown_var.set("Spotify")

dropdown_menu = tk.OptionMenu(tab3, dropdown_var, "Spotify", "Chrome", "Power Point")
dropdown_menu.pack()

# Label to display output
label = tk.Label(root, text="Output will appear here", font=("Arial", 14))
label.pack(pady=20)

# Pack the tab control
tab_control.pack(expand=5, fill="both")

# Start the GUI event loop
root.mainloop()
