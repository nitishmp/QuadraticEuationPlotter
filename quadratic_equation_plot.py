import tkinter as tk
import tkinter.messagebox as msg
import math
from distutils import command


class CoefficientsDialog:
    def __init__(self, master):
        '''
        Create the window widgets
        '''
        self.a =0
        self.b=0
        self.c=0


        self.top = tk.Toplevel(master )
        self.top.geometry('250x100')
        self.top.title("Coefficients")
        tk.Label(self.top , text = "X^2    +").grid(row=0 , column =1)
        tk.Label(self.top, text="X1    +").grid(row=1 , column =1)
        tk.Label(self.top, text="     ").grid(row=2 , column =1)

        self.e1 = tk.Entry(self.top)
        self.e2 = tk.Entry(self.top)
        self.e3 = tk.Entry(self.top)

        self.e1.grid(row =0 , column =0)
        self.e2.grid(row=1, column=0)
        self.e3.grid(row=2, column=0)
        tk.Button(self.top, text="Submit", command=self.submit).grid(rowspan=2, row=3)
        self.top.grab_set()
        master.wait_window(self.top)

    def submit(self, event = None):
        '''
        Handle submit button action
        '''
        self.a, self.b, self.c = self.e1.get(), self.e2.get(), self.e3.get()

        try:
            number1 = int(self.a)
            number2 = int(self.b)
            number3 = int(self.c)
            if (number1 == 0 ):
                raise Exception
        except ValueError:
            msg.showinfo(title="Warning", message="Co efficients must be an integer", parent=self.top)
        except Exception:
            msg.showinfo(title="Warning", message="Co efficients of X2 cannot be 0", parent=self.top)
        else:
            self.top.destroy()

