from tkinter import Button, Entry, Frame, Label, StringVar, font, ttk, CENTER

class Settings:
    def configure(self, root):
        self.root = root
        self.root.geometry("800x350")
        self.root.title("Project - ULA")

        "Frame Entradas"
        self.frameEntry = Frame(self.root, relief="raised", bg="orange")
        self.frameEntry.place(x=10,y=10, width=400, height=80)

        "Frame Saida das Entradas"
        self.frameOut = Frame(self.root, relief="raised", bg="orange")
        self.frameOut.place(x=400,y=10, width=390, height=290)

        "Frame Resultados"
        self.frame_03 = Frame(self.root, relief="raised", bg="orange")
        self.frame_03.place(x=10,y=100, width=380, height=200)

        "Configure Fontes color"
        self.font = font.Font(family="Bahnschrift SemiBold", size=15, weight="bold")

        "Rodape"
        Label(self.root, text="Disciplina - Organização de Computadores", font=('Arial',26,'bold')).place(x=0, y=300, width=800)

        "Frame NOT A - B"
        self.frame_04 = Frame(self.root, relief="raised", bg="orange")
        self.frame_04.place(x=240,y=135, width=40, height=100)

    def treeview(self):
        Label(self.frame_03, text="Operadores Logicos", bg='orange', font=self.font).place(x=20, y=5)
        
        "Treeview AND"
        self.tv_and = ttk.Treeview(self.frame_03, columns=("A"), show="headings")
        self.tv_and.column("A", anchor=CENTER, minwidth=20,width=50)
        self.tv_and.heading('A', text="AND")
        self.tv_and.place(x=5, y=35, height=100)

        "Treeview OR"
        self.tv_or = ttk.Treeview(self.frame_03, columns=("B"), show="headings")
        self.tv_or.column("B", anchor=CENTER, minwidth=20,width=50)
        self.tv_or.heading('B', text="OR")
        self.tv_or.place(x=60, y=35, height=100)
        
        "Treeview XOR"
        self.tv_xor = ttk.Treeview(self.frame_03, columns=("XOR"), show="headings")
        self.tv_xor.column("XOR", anchor=CENTER, minwidth=20,width=50)
        self.tv_xor.heading('XOR', text="XOR")
        self.tv_xor.place(x=115, y=35, height=100)
        
        "Treeview NOT"
        self.tv_not = ttk.Treeview(self.frame_03, columns=("NOT"), show="headings")
        self.tv_not.column("NOT", anchor=CENTER, minwidth=40,width=50)
        self.tv_not.heading('NOT', text="NOT")
        self.tv_not.place(x=170, y=35, height=100)
        
    def entry(self):
        self.numA = Label(self.frameEntry, text="Entre com o numero A: ", font=self.font)
        self.numA.place(x=5,y=5)
        
        self.entry_numA = StringVar()
        Entry(self.frameEntry, textvariable=self.entry_numA, font=self.font).place(x=230, y=5, width=50)

        self.numB = Label(self.frameEntry, text="Entre com o numero B: ", font=self.font)
        self.numB.place(x=5,y=45)

        self.entry_numB = StringVar()
        Entry(self.frameEntry, textvariable=self.entry_numB, font=self.font).place(x=230, y=45, width=50)

        self.btn_inp = Button(self.frameEntry, text="Enviar", font=self.font, command=lambda : self.convertBinary())
        self.btn_inp.place(x=300, y=5, height=70)

    def convertBinary(self):
        self.num_A = "{0:b}".format(int(self.entry_numA.get()))
        self.num_B = "{0:b}".format(int(self.entry_numB.get()))
        
        if len(self.num_A) == 1:
            self.num_A = "00" + str(self.num_A)

        if len(self.num_A) == 2:
            self.num_A = "0" + str(self.num_A)
        
        if len(self.num_B) == 1:
            self.num_B = "00" + str(self.num_B)

        if len(self.num_B) == 2:
            self.num_B = "0" + str(self.num_B)

        Label(self.frame_03,text="Decimal", bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 280, y= 100)
        
        Label(self.frame_03, text=f" A: {self.num_A}", font=self.font, background="orange").place(x=290, y=40)
        Label(self.frame_03, text=f" B: {self.num_B}", font=self.font, background="orange").place(x=290, y=70)

        Label(self.frame_03,text="Binario", bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 285, y= 10)
        
        Label(self.frame_03, text=" | ".join(self.num_A), bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 200, y= 140)
        Label(self.frame_03, text="4 | 2 | 1", bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 200, y= 170)
        
        Label(self.frame_03, text=" | ".join(self.num_B), bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 80, y= 140)
        Label(self.frame_03, text="4 | 2 | 1", bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 80, y= 170)