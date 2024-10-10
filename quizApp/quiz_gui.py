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

#Var to hold/store user's selected answer
selected_answer = StringVar()

#Create placeholder for radio buttons 
radio_buttons = []

#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz():
    global radio_buttons 
    opening_label.config(text='You GOT this')
    question_label.config(text=Questions[current_question][0]) #Gets first value from our Question dictionary 
    #Calls function to 'pack' or display buttons once user clicks 'start'
    show_buttons() #Show navigation buttons
    for i in range(4):
        rb = Radiobutton(q, text='', variable=selected_answer, value='')
        rb.pack()
        radio_buttons.append(rb)

# If number of questions are greater than 0, replace the question_label with a question from our list. 
def show_next_question(): 
    global current_question #global tag allowing var to be modified w/ in function
    if current_question < len(Questions)-1:
        #Increment quesiton index 
        current_question += 1
        #Update question label 
        question_label.config(text= Questions[current_question][0]) #Grabs the first value from each index in our dictionary 
        
        #Update radio buttons 
        for i, rb in enumerate(radio_buttons):
            rb.config(text=Questions[current_question][1][i])
    
    else:
        #Disable the 'next' button when no more questions
        Next_button.config(state='disabled')

#Updates answers choices as each question changes 
def update_answer_choices():
    answer_choices = Questions.pop() ##Check to see how this works w/ the for loop below, it may only pop the end of the entire dictionary 
    
    #Update radio buttons for answer choices 
    for i, choice in enumerate(answer_choices):
        radio_buttons[i].config(text = choice, value = choice)

#If the number associated with the question is > 0 (Any question but the first), subtract one (go back) and print the question associated with that number. 
def show_previous_question():
    global current_question
    if current_question > 0:
        current_question -=1
        question_label.config(text=Questions[current_question][0])#Grabs the first value from each index in our dictionary 
        Next_button.config(state="normal")

        #Update radio buttons 
        for i, rb in enumerate(radio_buttons):
            rb.config(text=Questions[current_question][1][i])
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

#Places buttons in gui, when function is called upon 
def show_buttons(): 
    Next_button.pack(side=RIGHT)
    Previous_button.pack(side=LEFT)

#Create buttons
start_button = Button(q, text='Start', width = 25, command = start_quiz)
start_button.pack() #Places button in the center of our gui window 
stop_button = Button(q, text='Stop', width = 25, command=q.destroy)
stop_button.pack()#Places button in the center of our gui window 
Next_button = Button(q, text='Next Question', width = 10, command=lambda: [check_answer()]) #Button user interacts w/ to access other questions and see the results of their answer choice
Previous_button= Button(q, text='Previous Question', width = 10, command=show_previous_question) #Button user interacts w/ to access previous question

#All code stops here, nothing beyond this point is ran.
#Infinite loop dependent on user interactions with gui to stop. 
q.mainloop()



 
