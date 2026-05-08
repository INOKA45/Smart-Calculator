import tkinter as tk

root = tk.Tk()
root.title("Smart Calculator")


value = tk.StringVar()
value.set("")

frame = tk.Frame(root,relief="groove",border=2,background="#ACC8E5")
frame.grid()

disp = tk.Entry(frame,textvariable=value,relief="sunken",justify="right",background="#112A46",foreground="white",font=("Ariel",20))
disp.grid(row=0,column=0,columnspan=4,ipadx=100,ipady=20,padx=20,pady=20)

def click(val):
    if val == "=":
        try:
            expression = value.get()
            if "%" in expression:
                import re
                match = re.search(r'(\d+)([\+\-\*\/])(\d+)%',expression)
                if match:
                    a = float(match.group(1))
                    op = match.group(2)
                    b = float(match.group(3))

                    percent = a * (b/100)

                    if op == "+":
                        result = a + percent
                    elif op == "-":
                        result = a - percent
                    elif op == "*":
                        result = percent
                    elif op == "/":
                        result = a / (b/100)
                
                    value.set(result)
                    return

            expression = expression.replace("%","/100")
            result = eval(expression)
            
            value.set(result)
        except:
            value.set("Error")

    elif val == "C":
        value.set("")
    elif val == "<-":
        value.set(value.get()[:-1])
    else:
        value.set(value.get() + val)

buttons =[
    ("C",1,0),("<-",1,1),("%",1,2),("/",1,3),
    ("7",2,0),("8",2,1),("9",2,2),("*",2,3),
    ("4",3,0),("5",3,1),("6",3,2),("-",3,3),
    ("1",4,0),("2",4,1),("3",4,2),("+",4,3),
    ("00",5,0),("0",5,1),(".",5,2),("=",5,3)
]

for (text,row,col) in buttons:
    
    tk.Button(frame,text=text,command=lambda t=text: click(t),font=("Ariel",20),bd=3,cursor="hand2",relief="sunken",justify="center",activebackground="#ACC8E5",background="#112A46",foreground="white").grid(row=row,column=col,ipadx=15,ipady=15,padx=5,pady=5)
    

root.mainloop()

