import tkinter
import random

rows=25
cols=25
tile_size=25

Window_width = tile_size*rows
Window_height = tile_size*cols

class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y



#game window setup
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window,bg="black",width=Window_width,height=Window_height,borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()

#center the window
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x = int((screen_width//2) - (window_width//2))
window_y = int((screen_height//2) - (window_height//2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initalizing game
snake=Tile(5*tile_size,5*tile_size) #single tile for stating position of snake
food = Tile(10*tile_size,10*tile_size)
snake_body = []
velocityX=0
velocityY=0
game_over = False
score=0

def change_direction(e):
    # print(e.keysym)
    global velocityX,velocityY,game_over
    if (game_over):
        return

    if (e.keysym=="Up" and velocityY !=1):
        velocityX=0
        velocityY=-1
    elif (e.keysym=="Down" and velocityY != -1):
        velocityX=0
        velocityY=1
    elif (e.keysym=="Left" and velocityX != -1):
        velocityX=-1
        velocityY=0
    elif (e.keysym=="Right" and velocityX != -1):
        velocityX=1
        velocityY=0  
    

def move():
    global snake,food,snake_body,game_over,score
    if (game_over):
        return
    if (snake.x<0 or snake.x>=Window_width or snake.y<0 or snake.y>=Window_height):
        game_over = True
        return

    for tile in snake_body:
        if(snake.x==tile.x and snake.y==tile.y):
            game_over=True
            return

    #collison
    if(snake.x==food.x and snake.y==food.y):
        snake_body.append(Tile(food.x,food.y))
        food.x=random.randint(0,cols-1)*tile_size
        food.y=random.randint(0,rows-1)*tile_size
        score+=1

    #update snake body
    for i in range(len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if(i==0):
            tile.x=snake.x
            tile.y=snake.y
        else:
            prev_tile=snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    snake.x += velocityX*tile_size
    snake.y += velocityY*tile_size

    #draw snake

def draw():
    global snake,food,snake_body,game_over,score
    move()
    canvas.delete("all")
    # draw snake
    canvas.create_rectangle(snake.x,snake.y,snake.x+tile_size,snake.y+tile_size,fill="lime green")

    #draw food
    canvas.create_rectangle(food.x,food.y,food.x+tile_size,food.y+tile_size,fill="red")

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x+tile_size,tile.y+tile_size,fill="lime green")

    if(game_over):
        canvas.create_text(Window_width/2,Window_height/2,font+"Arial 20",text=f"Game Over: {score}",fill="white")
    else:
        canvas.create_text(30,20,font="Arial 10",text=f"Score: {score}",fill="white")
    
    window.after(100,draw) # 10 frame/second ,, 100 milli seonds

draw()
window.bind("<KeyRelease>",change_direction)
window.mainloop()