import random
import tkinter as tk
from PIL import Image, ImageTk

def play_game():      
    user_choice = user_var.get()
    computer_choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    computer_choice_key = random.choice(list(computer_choices.keys()))
    computer_choice = computer_choices[computer_choice_key]

    result, color, button_colour = determine_winner(user_choice, computer_choice_key)

    messagebox = tk.Toplevel(root)
    messagebox.title("Result")
    messagebox.geometry("200x100")
    messagebox.configure(bg=color)
 
    result_label = tk.Label(messagebox, text=f"Computer Selected: {computer_choice}\n", bg=color, font=("Arial", 12))
    result_label.pack()

    # Create a separate label for the result variable with bold font
    result_text_label = tk.Label(messagebox, text=result, bg=color, font=("Arial", 17, "bold underline"))
    result_text_label.pack()

    # Create a button to close the result window
    close_button = tk.Button(messagebox, text="Close", command=messagebox.destroy,bg=button_colour,fg="white")
    close_button.pack()


def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!", "#add8e6","blue"  # Light blue
    elif (user == 'p' and computer == 'r') or (user == 'r' and computer == 's') or (user == 's' and computer == 'p'):
        return "You win!", "#90ee90","green"  # Light green
    else:
        return "You lose!", "#FF4A4A","red"  # Light red

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("300x300")

# Define colors
bg_color = "#fffdd0"  
button_bg_color = "#FFFF00"
button_fg_color = "black"

# Set background color
root.configure(bg=bg_color)

# Create a label and radio buttons for user input
label = tk.Label(root, text="Choose:", bg=bg_color, font=("Arial", 14, "bold underline"))
label.pack()

user_var = tk.StringVar()

# Use image paths for radio button choices
rock_img = Image.open(r"rock.png").resize((50, 50))
rock_photo = ImageTk.PhotoImage(rock_img)

paper_img = Image.open(r"paper.png").resize((50, 50))
paper_photo = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open(r"seasors.png").resize((50, 50))
scissors_photo = ImageTk.PhotoImage(scissors_img)

cissors_img = Image.open(r"Screenshot 2024-02-07 133149.png").resize((50, 50))
cissors_photo = ImageTk.PhotoImage(cissors_img)

rock_button = tk.Radiobutton(root, image=rock_photo, variable=user_var, value="r", bg=bg_color)
rock_button.image = rock_photo  # Keep a reference to avoid garbage collection
rock_button.pack()

paper_button = tk.Radiobutton(root, image=paper_photo, variable=user_var, value="p", bg=bg_color)
paper_button.image = paper_photo  # Keep a reference to avoid garbage collection
paper_button.pack()

scissors_button = tk.Radiobutton(root, image=scissors_photo, variable=user_var, value="s", bg=bg_color)
scissors_button.image = scissors_photo  # Keep a reference to avoid garbage collection 
scissors_button.pack() 

cissors_button = tk.Radiobutton(root, image=cissors_photo, variable=user_var, value="s", bg=bg_color)
cissors_button.image = cissors_photo  # Keep a reference to avoid garbage collection
cissors_button.pack()

# Create a button to play the game
play_button = tk.Button(root, text="Play", command=play_game, bg=button_bg_color, fg=button_fg_color, font=('Arial',12,'bold'))
play_button.pack()

# Start the main loop
root.mainloop()
