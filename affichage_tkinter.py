import tkinter as tk
from PIL import Image, ImageTk

#création première fenêtre
window = tk.Tk()

#paramètre de la fenêtre 
window.title("Pokémon Image")
window.geometry("1080x720")
 
image = Image.open('./images/blastoise.jpg')
# Remplace PhotoImage de Tkinter par celui de PIL
photo = ImageTk.PhotoImage(image)

label = tk.Label(window, image=photo)
label.pack()
# affichage
window.mainloop()