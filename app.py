import tkinter as tk
from random import randint
#from main import listening
from commands import stop_jarvis
import subprocess

WIDTH = 400
HEIGHT = 600
RADIUS = 50

colors = ['blue']#шарики

previous_process = None
def start_up():
    subprocess.call(['python', 'main.py'])
    #global previous_process
    # Проверяем, был ли запущен предыдущий сабпроцесс
    #if previous_process and previous_process.poll() is None:
    #    previous_process.terminate() 

    #previous_process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #while True:
    #    output = previous_process.stdout.readline().decode()
    #    if output == '' and previous_process.poll() is not None:
    #        break
    #    if output:
    #        label.config(text=output.strip()) # обновляем виджет Label
    #    root.update()

def create_circle(x, y, r, color):
    return canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)

directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

def move_circles():
    for i in range(len(circles)):
    # Get current coordinates of the circle
        x1, y1, x2, y2 = canvas.coords(circles[i])
        dx, dy = directions[i]  # Get current direction
        # Calculate next coordinates
        next_x1, next_y1, next_x2, next_y2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
    
        # Check if the circle is going out of the window boundaries
        if next_x2 > WIDTH or next_x1 < 0:
            dx = -dx  # Reverse direction on x-axis
        if next_y2 > HEIGHT or next_y1 < 0:
            dy = -dy  # Reverse direction on y-axis
    # Move the circle
    canvas.move(circles[i], dx, dy)
    # Update the direction
    directions[i] = (dx, dy)
    # Call the function again after a delay
    root.after(10, move_circles)

# Create the tkinter window
root = tk.Tk()

label = tk.Label(root, text="Привет, мир!", font=("Arial", 10))
label.pack()

root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Jarvice-service")
# Create the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create the circles
circles = []
for _ in colors:
    x = randint(RADIUS, WIDTH - RADIUS)
    y = randint(RADIUS, HEIGHT - RADIUS)
    circles.append(create_circle(x, y, RADIUS, _))

button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button1 = tk.Button(button_frame, text="СТАРТ", command=start_up, width=10, height=2, bd=8, relief=tk.RAISED, padx=20, borderwidth=4, font=('Arial', 12, 'bold'))
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(button_frame, text="СТОП", command= stop_jarvis, width=10, height=2, bd=8, relief=tk.RAISED, padx=20, borderwidth=4, font=('Arial', 12, 'bold'))
button2.pack(side=tk.LEFT, padx=5)

move_circles()
start_up()
root.mainloop()