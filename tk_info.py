import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Frame Info")
fenetre.geometry("400x400")

# faire labelframe est comme faire frame
for element in range(10):

    ma_frame = tk.LabelFrame(fenetre)
    label = tk.Label(ma_frame, text="titre" + str(element+1))
    btn = tk.Button(ma_frame, text="Bouton")

# placer nos boutons
    ma_frame.grid(row=0, column=element)

    label.grid(row=0, column=0)
    btn.grid(row=1, column=1)

fenetre.mainloop()
