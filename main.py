import string
import random
import tkinter as tk

class Mainwindow:
    def __init__(self):
        self.main = tk.Tk()
        self.main.geometry("300x350")
        self.main.resizable(width=False, height=False)
        self.main.title("Gerador de senha")
        self.main.mainloop()

    def widgets(self):
        self.frame = tk.Frame(self.main)

        # opcoes de caracteres
        self.val, self.special, self.num = tk.IntVar(), tk.IntVar(), tk.IntVar()
        self.optionsFrame = tk.LabelFrame(self.frame, text="Opções")
        self.uppercase = tk.Checkbutton(self.optionsFrame, text="Com letras maiusculas", onvalue=1, offvalue=0, variable=self.val)
        self.specialChar = tk.Checkbutton(self.optionsFrame, text="Com caracteres especiais (@#$)", onvalue=1, offvalue=0, variable=self.special)
        self.number = tk.Checkbutton(self.optionsFrame, text="Com números", onvalue=1, offvalue=0, variable=self.num)

        # opcoes de tamanho de senha
        self.length = tk.IntVar()
        self.lengthFrame = tk.LabelFrame(self.frame, text="Tamanho da senha")
        self.radioButton1 = tk.Radiobutton(self.lengthFrame, text="10", value=10, variable=self.length)
        self.radioButton2 = tk.Radiobutton(self.lengthFrame, text="12", value=12, variable=self.length)
        self.radioButton3 = tk.Radiobutton(self.lengthFrame, text="14", value=14, variable=self.length)
        self.length.set("10")

        # area das caixa de texto e botôes
        self.genPwd = tk.Button(self.main, text="Gerar senha", width=25, command=self.generatePassword)
        self.viewHistory = tk.Button(self.main, text="Ver senhas geradas (histórico)", command=self.getHistory)
        self.textBox = tk.Text(self.main, width=25, height=8, relief="solid")

        self.widgetsInFrame = [ self.uppercase, self.specialChar, self.number ]
        for item in self.widgetsInFrame: item.pack(pady=5, anchor="w")
        self.radioButtons = [ self.radioButton1, self.radioButton2, self.radioButton3 ]
        for radioButton in self.radioButtons: radioButton.pack(pady=5, anchor="w")
        self.optionsFrame.grid(row=0, column=0)
        self.lengthFrame.grid(row=0, column=1)
        self.mainWidgets = [ self.frame, self.genPwd, self.viewHistory, self.textBox ]
        for widget in self.mainWidgets: widget.pack(pady=5)

Mainwindow()