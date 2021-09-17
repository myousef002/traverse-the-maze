import tkinter as tk
import random
import turtle

class Maze:

    #Defines the grid size, square size, and creates the matrix with every square color set to black
    def __init__(self, size, square_size):

        self.size = size
        self.square_size = square_size
        self.visited_squares = []
        self.walls = []
        self.grid = [['b' for x in range(self.size)]for x in range(self.size)]


    #Used to draw the individual squares 
    def draw(self, row, col, canvas, color):
        x1 = col * self.square_size
        y1 = row * self.square_size
        x2 = x1 + self.square_size
        y2 = y1 + self.square_size
        return canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    #Converts the matrix into a canvas drawing
    def create(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 'b':
                    color = 'black'
                elif self.grid[row][col] == 'w':
                    color = 'white'
                self.draw(row, col, canvas, color)

    #Checks the squares surrounding a white square and determines which qualify as potential white squares
    def check_neighbors(self, cr, cc):
        neighbors =  [[cr, cc-1, cr-1, cc-2, cr, cc-2, cr+1, cc-2, cr-1, cc-1, cr+1, cc-1], #left
                [cr, cc+1, cr-1, cc+2, cr, cc+2, cr+1, cc+2, cr-1, cc+1, cr+1, cc+1], #right
                [cr-1, cc, cr-2, cc-1, cr-2, cc, cr-2, cc+1, cr-1, cc-1, cr-1, cc+1], #top
                [cr+1, cc, cr+2, cc-1, cr+2, cc, cr+2, cc+1, cr+1, cc-1, cr+1, cc+1]] #bottom
        
        visitable_neighbors = []           
        for i in neighbors:    #find neighbors to visit
            if i[0] > 0 and i[0] < (self.size-1) and i[1] > 0 and i[1] < (self.size-1):
                if self.grid[i[2]][i[3]] == 'w' or self.grid[i[4]][i[5]] == 'w' or self.grid[i[6]][i[7]] == 'w' or self.grid[i[8]][i[9]] == 'w' or self.grid[i[10]][i[11]] == 'w' or self.grid[i[2]][i[3]] == 'r' or self.grid[i[4]][i[5]] == 'r' or self.grid[i[6]][i[7]] == 'r' or self.grid[i[8]][i[9]] == 'r' or self.grid[i[10]][i[11]] == 'r' or self.grid[i[2]][i[3]] == 'g' or self.grid[i[4]][i[5]] == 'g' or self.grid[i[6]][i[7]] == 'g' or self.grid[i[8]][i[9]] == 'g' or self.grid[i[10]][i[11]] == 'g':
                    self.walls.append(i[0:2])
                else:
                    visitable_neighbors.append(i[0:2])
        return visitable_neighbors

class movingSquare:

    #Defines the starting square's row and column
    def __init__(self):
        
        self.sr = random.randrange(1, maze.size)
        self.sc = random.randrange(1, maze.size)
        self.revisitedSquares = []
        self.cr = self.sr
        self.cc = self.sc

    #Converts the matrix from all 'b' values to both 'b' and 'w' values. This creates the maze values
    def start_end(self):
        
        cr = self.sr
        cc = self.sc
        maze.grid[cr][cc] = 'w'
        finished = False
        while not finished:
            visitable_neighbors = maze.check_neighbors(cr, cc)
          
            if len(visitable_neighbors) != 0:
                d = random.randint(1, len(visitable_neighbors))-1
                nr, nc = visitable_neighbors[d]
                maze.grid[nr][nc] = 'w'
                maze.visited_squares.append([nr, nc])
                cr = nr
                cc = nc

            if len(visitable_neighbors) == 0:
                #If there is no squares that can be converted to 'w' the program will try and use the last value and see if there was another route or potential square
                try:
                    cr, cc = maze.visited_squares.pop()
                    self.revisitedSquares.append([cr, cc])
                except:
                    finished = True
                    

    #Event functions that move the starting square and reset canvas        
    def up(self, event):
        if maze.grid[self.cr-1][self.cc] == 'w':
            canvas.move(originalSquare, 0, -maze.square_size)
            self.cr -= 1       
        if self.cr == er and self.cc == ec:
            canvas.delete("all")
            end_title.place(x=120, y=100)
            play.place(x=150,y=200)
            difficultyMenu.place(x=200, y=250)
            timer.pack_forget()
            end_time.config(text="Completed in "+str(time)+" seconds")
            end_time.place(x=100,y=300)
            
    def down(self, event):
        if maze.grid[self.cr+1][self.cc] == 'w':
            canvas.move(originalSquare, 0, maze.square_size)
            self.cr += 1
        if self.cr == er and self.cc == ec:
            canvas.delete("all")
            end_title.place(x=120, y=100)
            play.place(x=150,y=200)
            difficultyMenu.place(x=200, y=250)
            timer.pack_forget()
            end_time.config(text="Completed in "+str(time)+" seconds")
            end_time.place(x=100,y=300)
            
    def left(self, event):
        if maze.grid[self.cr][self.cc-1] == 'w':
            canvas.move(originalSquare, -maze.square_size, 0)
            self.cc -= 1
        if self.cr == er and self.cc == ec:
            canvas.delete("all")
            end_title.place(x=120, y=100)
            play.place(x=150,y=200)
            difficultyMenu.place(x=200, y=250)
            timer.pack_forget()
            end_time.config(text="Completed in "+str(time)+" seconds")
            end_time.place(x=100,y=300)
            
    def right(self, event):
        if maze.grid[self.cr][self.cc+1] == 'w':
            canvas.move(originalSquare, maze.square_size, 0)
            self.cc += 1
        if self.cr == er and self.cc == ec:
            canvas.delete("all")
            end_title.place(x=120, y=100)
            play.place(x=150,y=200)
            difficultyMenu.place(x=200, y=250)
            timer.pack_forget()
            end_time.config(text="Completed in "+str(time)+" seconds")
            end_time.place(x=100,y=300)
            
#Create the starting window and screen 
win = tk.Tk()
win.title('Maze Game')
canvas_size = 1500
win_size = ("500x550")
win.geometry(win_size)
canvas = tk.Canvas(win, width=canvas_size, height=canvas_size, bg='Gray')
canvas.pack()

game_title = tk.Label(win, text="Traverse the Maze", bg='Gold', font=("Courier", 35, "bold"))
game_title.place(x=70, y=100)

end_title = tk.Label(win, text="Maze Cleared", bg='Gold', font=("Courier", 35, "bold"))

#Timer function
time = 0
timer = tk.Label(win, text="Time: "+str(time), font=("Courier", 20, "bold"))
end_time = tk.Label(win, text="Completed in "+str(time)+" seconds", font=("Courier", 20, "bold"))
def timerUpdate():
    global time
    time += 1
    timer.config(text="Time: "+str(time))
    win.after(1000, timerUpdate)
timerUpdate()

#Difficulty Settings
difficulty = tk.StringVar(win)
difficulty.set("Medium")

difficultyMenu = tk.OptionMenu(win, difficulty, "Easy", "Medium", "Hard")
difficultyMenu.place(x=180, y=250)
difficultyMenu.config(font=("Courier", 25, "bold"))

def g(offset):
    g = turtle.RawTurtle(canvas) #Makes the turtle drawing be on the same canvas as the maze game rather than in a seperate window
    g.speed(800)
    g.color("navy blue")

    rotate=int(0)
    h(g,random.randrange(0, 1), offset)

def circle(g,s):
    for i in range(8):
        g.circle(s)
        s = s - 100

def h(g,s,repeat):
    for i in range(repeat):
        circle(g,s)
        g.right(6/repeat)

def main(x, y):
    for i in range(2):
        g(x)
        x+=y


#These variables need to be global variables in order to be used throughout the code
maze = None

square = None

originalSquare = None

er = None

ec = None

#The play button creates and begins the game                                                    
def playButton():
    global maze
    global square
    global originalSquare
    global er, ec
    global time
    
    #Sets the maze size and square size based on difficulty
    if difficulty.get() == "Easy":
        size = 20
        square_size = 25
    elif difficulty.get() == "Medium":
        size = 40
        square_size = 12
    elif difficulty.get() == "Hard":
        size = 60
        square_size = 8

    #Create Timer
    time = 0
    timer.pack()

    #Create the objects and gain access to methods within them
    maze = Maze(size, square_size)
    square = movingSquare()

    #Converts the canvas size according to our maze size
    canvas_size = maze.size * maze.square_size
    canvas.config(width=canvas_size, height=canvas_size)

    #Creates the maze
    square.start_end()
    maze.create()

    #Create the starting/movable square
    originalSquare = maze.draw(square.sr, square.sc, canvas, 'light green')

    #Create the ending square
    d = random.randint(1, len(square.revisitedSquares))-1
    er, ec = square.revisitedSquares[d]
    maze.draw(er, ec, canvas, 'red')

    #Removes all the buttons from the starting screen
    play.place_forget()
    game_title.place_forget()
    end_title.place_forget()
    difficultyMenu.place_forget()
    end_time.place_forget()
    
    #Binds the wasd keys to the movement methods created in the start_end class
    win.bind("<w>", square.up)
    win.bind("<s>", square.down)
    win.bind("<a>", square.left)
    win.bind("<d>", square.right)



#Create the play button
play = tk.Button(win, text="Click to Play", fg='black', font=("Courier", 25, "bold"))
play['command'] = playButton
play.place(x=140,y=190)

#Calls the turtle function
main(1, 3) 

win.mainloop()


