import tkinter, random 


def lodicka(x, y): 
    plachta = random.randint(-4, 4) 
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)


def ciara():
    canvas.create_line(650, 0, 650, 700, fill="red", width=3)
    

def preteky(distances):
    canvas.delete("all")
    win = []
    for i in range(15):
        distances[i] += random.randint(0, 12)
        x = distances[i] + random.randint(-3, 3)
        y = 30 + i*45
        lodicka(x, y)
        if x >= 650:
            win.append(i)
    ciara()
    
    if len(win) == 0:
        canvas.after(100, preteky, distances)
    elif len(win) == 1:
        canvas.create_text(350, 400, text=f"Vyhrala lodička číslo: {win[0]+1}", font=("Arial", 30), fill="red", anchor="center")
    else:
        canvas.create_text(350, 400, text=f"Vyhrali lodičky s číslami: {', '.join([str(i+1) for i in win[:-1]])} a {win[-1]+1}", font=("Arial", 20), fill="red", anchor="center")
    
root = tkinter.Tk()
root.title("Lodicky")
root.geometry("700x800")

canvas = tkinter.Canvas(width=700, height=800) 
canvas.pack()

distances = [20]*15

for i in range(15):
    lodicka(20, 30 + i*45)

ciara()
    
canvas.after(1000, preteky, distances)
root.mainloop()
