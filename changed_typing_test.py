from tkinter import * 
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading


#Functionality Part
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0
def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    accuracy_percent_label.config(text=str(accuracy)+'%')


def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time,elapsedtimeinminutes
    time=0
    elapsedtimeinminutes=0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')




#GUI 

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1000x735+200+10')
root.configure(bg="")
root.resizable(0,0)
root.overrideredirect(True)

mainframe=Frame(root,bd=4,bg="gray16")
mainframe.grid()

titleframe=Frame(mainframe,bg='black')
titleframe.grid()

titleLabel=Label(titleframe,text='Typing Hercules',font=('castellar',24,'bold'),bg='gray16',fg='ivory1',width=38,bd=10)
titleLabel.grid(pady=5)

paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=[
                'The Times Group established Bennett University in 2016 with a vision to provide quality education and establish itself as one of the best private universities in India to impart interdisciplinary education. It was established by the Act of the State Legislature of Uttar Pradesh as a private university.',
                'The six schools with 30+ programs and 70+ leading specialisations in Engineering, Management, Media, Law and Liberal Arts have positioned it as one of the top universities in India. This has made it a sought-after destination for fortune companies and leading corporates in a short period, picking talents with prominent placement records.',
                'Realize dream career options in Computer Science Engineering with specializations on AI, Blockchain, Cyber-Security, Data-Science, Gaming & Virtual-Reality, Robotics & Automation, DevOps, Full-Stack and Cloud-Computing. World Class Program with Flexible Credit System with Honors-Minors-Electives, Top notch faculty, Industry Internship options, Stellar placements with average of more than 8 Lac Per Annum',
                'Project Based Learning resulting in Public Project Showcase events and opens the doors of top global universities for pursuing higher education like Carnegie Mellon University, Pittsburgh, NYU Tandon School of Engineering, Northeastern University and many more. The entrepreneurial ecosystem at University have inspired students to launch startups like C-Safe Key, Travelsey, Savart, InstaDapp, and many more.',
                'The specializations introduced in the B.Tech. CSE curriculum not only helps the students to understand the core of computer science engineering but also provides an exposure to the new tools and technologies being used in the popular domains.',
                'This specialization will help students to understand how machines can be made intelligent to act like humans for performing tasks like decision making, performing analysis, extracting insights from data, among others. The basics of model and algorithm development for multiple applications like image processing, pattern recognition, natural language processing etc., are covered in this specialization.',
                'The courses offered as a part of this specializations help the students to gather knowledge about the cloud architecture, services provided, security issues, etc. This specialization helps the students to understand the mathematics behind data science, statistical methods that are utilized for extracting useful information from big data. The specialization offers courses to understand tools for analysis of data and various algorithms to gain useful insights from structured and unstructured data.',
                'This specialization provides exposure to the students about the latest trend in the industry for accelerating the processes of design, development, and deployment of the products. Students learn about the agile methodology, compliance policies, performance metrics, security concerns, etc.',
                'This specialization help students to learn about different frameworks and build professional applications from scratch. Learners get to know about the end-to-end development of cross-platform web and mobile solutions.This specialization offers courses that help the students to understand information, network and system security, the privacy of big data, security in IoT and mobile devices, vulnerabilities, etc.',
                'This specialization offers courses that make the students familiar with the popular terms of this technology like Bitcoin, smart contracts, Hyperledger, and also understand the application areas of this technology.',
                'In this specialization, students get an opportunity to interact with hardware and software bots. They are exposed to designing and developing them based on the provided requirements for a particular application or problem at hand. The courses offer the required knowledge about kinematics, dynamics, and control, automation architecture, deployment, security, etc.',
                'This specialization helps the students to understand computer graphics, game engines, game mechanics, animation, rendering techniques, and the requisite knowledge of the latest tools and technologies like AR and VR.'
                ]

random.shuffle(paragraph_list)

label_paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'),bg='grey26',fg='white')
label_paragraph.grid(row=0,column=0)

textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea=Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word',state=DISABLED,fg='black',bg='gray69')
textarea.grid()

frame_output=Frame(mainframe,bg='gray16')
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',13,'bold'),fg='yellow',bg='gray16')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',13,'bold'),fg='red',bg='gray16')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(frame_output,text='WPM',font=('Tahoma',13,'bold'),fg='goldenrod3',bg='gray16')
wpm_label.grid(row=0,column=8,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
wpm_count_label.grid(row=0,column=9,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',13,'bold'),fg='limegreen',bg='gray16')
totalwords_label.grid(row=0,column=4,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
totalwords_count_label.grid(row=0,column=5,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',13,'bold'),fg='red',bg='gray16')
wrongwords_label.grid(row=0,column=6,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
wrongwords_count_label.grid(row=0,column=7,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',13,'bold'),fg='lightseagreen',bg='gray16')
accuracy_label.grid(row=0,column=10,padx=5)

accuracy_percent_label=Label(frame_output,text='0',font=('Tahoma',13,'bold'),bg='gray16',fg='white')
accuracy_percent_label.grid(row=0,column=11,padx=5)

#buttons
buttons_Frame=Frame(mainframe,bg='gray16')
buttons_Frame.grid(row=4,column=0)

startButton=ttk.Button(buttons_Frame,text='Start',command=start)
startButton.grid(row=0,column=0,padx=10)

resetButton=ttk.Button(buttons_Frame,text='Reset',state=DISABLED,command=reset)
resetButton.grid(row=0,column=1,padx=10)

exitButton=ttk.Button(buttons_Frame,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=2,padx=10)

#keyboard layout
keyboard_frame=Frame(mainframe,bg='gray16')
keyboard_frame.grid(row=5,column=0)

frame1to0=Frame(keyboard_frame,bg='gray16')
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2=Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3=Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4=Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5=Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6=Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7=Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8=Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9=Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label0=Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5)
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

frameqtop=Frame(keyboard_frame,bg='gray16')
frameqtop.grid(row=1,column=0,pady=3)
labelQ=Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelW=Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelE=Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelR=Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelT=Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelY=Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelU=Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelI=Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelO=Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelP=Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame,bg='gray16')
frameatol.grid(row=2,column=0,pady=3)
labelA=Label(frameatol,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelS=Label(frameatol,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelD=Label(frameatol,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelF=Label(frameatol,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelG=Label(frameatol,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelH=Label(frameatol,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelJ=Label(frameatol,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelK=Label(frameatol,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelL=Label(frameatol,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameztom=Frame(keyboard_frame,bg='gray16')
frameztom.grid(row=3,column=0,pady=3)
labelZ=Label(frameztom,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelX=Label(frameztom,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelC=Label(frameztom,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelV=Label(frameztom,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelB=Label(frameztom,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelN=Label(frameztom,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelM=Label(frameztom,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

spaceFrame=Frame(keyboard_frame,bg='gray16')
spaceFrame.grid(row=4,column=0,pady=3)

labelSpace=Label(spaceFrame,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
labelSpace.grid(row=0,column=0)

def changeBG(widget):
    widget.config(bg='grey')
    widget.after(100,lambda :widget.config(bg='black'))


label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]

space_label=[labelSpace]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))


for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))

root.bind('<space>',lambda event:changeBG(space_label[0]))

root.mainloop()