import tkinter as tk

fenetre = tk.Tk()
fenetre.title("COUCOU")
fenetre.geometry("300x300")


# afficher du texte sur l'écran tkiner par le bouton
def bonjourfonction():
    label['text'] = "rizz"
    quitter.config(bg="green", state="normal")
    fenetre.config(bg="blue")


# ecrire quelque chose dans le label avant le bouton
label = tk.Label(fenetre, text="en attente...")

bonjour = tk.Button(fenetre, text="bonjour", command=bonjourfonction)
quitter = tk.Button(fenetre, text="quitter", bg="red", state="disabled", command=fenetre.destroy)

label.pack()
bonjour.pack()
quitter.pack()

fenetre.mainloop()