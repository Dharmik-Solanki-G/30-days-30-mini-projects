import tkinter as tk

def correct(input_val, ans, options, counter_label):
    if input_val == ans:
        result_label.config(text='Correct answer!', fg='green')
        counter_label.config(text=f'Counter: {counter_label.counter_value + 1}')
        counter_label.counter_value += 1
    else:
        result_label.config(text=f'Incorrect answer! Correct answer is: {ans}', fg='red')

def ask_question(question, options, ans):
    question_label.config(text=question)
    for i, option in enumerate(options):
        radio_buttons[i].config(text=option, value=option)
    selected_option.set(None)
    result_label.config(text='', bg='black', fg='white', font=('Helvetica', 10, 'bold'))

def next_question():
    current_question_index = next_question.question_index
    if current_question_index < len(questions):
        ask_question(questions[current_question_index], options[current_question_index], answers[current_question_index])
        next_question.question_index += 1
    else:
        question_frame.destroy()
        final_frame = tk.Frame(root, bg='black')
        final_frame.pack()
        final_counter_label = tk.Label(final_frame, text=f'Final Counter: {counter_label.counter_value}', bg='black', fg='white', font=('Helvetica', 10, 'bold'))
        final_counter_label.pack()

root = tk.Tk()
root.title("Quiz Program")
root.configure(bg='black')

questions = [
    "What is the national animal?",
    "What is the largest country?",
    "What is the largest mammal on Earth?",
    "Which programming language is known for its readability and simplicity?",
    "What is the largest ocean on Earth?"
]

options = [
    ['tiger', 'elephant', 'lion', 'dog'],
    ['india', 'uk', 'usa', 'russia'],
    ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
    ['Java', 'Python', 'C++', 'JavaScript'],
    ['Atlantic Ocean', 'Indian Ocean', 'Southern Ocean', 'Pacific Ocean']
]

answers = ['tiger', 'russia', 'Blue Whale', 'Python', 'Pacific Ocean']

question_frame = tk.Frame(root, bg='black')
question_frame.pack()

question_label = tk.Label(question_frame, text="", bg='black', fg='white', font=('Helvetica', 12, 'bold'))
question_label.grid(row=0, column=0, columnspan=2)

selected_option = tk.StringVar()

radio_buttons = []
for i in range(4):
    radio_button = tk.Radiobutton(question_frame, text="", variable=selected_option, bg='black', fg='white', font=('Helvetica', 10, 'bold'))
    radio_button.grid(row=i+1, column=0, sticky='w')
    radio_buttons.append(radio_button)

result_label = tk.Label(question_frame, text="", bg='black', fg='white', font=('Helvetica', 10, 'bold'))
result_label.grid(row=6, column=0, columnspan=2)

counter_label = tk.Label(question_frame, text="Counter: 0", bg='black', fg='white', font=('Helvetica', 10, 'bold'))
counter_label.grid(row=7, column=0, columnspan=2)
counter_label.counter_value = 0

next_question.question_index = 0
ask_question(questions[0], options[0], answers[0])

def submit_answer():
    correct(selected_option.get(), answers[next_question.question_index - 1], options[next_question.question_index - 1], counter_label)

submit_button = tk.Button(question_frame, text="Submit", command=submit_answer, bg='black', fg='white', font=('Helvetica', 10, 'bold'))
submit_button.grid(row=5, column=0)

next_button = tk.Button(question_frame, text="Next Question", command=next_question, bg='black', fg='white', font=('Helvetica', 10, 'bold'))
next_button.grid(row=5, column=1)

root.mainloop()
