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
question_label = Label(q, text='') #Placeholder variable for questions
question_label.pack() # Places label in center of gui window 

#List of questions that we'll cycle through as the user interacts w/ gui. 
Questions = {
     0 :("Question 1: Which out of the following is used to protect data in transit?", ['A: SSL/TLS', 'B: Full-Disk Encryption', 'C: Switch', 'D: Applying Permissions'], 'A: SSL/TLS'),
     1 :("Question 2: What can organizations do to ensure compliance with local laws regarding data at rest?", ['A: Anually skim through regulations and laws', 'B: Constantly monitor where their data is stored', 'C: ', 'D: '], 'A: Anually skim through regulations and laws'), 
     2 :("Question 3: What is used to protect sensitive information on receipts?", ['A: Tokenization', 'B: Hashing', 'C: Masking', 'D: Encryption']  )
}
#Establishes and associates a number to each question, allowing us to keep track of questions. 
current_question = 0 
#Keeps track of how many answers are right
score = 0 


#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz(): 
    opening_label.config(text='You GOT this')
    question_label.config(text=Questions[current_question])
    #Calls function to 'pack' or display buttons once user clicks 'start'
    show_buttons()

# If number of questions are greater than 0, replace the question_label with a question from our list. 
def show_next_question(): 
    global current_question #global tag allowing var to be modified w/ in function
    global selected_answer ##stopping point 

    if current_question < len(Questions)-1:
        current_question += 1
        question_label.config(text= Questions[current_question])
    else:
        Next_button.config(state='disabled')

#If the number associated with the question is > 0 (Any question but the first), subtract one (go back) and print the question associated with that number. 
def show_previous_question():
    global current_question
    if current_question > 0:
        current_question -=1
        question_label.config(text=Questions[current_question])
        Next_button.config(state="normal")
    else:
        Previous_button.config(state='disabled') #Disables previous button if we are at first question

#Places buttons in gui, when function is called upon 
def show_buttons(): 
    Next_button.pack(side=RIGHT)
    Previous_button.pack(side=LEFT)

#Create buttons
start_button = Button(q, text='Start', width = 25, command = start_quiz)
start_button.pack() #Places button in the center of our gui window 
stop_button = Button(q, text='Stop', width = 25, command=q.destroy)
stop_button.pack()#Places button in the center of our gui window 
Next_button = Button(q, text='Next Question', width = 10, command=show_next_question) #Button user interacts w/ to access other questions 
Previous_button= Button(q, text='Previous Question', width = 10, command=show_previous_question) #Button user interacts w/ to access previous question

#All code stops here, nothing beyond this point is ran.
#Infinite loop dependent on user interactions with gui to stop. 
q.mainloop()



 
