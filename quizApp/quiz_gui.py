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
question_label = Label(q, text='Placeholder for current question')
question_label.pack() # Places label in center of gui window 

#List of questions that we'll cycle through as the user interacts w/ gui. 
Questions = ["Question 1: Which out of the following used to protect data in transit?",
             "Question 2: What can organizations do to ensure compliance with local laws regarding data at rest?", 
             "Question 3: What is used to protect sensitive information on receipts?"]
#Establishes and associates a number to each question, allowing us to keep track of questions. 
current_question = 0 


#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz(): 
    opening_label.config(text='Quiz starting...')
    question_label.config(text=Questions[current_question])

#Create buttons
start_button = Button(q, text='Start', width = 25, command = start_quiz)
start_button.pack() #Places button in the center of our gui window 
stop_button = Button(q, text='Stop', width = 25, command=q.destroy)
stop_button.pack()#Places button in the center of our gui window 
Next_question = Button(q, text='Next Question', width = 10) #Button user interacts w/ to access other questions
Next_question.pack()
Previous_question = Button(q, text='Previous Question', width = 10) #Button user interacts w/ to access previous question
Previous_question.pack()
#Infinite loop that runs until an enduser interacts w/ gui 
q.mainloop()



 