class QuadEQPlot:
    def __init__(self):
        '''
        initialize any required data
        call init_widgets to create the UI
        '''
        self.a=0
        self.b=1
        self.c=0
        self.final_equation = ""
        self.calc=0
        self.points = []
        self.line = []
        self.x_values = [-5 , -4 , -3 , -2 , -1 ,1 ,2 ,3 , 4 ,5]
        self.y_values = [-5 , -4 , -3 , -2 , -1 ,1 ,2 ,3 , 4 ,5]
        self.y_points = [-5, -4, -3, -2, -1,0, 1, 2, 3, 4, 5]
        self.window = tk.Tk()
        self.menu_bar = tk.Menu(self.window)
        self.canvas_frame = tk.Canvas(self.window, width=600, height=600, bg="white")
        self.init_widgets()
        self.plot_axis()
        self.window.config(menu=self.menu_bar)
        self.window.mainloop()
    def init_widgets(self):
        '''
        Create the window widgets and start the mainloop here
        You can call plot_axis to draw the inital x and y
        '''
        def dn():
            pass

        self.window.title("Function Plot")
        self.window.geometry("600x600")

        file_menu = tk.Menu(self.menu_bar , tearoff=False)
        file_menu.add_command(label="New Equation", command=self.new_equation)
        file_menu.add_command(label="Save plot as .ps", command=self.save_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Clear", command=self.clear_canvas)
        file_menu.add_command(label="Exit", command=self.exit)

        self.menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(self.menu_bar , tearoff=False)
        help_menu.add_command(label="About", command= self.show_help_about)

        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        equation_frame = tk.Frame(self.window)
        equation_frame.pack(fill = tk.X , expand = tk.TRUE , side = tk.TOP)
        self.equation_display = tk.Label(equation_frame , text = "No Equation")
        self.equation_display.pack(side = tk.LEFT ,expand = tk.FALSE )
        options = [ "Line" , "Points"]
        radio_frame = tk.Frame(equation_frame)
        radio_frame.pack(expand=tk.FALSE, side=tk.RIGHT)
        self.variable = tk.IntVar()
        rb1= tk.Radiobutton(radio_frame , text = options[1] , variable = self.variable , value =1 , command = self.plot_equation)
        rb1.pack(side=tk.RIGHT)
        rb2 = tk.Radiobutton(radio_frame, text=options[0], variable=self.variable, value=2, command=self.plot_equation)
        rb2.pack(side=tk.RIGHT)
        self.variable.set(1)

    def plot_axis(self):
        '''
        Draw x and y axis in the middle of the canvas
        '''
        self.canvas_frame.delete("all")
        self.canvas_frame.create_line(50, 300, 550, 300, fill="blue")
        self.canvas_frame.create_line(300, 50, 300, 550, fill="blue")

        self.canvas_frame.pack(fill=tk.X, expand=tk.TRUE, side=tk.BOTTOM)
        for num in range(50, 600, 50):
            self.canvas_frame.create_line(num, 300, num, 295, fill="black")

        for num in range(50 , 600 ,50):
            self.canvas_frame.create_line(300, num, 305, num, fill="black")


        self.canvas_frame.create_text(50,310, text = self.x_values[0] )
        self.canvas_frame.create_text(100,310, text= self.x_values[1])
        self.canvas_frame.create_text(150, 310, text= self.x_values[2])
        self.canvas_frame.create_text(200, 310, text= self.x_values[3])
        self.canvas_frame.create_text(250, 310, text= self.x_values[4])
        self.canvas_frame.create_text(350, 310, text= self.x_values[5])
        self.canvas_frame.create_text(400, 310, text= self.x_values[6])
        self.canvas_frame.create_text(450, 310, text= self.x_values[7])
        self.canvas_frame.create_text(500, 310, text= self.x_values[8])
        self.canvas_frame.create_text(550, 310, text= self.x_values[9])

        self.canvas_frame.create_text(285, 550, text= self.y_values[0])
        self.canvas_frame.create_text(285, 500, text= self.y_values[1])
        self.canvas_frame.create_text(285, 450, text= self.y_values[2])
        self.canvas_frame.create_text(285, 400, text= self.y_values[3])
        self.canvas_frame.create_text(285, 350, text= self.y_values[4])
        self.canvas_frame.create_text(285, 250, text= self.y_values[5])
        self.canvas_frame.create_text(285, 200, text= self.y_values[6])
        self.canvas_frame.create_text(285, 150, text= self.y_values[7])
        self.canvas_frame.create_text(285, 100, text= self.y_values[8])
        self.canvas_frame.create_text(285, 50, text= self.y_values[9])

    def plot_equation(self,*args):
        '''
        plot the equation on canvas
        first clean the canvas, call plot_axis, calculate y values, and call either plot_points or plot_line
        '''
        self.clear_canvas()
        self.plot_axis()
        self.equation_display["text"] = self.final_equation

        i=0
        check = 0
        for x in range(-5, 6):
            self.y_points[i] = (int(self.a) * (x ** 2)) + (int(self.b) * (x)) + int(self.c)
            if (self.y_points[i] > 0):
                check = 1
            i = i + 1

        if (check == 1):
            highest = self.y_points[0]

            for x in self.y_points:
                if (x > highest):
                    highest = x
            self.calc = highest
            index = highest // 5
            highest = highest * -1
            i = 0
            for i in range(0, 5):
                self.y_values[i] = highest
                highest = highest + index
            j = 4
            for i in range(5, 10):
                self.y_values[i] = self.y_values[j] * -1
                j = j - 1
        else:
            lowest = self.y_points[0]

            for x in self.y_points:
                if (x < lowest):
                    lowest = x
            self.calc = lowest*-1
            index = (lowest * -1) // 5

            i = 0
            for i in range(0, 5):
                self.y_values[i] = lowest
                lowest = lowest + index
            j = 4
            for i in range(5, 10):
                self.y_values[i] = self.y_values[j] * -1
                j = j - 1

        self.plot_axis()

        self.points = []

        for i in range(0,11):
            self.points.append(self.y_points[i])
        if (self.calc == 0) :
            pass
        else:
            mul = 500 / (2 *self.calc)

            x=50
            y=0
            for i in range(0,11):
                y = mul * (self.calc - self.y_points[i])
                y1 = 50 + math.ceil(y)
                #self.canvas_frame.create_oval(x,y1 , x+5, y1+5, width=1, fill="yellow" , outline = "red")
                self.line.append(x)
                self.line.append(y1)
                x = x+50
        if(self.variable.get() == 1 ):
            self.plot_points(self.points)
        else:
            self.plot_line(self.points)

    def plot_points(self,scaled_points):
        '''
        for each x and y points, plot a 2x2 oval shape with a red border and yellow fill
        '''

        self.clear_canvas()

        self.plot_axis()
        self.equation_display["text"] = self.final_equation
        if (self.calc == 0) :
            pass
        else:
            mul = 500 / (2 *self.calc)

            x=50
            y=0
            for i in range(0,11):
                y = mul * (self.calc - self.y_points[i])
                y1 = 50 + math.ceil(y)
                self.canvas_frame.create_oval(x,y1 , x+5, y1+5, width=1, fill="yellow" , outline = "red")
                self.line.append(x)
                self.line.append(y1)
                x = x+50


    def plot_line(self,*scaled_points):
        '''
        using the (x, y) points, plot a smooth red line
        '''
        self.clear_canvas()
        self.plot_axis()
        self.equation_display["text"] = self.final_equation
        for x in range(0,19,2):
            self.canvas_frame.create_line(self.line[x] ,self.line[x+1] , self.line[x+2] ,self.line[x+3] , fill="red"  )


    def clear_canvas(self):
        '''
        triggered when the menu command 'Clear' is clicked
        delete everything from the canvas and set the coefficients to 0's
        '''
        self.x_values = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        #self.y_values = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.equation_display["text"] = "No Equation"
        self.plot_axis()

    def new_equation(self):
        '''
        triggered when the menu command 'New Equation' is clicked
        call the child window to get the equation coefficients and then call plot_equation
        '''
        self.getVariables = CoefficientsDialog(self.window)
        self.final_equation = self.getVariables.a + " X^2 + " + self.getVariables.b + " X + " + self.getVariables.c
        self.line = []
        self.a= self.getVariables.a
        self.b = self.getVariables.b
        self.c = self.getVariables.c
        self.plot_equation()

       # self.getVariables.
    def save_canvas(self):
        '''
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        '''
        self.canvas_frame.postscript(file="1014060.ps", colormode='color')
    def exit(self):

        '''
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        '''
        reply = msg.askyesno('Exit',"Are you sure you want to exit?")
        if reply == True:
            self.window.destroy()
    def show_help_about(self):
        '''
        triggered when the menu command 'About' is clicked
        Show an information dialog displaying your name on one line and id number on the second
        '''
        msg.showinfo(title="About QuadEQPlot" , message="Created by = Adarsh Sarala Nagaraja \n ID : 1014060")

q = QuadEQPlot()