from tkinter import *
from tkinter import ttk
import tkinter.messagebox



class atm:

    def __init__(self, root):
       self.root = root
       blank_space = " "
       # by this we get our title in the center
       self.root.title(110 * blank_space + "ATM System")
       self.root.geometry("800x760+280+0")  # this the border size
       self.root.configure(background='gainsboro')

# 0).================================Frame===================================#

       MainFrame = Frame(self.root, bd=20, width=760, height=700, relief=RIDGE)
       MainFrame.grid()
     # in the out put we can able to see the margins or border

       TopFrame = Frame(MainFrame, bd=8, width=730, height=300, relief=RIDGE)
       # this is the topframe under mainframe
       TopFrame.grid(row=2, column=0, padx=12)

       TopFrame1 = Frame(MainFrame, bd=8, width=730, height=300, relief=RIDGE)
       TopFrame1.grid(row=2, column=0, padx=12)
       TopFrame2 = Frame(MainFrame, bd=8, width=730, height=300, relief=RIDGE)
       TopFrame2.grid(row=1, column=0, padx=8)  # lets chnage the frame spacing

       TopFrame2Left = Frame(TopFrame2, bd=5, width=190,
                             height=300, relief=RIDGE)
       # this is the topframe2 left in topframe2
       TopFrame2Left.grid(row=0, column=0, padx=3)

       TopFrame2Mid = Frame(TopFrame2, bd=5, width=200,
                            height=300, relief=RIDGE)
       # this is the middle frame in topframe2
       TopFrame2Mid.grid(row=0, column=1, padx=3)

       TopFrame2Right = Frame(TopFrame2, bd=5, width=190,
                              height=300, relief=RIDGE)
       # this is the topframe2Right in topframe2
       TopFrame2Right.grid(row=0, column=2, padx=3)

       #=============================functions=======================================#

       def enter_Pin():
           pinNo = self.txtReceipt.get("1.0","end-1c")
           if((pinNo == str("2213"))or (pinNo == str("4323"))or (pinNo == str("5982"))):
              self.txtReceipt.delete("1.0",END)

              
              self.txtReceipt.insert(END,'\t\t         ATM' + "\n\n")
                                     
              self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")

              self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' + "\n\n\n\n")

              self.txtReceipt.insert(END,'Balance \t\t\t Request New Pin' + "\n\n\n\n")

              self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")

#7).making button normal enable ============#right button====================#

              self.btnrArrow1=Button(TopFrame2Right, width=160, height=60, state =NORMAL,command=loan,
              image=self.img_arrow_Right).grid(row=0,column =0,padx=2,pady =4)

              self.btnrArrow2=Button(TopFrame2Right, width=160, height=60, state =NORMAL,command=deposit,
              image=self.img_arrow_Right).grid(row=1,column =0,padx=2,pady =4)


              self.btnrArrow3=Button(TopFrame2Right, width=160, height=60, state =NORMAL,
                                     command=request_new_pin,
              image=self.img_arrow_Right).grid(row=2, column =0,padx=2, pady =4)


              self.btnrArrow4=Button(TopFrame2Right, width=160, height=60, state =NORMAL,
                                     command=statement,
              image=self.img_arrow_Right).grid(row=3, column =0,padx=2, pady =4)
