import tkinter as tk
from PIL import Image, ImageTk

#création première fenêtre
window = tk.Tk()

#paramètre de la fenêtre 
window.title("Pokémon Image")
window.geometry("1080x720")
 
image = Image.open('./images/caterpie.jpg')

image2 =image.resize((int(image.width/1.5),int(image.height/1.5)))
# Remplace PhotoImage de Tkinter par celui de PIL
photo = ImageTk.PhotoImage(image2)

#label = tk.Label(window, image=photo)
#label.pack()
canvas = tk.Canvas(window, width=photo.width(), height=photo.height())
canvas.create_image(540,360,anchor='center',image=photo)
canvas.pack(side='top', fill='both', expand='yes')


# affichage
window.mainloop()