
from tkinter import Button
from tkinter import Entry
from tkinter import *



root = Tk()
root.title("Basic Calculator")

input_display = Entry(root,width = "35", borderwidth=5, justify = RIGHT)
input_display.grid(row = 0, column = 0, columnspan = 3, padx = 10,pady = 10 )

result = Entry(root,width = "35", borderwidth=5, justify = RIGHT)
result.grid(row = 1, column = 0, columnspan = 3, padx = 10,pady = 10 )

isPrevKeyOp = False

def compute(key):
    ops_list = {"+","-","/","%","*","="} 
    global isPrevKeyOp
    if((any(key in op for op in ops_list)) ):
        isPrevKeyOp = True
    left_operand = result.get()
    curr_exp = input_display.get()
    if(any(op in curr_exp for op in ops_list)):
       result.delete(0,'end')
       result.insert(0,eval(curr_exp+ left_operand))
    input_display.delete(0,'end')
    curr_exp = curr_exp + left_operand + key
    input_display.insert(0,curr_exp)
   
    
def result_display(key):
    global isPrevKeyOp
    curr_exp = result.get()
    if(key == "<-"):
        curr_exp =  curr_exp[:-1:]
    elif(isPrevKeyOp == True):
        curr_exp = key
        isPrevKeyOp = False
    elif(key == '-'):
        curr_exp = (key + curr_exp) if key not in curr_exp else curr_exp
    elif(key == '.'):
        curr_exp = (curr_exp + key) if key not in curr_exp else curr_exp
    else:
        curr_exp = curr_exp + key
    result.delete(0,'end')
    result.insert(0,curr_exp)


btn_1 = Button(root, text = '1', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("1"))
btn_2 = Button(root, text = '2', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("2"))
btn_3 = Button(root, text = '3', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("3"))
btn_4 = Button(root, text = '4', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("4"))
btn_5 = Button(root, text = '5', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("5"))
btn_6 = Button(root, text = '6', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("6"))
btn_7 = Button(root, text = '7', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("7"))
btn_8 = Button(root, text = '8', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("8"))
btn_9 = Button(root, text = '9', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("9"))
btn_0 = Button(root, text = '0', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("0"))
btn_negate = Button(root, text = '+/-', font = ("Helvetica", 13),padx = 36, pady = 20, command = lambda: result_display("-"))
btn_dot = Button(root, text = '.', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("."))
btn_prod = Button(root, text = '*', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("*"))
btn_minus = Button(root, text = '-', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("-"))
btn_plus = Button(root, text = '+', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("+"))
btn_equal = Button(root, text = '=', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("="))
btn_mod = Button(root, text = '%', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("%"))
btn_ce = Button(root, text = 'CE', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("CE"))
btn_c = Button(root, text = 'C', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: cancel())
btn_del = Button(root, text = '<-', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: result_display("<-"))
btn_divx = Button(root, text = '1/x', font = ("Helvetica", 13),padx = 37, pady = 20, command = lambda: compute("1/x"))
btn_sqrx = Button(root, text = 'x²', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("x²"))
btn_rootx = Button(root, text = '√x', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("√x"))
btn_div = Button(root, text = '/', font = ("Helvetica", 13),padx = 40, pady = 20, command = lambda: compute("/"))



btn_mod.grid(row = 2, column = 0)
btn_ce.grid(row = 2, column = 1)
btn_c.grid(row = 2, column = 2)
btn_del.grid(row = 2, column = 3)
btn_divx.grid(row = 3, column = 0)
btn_sqrx.grid(row = 3, column = 1)
btn_rootx.grid(row = 3, column = 2)
btn_div.grid(row = 3, column = 3)
btn_7.grid(row = 4, column = 0)
btn_8.grid(row = 4, column = 1)
btn_9.grid(row = 4, column = 2)
btn_prod.grid(row = 4, column = 3)
btn_4.grid(row = 5, column = 0)
btn_5.grid(row = 5, column = 1)
btn_6.grid(row = 5, column = 2)
btn_minus.grid(row = 5, column = 3)
btn_1.grid(row = 6, column = 0)
btn_2.grid(row = 6, column = 1)
btn_3.grid(row = 6, column = 2)
btn_plus.grid(row = 6, column = 3)
btn_negate.grid(row = 7, column = 0)
btn_0.grid(row = 7, column = 1)
btn_dot.grid(row = 7, column = 2)
btn_equal.grid(row = 7, column = 3)


root.mainloop()