#8).WE ARE ENABLING BUTTONS BY CLICKING ENTER BUTTON LEFT SIDE BUTTON ==============#

              self.btnlArrow1=Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=withdrawcash,
              image=self.img_arrow_Left).grid(row=0,column =0,padx=2,pady =4)
       
       
              self.btnlArrow2=Button(TopFrame2Left, width=160, height=60, stat=NORMAL,command=withdrawcash,
              image=self.img_arrow_Left).grid(row=1, column =0, padx=2, pady =4)

       
              self.btnlArrow3=Button(TopFrame2Left, width=160, height=60, state=NORMAL,
                                     command=balance,
              image=self.img_arrow_Left).grid(row=2, column =0, padx=2, pady =4)

       
              self.btnlArrow4=Button(TopFrame2Left, width=160, height=60, state=NORMAL,
                                     command=statement,
              image=self.img_arrow_Left).grid(row=3, column =0, padx=2, pady =4)

           else:
              self.txtReceipt.delete("1.0",END)

              
              self.txtReceipt.insert(END,'Invalid Pin Number' + "\n\n")
               
              

       def clear():
        self.txtReceipt.delete("1.0",END)
        self.btnlArrow1=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image=self.img_arrow_Left).grid(row=0, column =0, padx=2, pady =4)

        self.btnlArrow2=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image=self.img_arrow_Left).grid(row=1, column =0, padx=2, pady =4)

       
        self.btnlArrow3=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image=self.img_arrow_Left).grid(row=2, column =0, padx=2, pady =4)

       
        self.btnlArrow4=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image=self.img_arrow_Left).grid(row=3, column =0, padx=2, pady =4)


        self.img_arrow_Right = PhotoImage(file ="rArrow.png")
        self.btnrArrow1=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
        image=self.img_arrow_Right).grid(row=0, column =0,padx=2, pady =4)

        self.btnrArrow2=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
        image=self.img_arrow_Right).grid(row=1, column =0,padx=2, pady =4)


        self.btnrArrow3=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
        image=self.img_arrow_Right).grid(row=2, column =0,padx=2, pady =4)


        self.btnrArrow4=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
        image=self.img_arrow_Right).grid(row=3, column =0,padx=2, pady =4)

       def insert0():
           value0 = 0
           self.txtReceipt.insert(END,value0)
       def insert1():
           value1 = 1
           self.txtReceipt.insert(END,value1)

       def insert2():
           value2 = 2
           self.txtReceipt.insert(END,value2)
       def insert3():
           value3 = 3
           self.txtReceipt.insert(END,value3)
       def insert4():
           value4 = 4
           self.txtReceipt.insert(END,value4)
       def insert5():
           value5 = 5
           self.txtReceipt.insert(END,value5)

       def insert6():
           value6 = 6
           self.txtReceipt.insert(END,value6)

       def insert7():
           value7 = 7
           self.txtReceipt.insert(END,value7)
       def insert8():
           value8 = 8
           self.txtReceipt.insert(END,value8)
       def insert9():
           value9 = 9
           self.txtReceipt.insert(END,value9)
       def cancel():
           Cancel = tkinter.messagebox.askyesno("ATM","Confirm if you want to cancel")
           Cancel > 0 
           self.root.destroy()
           return
       def withdrawcash():
           enter_Pin()
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.focus_set()

       def loan():
           enter_Pin()
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.insert(END, 'Loan ₹')
           self.txtReceipt.focus_set()
       def deposit():
           enter_Pin()
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.focus_set()

       def request_new_pin():
           enter_Pin()
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.insert(END, '\t\t Welcome To LPU Bank \n')
           self.txtReceipt.insert(END, 'New Pin will be send your home address \n')                          
           self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Balance \t\t\t Request New Pin' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")
           self.txtReceipt.insert(END, '\t\t Thanks for using  LPU Bank \n')

       def balance(): 
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.insert(END, '\t\t Welcome To LPU Bank \n')
           self.txtReceipt.insert(END, '₹1296' +"\n")                        
           self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Balance \t\t\t Request New Pin' + "\n\n\n\n")

           self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")
           self.txtReceipt.insert(END, '\t\t Thanks for using  LPU Bank \n')

       def statement():
           pinNo1 = str(self.txtReceipt.get("1.0", "end-1c"))
           pinNo2 = str(pinNo1)
           pinNo3 = float(pinNo2)
           pinNo4 = float(1296-(pinNo3))
           self.txtReceipt.delete("1.0",END)
           self.txtReceipt.insert(END, '\n\t' + str(pinNo4)+ "\t\t")
                                
           self.txtReceipt.insert(END,'\t\t\t\n\n Account Balance ₹' + str(pinNo4)+ "\n\n\n\n")

           self.txtReceipt.insert(END,'Rent\t\t\t\t ₹1200' + "\n\n")

           self.txtReceipt.insert(END,'Tesco\t\t\t\t ₹79.36' + "\n\n")

           self.txtReceipt.insert(END,'Sainsbury'+'s \t\t\t ₹53.87' + "\n\n")
           self.txtReceipt.insert(END,'Student Loan \t\t\t\t ₹69.72' + "\n\n")
           self.txtReceipt.insert(END,'RupeesLand \t\t\t\t ₹19' + "\n\n")
           

    
    
       #1).=============================widget======================================================#
       self.txtReceipt = Text(TopFrame2Mid, height = 17, width=42, bd=12, font=('arial',9,'bold'))
       self.txtReceipt.grid(row=0, column=0)


       self.img_arrow_Left = PhotoImage(file ="lArrow.png")
       self.btnlArrow1=Button(TopFrame2Left, width=160, height=60, state=DISABLED,command=withdrawcash,
       image=self.img_arrow_Left).grid(row=0, column =0, padx=2, pady =4)
       
       
       self.btnlArrow2=Button(TopFrame2Left, width=160, height=60, state=DISABLED,command=withdrawcash,
       image=self.img_arrow_Left).grid(row=1, column =0, padx=2, pady =4)

       
       self.btnlArrow3=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
                               command=balance,
       image=self.img_arrow_Left).grid(row=2, column =0, padx=2, pady =4)

       
       self.btnlArrow4=Button(TopFrame2Left, width=160, height=60, state=DISABLED,
                               command=statement,
       image=self.img_arrow_Left).grid(row=3, column =0, padx=2, pady =4)

       # here i have to add four times button so due to error it isn't working and these are
       # added in the left side

       #2).=================================right button=======================================#
       self.img_arrow_Right = PhotoImage(file ="rArrow.png")
       self.btnrArrow1=Button(TopFrame2Right, width=160, height=60, state =DISABLED,command=loan,
       image=self.img_arrow_Right).grid(row=0, column =0,padx=2, pady =4)

       self.btnrArrow2=Button(TopFrame2Right, width=160, height=60, state =DISABLED,command=deposit,
       image=self.img_arrow_Right).grid(row=1, column =0,padx=2, pady =4)


       self.btnrArrow3=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
                               command=request_new_pin,
       image=self.img_arrow_Right).grid(row=2, column =0,padx=2, pady =4)


       self.btnrArrow4=Button(TopFrame2Right, width=160, height=60, state =DISABLED,
                               command=statement,
       image=self.img_arrow_Right).grid(row=3, column =0,padx=2, pady =4)

       #3).=============================================pin number button==========================================#
       #this are the pins buttons of the atm system
       
       self.img1 = PhotoImage(file ="one.png")
       self.btn1=Button(TopFrame1, width=160, height=60,command = insert1,
       image=self.img1).grid(row=2, column =0,padx=4, pady =4)

       self.img2 = PhotoImage(file ="two.png")
       self.btn2=Button(TopFrame1, width=160, height=60,command = insert2, 
       image=self.img2).grid(row=2, column =1,padx=4, pady =4)

       self.img3 = PhotoImage(file ="three.png")
       self.btn3=Button(TopFrame1, width=160, height=60,command = insert3, 
       image=self.img3).grid(row=2, column =2,padx=4, pady =4)


       self.imgCE = PhotoImage(file ="cancel.png")
       self.btnCancel=Button(TopFrame1, width=160, height=60,command = cancel,
       image=self.imgCE).grid(row=2, column =3,padx=4, pady =4)
       #4).=====================================******===============================================#
       self.img4 = PhotoImage(file ="four.png")
       self.btn4=Button(TopFrame1, width=160, height=60,command = insert4, 
       image=self.img4).grid(row=3, column =0,padx=4, pady =4)

       self.img5 = PhotoImage(file ="five.png")
       self.btn2=Button(TopFrame1, width=160, height=60,command = insert5, 
       image=self.img5).grid(row=3, column =1,padx=4, pady =4)

       self.img6 = PhotoImage(file ="six.png")
       self.btn6=Button(TopFrame1, width=160, height=60,command = insert6,
       image=self.img6).grid(row=3, column =2,padx=4, pady =4)


       self.imgCl = PhotoImage(file ="clear.png")
       self.btnClear=Button(TopFrame1, width=160, height=60,command=clear,
       image=self.imgCl).grid(row=3, column =3,padx=4, pady =4)

       #5).=====================================******===============================================#
       self.img7 = PhotoImage(file ="seven.png")
       self.btn7=Button(TopFrame1, width=160, height=60,command = insert7, 
       image=self.img7).grid(row=4, column =0,padx=4, pady =4)

       self.img8 = PhotoImage(file ="eight.png")
       self.btn8=Button(TopFrame1, width=160, height=60,command = insert8, 
       image=self.img8).grid(row=4, column =1,padx=6, pady =4)

       self.img9 = PhotoImage(file ="nine.png")
       self.btn9=Button(TopFrame1, width=160, height=60,command = insert9, 
       image=self.img9).grid(row=4, column =2,padx=6, pady =4)


       self.imgEnter = PhotoImage(file ="enter.png")
       self.btnEnter=Button(TopFrame1, width=160, height=60,command= enter_Pin,
       image=self.imgEnter).grid(row=4, column =3,padx=6, pady =4)

       #In this button we have to change the row and column , and we have to change the
       #image which is neccsary .
       #6).=====================================******===============================================#
       self.imgSp1 = PhotoImage(file ="empty.png")
       self.btnSp1=Button(TopFrame1, width=160, height=60, 
       image=self.imgSp1).grid(row=5, column =0,padx=4, pady =4)

       self.img0 = PhotoImage(file ="zero.png")
       self.btn0=Button(TopFrame1, width=160, height=60,command=insert0,
       image=self.img0).grid(row=5, column =1,padx=6, pady =4)

       self.imgSp2 = PhotoImage(file ="empty.png")
       self.btnSp2=Button(TopFrame1, width=160, height=60, 
       image=self.imgSp2).grid(row=5, column =2,padx=6, pady =4)


       self.imgSp3 = PhotoImage(file ="empty.png")
       self.btnSp3=Button(TopFrame1, width=160, height=60, 
       image=self.imgSp3).grid(row=5, column =3,padx=6, pady =4)
       
       #just trying to be consistent with naming  and check the indentation and proper naming should
       #be given   now go to function 

      
if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
        
#the above part is the title as atm system for the project .
