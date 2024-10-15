from tkinter import * ##Library used to develop GUI + interface to the Tk GUI toolkit

#Tk(screenName=None, baseName=None, className='Tk', useTk=1)
#Variable that holds and store our first window
q = Tk() 

#Sets the title and dimensions of our first window
q.title('2Min Quiz')
q.geometry('350x200')

#Text presented to user when they open a window 
opening_label = Label(q, text='Welcome to 2Min Quiz App')
opening_label.pack() #Places label in center of gui window

#List of questions that we'll cycle through as the user interacts w/ gui. 
Questions = {
     0 :("Question 1: Which out of the following is used to protect data in transit?", 
        ['A: SSL/TLS', 'B: Full-Disk Encryption', 'C: Switch', 'D: Applying Permissions'], 'A: SSL/TLS'),
     1 :("Question 2: What can organizations do to ensure compliance with local laws regarding data at rest?", 
        ['A: Anually skim through regulations and laws', 'B: Constantly monitor where their data is stored', 'C: ', 'D: '], 'A: Anually skim through regulations and laws'), 
     2 :("Question 3: What is used to protect sensitive information on receipts?", 
        ['A: Tokenization', 'B: Hashing', 'C: Masking', 'D: Encryption'], 'A: Tokenization')
}
#Establishes and associates a number to each question, allowing us to keep track of questions. 
current_question = 0 

#Keeps track of how many answers are right
score = 0 

#Var to store user's answer for each question 
user_answer = [NONE] * len(Questions) #Initalized with none for however many questions we have. 

#Var to hold/store user's selected answer
selected_answer = StringVar()

#Create placeholder for radio buttons 
radio_buttons = []

#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz():
    global radio_buttons
    start_button.pack_forget() #Hide start button once user clicks start
    opening_label.config(text='Good luck!')#Updates welcoming message @ top of window
    question_label.config(text=Questions[current_question][0]) #Gets first value from our Question dictionary 
    selected_answer.set(None)#Clears answer choices once user starts quiz
    show_buttons() #Show navigation buttons
    if not radio_buttons: #Only create the buttons once
        for i in range(4):
            rb = Radiobutton(q, text=Questions[current_question][1][i], variable=selected_answer, value='') 
            rb.pack()
            radio_buttons.append(rb) #Keeps track of created buttons 
    update_answer_choices()


# If number of questions are greater than 0, replace the question_label with a question from our list. 
def show_next_question(): 
    global current_question #global tag allowing var to be modified w/ in function
    if current_question < len(Questions)-1:
        #Increment quesiton index 
        current_question += 1
        #Update question label 
        question_label.config(text= Questions[current_question][0]) #Grabs the first value from each index in our dictionary 
        update_answer_choices()  
    else:
        #Disable the 'next' button when no more questions
        Next_button.config(state='disabled')

#Sets radio buttons answer choices by referencing Questions dictionary. 
def update_answer_choices():
    answer_choices = Questions[current_question][1]  # Get the answer choices
    for i, choice in enumerate(answer_choices):
        radio_buttons[i].config(text=choice, value=choice)  # Update text and value for each radio button

#If the number associated with the question is > 0 (Any question but the first), subtract one (go back) and print the question associated with that number. 
def show_previous_question():
    global current_question
    if current_question > 0:
        current_question -=1
        question_label.config(text=Questions[current_question][0])#Grabs the first value from each index in our dictionary 
        Next_button.config(state="normal")
        update_answer_choices()
    else:
        Previous_button.config(state='disabled') #Disables previous button if we are at first question

#Function to check user's answer
def check_answer(): 
    global score, current_question
    #Get users answer  
    user_answer = selected_answer.get()

    #check if it's correct
    if user_answer == Questions[current_question][2]:
        score +=1

    #Move to next question if avail 
    show_next_question()

question_label = Label(q, text='') #Placeholder variable for questions
question_label.pack() # Places label in center of gui window 

#Create buttons
start_button = Button(q, text='Start', width = 25, command = start_quiz)
stop_button = Button(q, text='Stop', width = 25, command=q.destroy)
stop_button.pack(side=BOTTOM)#Places button in the center of our gui window
start_button.pack(side=BOTTOM) #Places button in the center of our gui window  
Next_button = Button(q, text='Next Question', width = 10, command=lambda: [check_answer()]) #Button user interacts w/ to access other questions and see the results of their answer choice
Previous_button= Button(q, text='Previous Question', width = 10, command=show_previous_question) #Button user interacts w/ to access previous question
submit_quiz = Button(q, text='Submit', width=25, state='disabled') #Disabled until we can reference function in 'command' to save results to our DB. 
#Places buttons in gui, when function is called upon 
def show_buttons(): 
    Next_button.pack(side=RIGHT)
    Previous_button.pack(side=LEFT)


#All code stops here, nothing beyond this point is ran.
#Infinite loop dependent on user interactions with gui to stop. 
q.mainloop()



 
