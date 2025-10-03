import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
]

right_symbols = {"÷", "x", "-", "+", "="}
top_symbols = {"AC", "+/-", "%", "√"}


color_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

row_count = len(button_values)
col_count = len(button_values[0])

# create main window
window = tkinter.Tk()
window.title("Calculator")

window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", anchor="e", 
                      bg=color_black, fg=color_white, 
                      padx=10, font=("Arial", 40),
                      width=col_count)  # if not add width it will take the full width of the window

label.grid(row = 0, column = 0, columnspan=col_count, sticky="we")


for row in range(row_count):
    for col in range(col_count):
        value = button_values[row][col]
        
        button = tkinter.Button(frame, text=value, font=("Arial", 24),
                                width= col_count - 1, height= 1,
                                command= lambda value=value:button_clicked(value))  
        # To add colors in the buttons
        if value in top_symbols:
            button.config(foreground=color_black, background=color_gray,
                          activebackground=color_gray)
            
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange,
                          activebackground=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray,
                          activebackground=color_dark_gray)
            
            
        button.grid(row=row + 1, column=col, sticky="")
        
frame.pack()


# operation to perform in the calculator when a button is clicked
A = "0"
operator = None
B = None

#after complete work to clear valus

def clear_all():
    global A, operator, B
    A = "0"
    operator = None
    B = None
    
def button_clicked(value):
    
    if value in top_symbols:
        # {"AC", "+/-", "%", "√"}
        
        if value == "AC":
            clear_all()
            label["text"] = "0"
        
        elif value == "+/-":
            try:
                current_value = float(label["text"])
                current_value = -current_value
                if current_value.is_integer():  # check if the float is an integer value
                    current_value = int(current_value)  # convert to int to avoid displaying .0
                label["text"] = str(current_value)
                
            except ValueError:
                label["text"] = "Error"
        
        
        elif value == "%":
            try:
                current_value = float(label["text"])
                percent_value = current_value / 100
                label["text"] = str(percent_value)
            except ValueError:
                label["text"] = "Error"
        
        elif value == "√":
            try:
                current_value = float(label["text"])
                if current_value < 0:
                    label["text"] = "Error"  # Square root of negative number is not defined in real numbers
                else:
                    sqrt_value = current_value ** 0.5
                    label["text"] = f"{sqrt_value:.5f}"   # display up to 5 decimal places
                    
                    """
                    Another way
                    square_root = round(current_value ** 0.5, 5)
                    label["text"] = str(square_root)
                    """ 
            except ValueError:
                label["text"] = "Error"
        

    
    # right_symbols = {"÷", "x", "-", "+", "="}
    elif value in right_symbols:
        global A, operator, B
        
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                
                try:
                    num1 = float(A)
                    num2 = float(B)
                    result = 0
                    
                    if operator == "÷":
                        if num2 == 0:
                            label["text"] = "Error"  # handle division by zero
                        else:
                            result = num1 / num2
                            label["text"] = str(result)
                    
                    elif operator == "x":
                        result = num1 * num2
                        label["text"] = str(result)
                    
                    elif operator == "-":
                        result = num1 - num2
                        label["text"] = str(result)
                    
                    elif operator == "+":
                        result = num1 + num2
                        label["text"] = str(result)
                    
                    if result.is_integer():  # check if the float is an integer value
                        result = int(result)  # convert to int to avoid displaying .0
                        label["text"] = str(result)
                        
                    # after calculation reset A, operator, B for next calculation
                    clear_all()
                    
                except ValueError:
                    label["text"] = "Error"
            
            
        elif value in {"÷", "x", "-", "+"}:
            if operator is None:  # if no operator is set
                A = label["text"]
                label["text"] = "0"  # reset the label for the next number input
                B = "0"
                
            operator = value
            
    
    # for numbers and decimal point
    else:  
        
        #decimal point
        if value == ".":
            
            #To avoid multiple decimal points in the label -> 4.5.6 invalid
            if value not in label["text"]:   # if there is no decimal point in the label then add it
                label["text"] += value
        
        #int number
        elif value in "0123456789":
            
            # 05 -> 5
            if label["text"] == "0":   # if the label is 0 then replace it with the new value          
                label["text"] = value
                
            else:
                label["text"] += value


# center the window on the screen
# generally window open in the top left corner of the screen, to center it we use the following code
window.update() # Update "requested size" from geometry manager
width = window.winfo_width()
height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = (screen_width // 2) - (width // 2)
window_y = (screen_height // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, window_x, window_y))  

window.mainloop()

