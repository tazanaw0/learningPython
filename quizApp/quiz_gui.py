from tkinter import * ##Library used to develop GUI + interface to the Tk GUI toolkit

#Tk(screenName=None, baseName=None, className='Tk', useTk=1)
#Variable that holds and store our first window
q = Tk() 

#Sets the title and dimensions of our first window
q.title('2Min Quiz')
q.geometry('350x200')

#Create buttons
start_button = Tk.Button(q, text='Start', width = 25, command = start_quiz)
stop_button = Tk.Button(q, text='Stop', width = 25, command=q.destroy)
#Infinite loop that runs until an enduser interacts w/ gui 
q.mainloop()

start_label = Tk.label(q, text='Welcome to 2Min Quiz App')
#Changes label (welcome msg) in main window once a user clicks start button
def start_quiz(): 
    start_label.config(text='Quiz starting...')


start_label.pack()#Places our text in gui window
start_button.pack() #Places button in the center of our gui window 
stop_button.pack()#Places button in the center of our gui window 