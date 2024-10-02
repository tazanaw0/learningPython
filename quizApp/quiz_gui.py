from tkinter import * ##Library used to develop GUI + interface to the Tk GUI toolkit

#Tk(screenName=None, baseName=None, className='Tk', useTk=1)
#Variable that holds and store our first window
q = Tk() 

#Sets the title and dimensions of our first window
q.title('2Min Quiz')
q.geometry('350x200')

#Text presented to user when they open a window 
start_label = Label(q, text='Welcome to 2Min Quiz App')
start_label.pack() #Places label in center of gui window
current_question = Label(q, text='Placeholder for current question')
current_question.pack() # Places label in center of gui window 

#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz(): 
    start_label.config(text='Quiz starting...')

#Create buttons
start_button = Button(q, text='Start', width = 25, command = start_quiz)
start_button.pack() #Places button in the center of our gui window 
stop_button = Button(q, text='Stop', width = 25, command=q.destroy)
stop_button.pack()#Places button in the center of our gui window 
Next_question = Button(q, text='Next Question', width = 7) #Button user interacts w/ to access other questions
Next_question.pack()

#Infinite loop that runs until an enduser interacts w/ gui 
q.mainloop()



 
