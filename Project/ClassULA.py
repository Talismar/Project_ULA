"Aqui se refere-se as configurações de Frames e Convenção Binaria que fiz no arquivo Settings.py"
from Settings import Settings
from tkinter import Button, Entry, Label, Tk, END
"Aqui se refere-se ao arquivo Divisao.py que fiz em outro arquivo"
from Divisao import Division

class ULA(Settings):
    def __init__(self):
        self.root = Tk()
        self.configure(self.root)
        self.treeview()
        self.entry()
        self.UC()
        self.root.mainloop()

    def UC(self):
        "Lista UC"
        self.lst_UC = [("000","Soma"), 
                       ("001","Subtração"), 
                       ("010", "Multiplicação"),
                       ("011", "Divisão"),
                       ("100","AND"), 
                       ("101","OR"), 
                       ("110","XOR"),
                       ("111","NOT")] 
        
        "Table com informações da UC"
        axis_y = 40
        axis_x = 170
        for i in range(len(self.lst_UC)): 
            for j in range(0,1):
                self.e = Entry(self.frameOut, width=17, relief='groove', font=('Arial',16,'bold'), disabledforeground='black', disabledbackground="white")
                self.e.place(x=axis_x, y=axis_y) 
                self.e.insert(END, self.lst_UC[i][j]) 
                self.e.config(state='disabled')
            
            axis_y += 25
            axis_x = 170

        "Label UC"
        Label(self.frameOut,text="Unidade de controle", bg="orange", fg="white", font=('Arial',16,'bold')).place(x= 170, y= 10)
        
        "Configure Buttons"
        Button(self.frameOut, text=self.lst_UC[0][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("000")).place(x = 230, y = 41, height=23)
        Button(self.frameOut, text=self.lst_UC[1][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("001")).place(x = 230, y = 41+25, height=23)
        Button(self.frameOut, text=self.lst_UC[2][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("010")).place(x = 230, y = 66+25, height=23)
        Button(self.frameOut, text=self.lst_UC[3][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("011")).place(x = 230, y = 91+25, height=23)
        Button(self.frameOut, text=self.lst_UC[4][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("100")).place(x = 230, y = 116+25, height=23)
        Button(self.frameOut, text=self.lst_UC[5][1], border=0, bg='white', fg="black",font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("101")).place(x = 230, y = 141+27, height=23)
        Button(self.frameOut, text=self.lst_UC[6][1], border=0, bg='white',fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("110")).place(x = 230, y = 166+25, height=23)
        Button(self.frameOut, text=self.lst_UC[7][1], border=0, bg='white', fg="black", font=('Arial',16,'bold'), cursor="circle", command=lambda:self.ULA00("111")).place(x =230, y = 191+27, height=23)
        
    def AND(self, index):   
        self.tv_and.insert(parent='', index="end", values=int(self.num_A[index]) & int(self.num_B[index]))
        
        return int(self.num_A[index]) & int(self.num_B[index])

    def OR(self, index):
        self.tv_or.insert(parent='', index="end", values=int(self.num_A[index]) | int(self.num_B[index]))
        
        return int(self.num_A[index]) | int(self.num_B[index])

    def XOR(self, index):
        self.tv_xor.insert(parent='', index="end", values=int(self.num_A[index]) ^ int(self.num_B[index]))

        return int(self.num_A[index]) ^ int(self.num_B[index])

    def NOT(self, index):
        if self.Op_not == "A":
            self.tv_not.insert(parent='', index="end", values=self.negando(int(self.num_A[index])))

        else:
            self.tv_not.insert(parent='', index="end", values=self.negando(int(self.num_B[index])))      
    
    def negando(self, x):
        if x == 0:
            return 1
        elif x == 1:
            return 0

    def ULA00(self, operacion): 
        # AND - 100
        if operacion == "100":
            for i in self.tv_and.get_children():
                self.tv_and.delete(i)
            self.root.update()   

            self.AND(0)
            self.ULA01(operacion)

        # OR - 101
        elif operacion == "101":
            for i in self.tv_or.get_children():
                self.tv_or.delete(i)
            self.root.update() 

            self.OR(0)
            self.ULA01(operacion)
        
        # XOR - 110
        elif operacion == "110":
            for i in self.tv_xor.get_children():
                self.tv_xor.delete(i)
            self.root.update() 

            self.XOR(0)
            self.ULA01(operacion)

        # NOT - 111
        elif operacion == "111":
            for i in self.tv_not.get_children():
                    self.tv_not.delete(i)
            self.root.update()

            def A():
                self.Op_not = "A"
                self.NOT(index=0)
                self.ULA01(operacion)

                "Limpando o frameOp_A-B"
                for i in self.frame_04.winfo_children():
                    i.destroy()

            def B():
                self.Op_not = "B"
                self.NOT(index=0)
                self.ULA01(operacion)

                "Limpando o frameOp_A-B"
                for i in self.frame_04.winfo_children():
                    i.destroy()

            Button(self.frame_04, text="A", font=self.font, command=A).place(x=5, y=5)
            Button(self.frame_04, text="B", font=self.font, command=B).place(x=5, y=55)
            
        # SOMA - 000
        elif operacion == "000":
            self.carryIn = []
            self.somatorio = []
            self.lista_A = list(self.num_A)
            self.lista_A = [int(val) for val in self.lista_A]

            self.lista_B = list(self.num_B)
            self.lista_B = [int(val) for val in self.lista_B]

            self.somatorio.append(self.lista_A[2] ^ self.lista_B[2])

            if ((self.lista_A[2] ^ self.lista_B[2]) == 0) or (self.lista_A[2] == 1 and self.lista_B[2] == 1):
                if self.lista_A[2] == 0 and self.lista_B[2] == 0:
                    self.carryIn.append(0)
                else:
                    self.carryIn.append(1)
            else:
                self.carryIn.append(0)

            self.somatorio.append((self.lista_A[1] ^ self.lista_B[1]) ^ self.carryIn[0])
        
            self.ULA01(operacion)

        # SUBTRAÇÃO - 001
        elif operacion == "001":
            self.carryIn = [1]
            self.subtracao = []

            self.lista_A = list(self.num_A)[::-1]
            self.lista_A = [int(val) for val in self.lista_A]

            self.lista_B = list(self.num_B)[::-1]
            self.lista_B = [self.negando(int(val)) for val in self.lista_B]
            
            aux = str("{0:b}".format(self.carryIn[0] + self.lista_A[0] + self.lista_B[0]))
            if len(aux) == 1:
                aux = "0" + aux

            self.subtracao.append(aux[1])
            self.carryIn.append(int(aux[0]))

            self.ULA01(operacion)

        # Multiplicação - 010
        elif operacion == "010":
            self.Multiplication = []

            self.lista_A = list(self.num_A)[::-1]
            self.lista_A = [int(val) for val in self.lista_A]

            self.lista_B = list(self.num_B)[::-1]
            self.lista_B = [int(val) for val in self.lista_B]   

            self.lista_M_01 = []
            self.lista_M_02 = []
            self.lista_M_03 = []

            for i in range(0,3):
                self.lista_M_01.append(self.lista_A[0] & self.lista_B[i])

            self.ULA01(operacion)
        
        # Divisão
        elif operacion == "011":
            self.Division = ""

            self.Division = Division(int(self.num_A,2), int(self.num_B,2))
            
            self.ULA01(operacion)

    def ULA01(self, operacion):
        # AND - 100
        if operacion == "100":
            self.AND(1)
            self.ULA02(operacion)

        # OR - 101
        elif operacion == "101":
            self.OR(1)
            self.ULA02(operacion)
        
        # XOR - 110
        elif operacion == "110":
            self.XOR(1)
            self.ULA02(operacion)

        # NOT - 111
        elif operacion == "111":
            self.NOT(index=1)
            self.ULA02(operacion)
        
        # SOMA - 000
        elif operacion == "000":            
            if ((self.lista_A[1] ^ self.lista_B[1]) ^ self.carryIn[0] == 0) or (self.lista_A[1] == 1 and self.lista_B[1] == 1):
                if self.lista_A[1] == 0 and self.lista_B[1] == 0:
                    self.carryIn.append(0)
                else:
                    self.carryIn.append(1)
            else:
                self.carryIn.append(0)

            self.somatorio.append((self.lista_A[0] ^ self.lista_B[0]) ^ self.carryIn[1])

            self.ULA02(operacion)
            
        # SUBTRAÇÃO - 001
        elif operacion == "001":
            aux = str("{0:b}".format(self.carryIn[1] + self.lista_A[1] + self.lista_B[1]))
            if len(aux) == 1:
                aux = "0" + aux

            self.subtracao.append(aux[1])
            self.carryIn.append(int(aux[0]))

            self.ULA02(operacion)

        # Multiplicação - 010
        elif operacion == "010":
            for i in range(0,3):
                self.lista_M_02.append(self.lista_A[1] & self.lista_B[i])

            self.ULA02(operacion)
        
        # Divisão
        elif operacion == "011":
            
            self.ULA02(operacion)

    def ULA02(self,operacion):
        # AND - 100
        if operacion == "100":
            self.AND(2)

        # OR - 101
        elif operacion == "101":
            self.OR(2)
        
        # XOR - 110
        elif operacion == "110":
            self.XOR(2)
        
        # NOT - 111
        elif operacion == "111":
            self.NOT(index=2)

        # SOMA - 000
        elif operacion == "000":
            if ((self.lista_A[0] ^ self.lista_B[0]) == 0) or (self.lista_A[0] == 1 and self.lista_B[0] == 1):
                if self.lista_A[0] == 0 and self.lista_B[0] == 0:
                    self.carryIn.append(0)
                else:
                    self.carryIn.append(1)
            else:
                self.carryIn.append(0)

            Label(self.frameOut, text="ADDITION", font=self.font, bg="orange").place(x=30, y=10)
            Label(self.frameOut, text=self.somatorio[::-1], font=self.font, bg="orange").place(x=60, y=40)
            
            Label(self.frame_03, text=int("".join(list(map(str, self.somatorio[::-1]))),2), bg="orange", font=self.font).place(x=310, y=130)
            
            "Limpando as listas"
            self.somatorio.clear()
            self.carryIn.clear()

        # SUBTRAÇÃO - 001
        elif operacion == "001":
            aux = str("{0:b}".format(self.carryIn[2] + self.lista_A[2] + self.lista_B[2]))
            if len(aux) == 1:
                aux = "0" + aux

            self.subtracao.append(aux[1])
            self.carryIn.append(int(aux[0]))

            Label(self.frameOut, text="SUBTRACTION", font=self.font, bg="orange").place(x=15, y=80)
            Label(self.frameOut, text=self.subtracao[::-1], font=self.font, bg="orange").place(x=60, y=110)
            
            Label(self.frame_03, text=int("".join(list(map(str, self.subtracao[::-1]))),2), bg="orange", font=self.font).place(x=310, y=130)

            "Limpando as listas"
            self.subtracao.clear()
            self.carryIn.clear()
        
        # Multiplicação - 010
        elif operacion == "010":
            for i in range(0,3):
                self.lista_M_03.append(self.lista_A[2] & self.lista_B[i])

            self.carryIn = [0]
            self.Multiplication.append(int(self.lista_M_01[0]))

            aux = str("{0:b}".format(self.carryIn[0] + self.lista_M_01[1] + self.lista_M_02[0]))
            if len(aux) == 1:
                aux = "0" + aux 

            self.Multiplication.append(int(aux[1]))
            self.carryIn.append(int(aux[0]))

            aux = str("{0:b}".format(self.carryIn[1] + self.lista_M_01[2] + self.lista_M_02[1] + self.lista_M_03[0]))
            if len(aux) == 1:
                aux = "0" + aux 

            self.Multiplication.append(int(aux[1]))
            self.carryIn.append(int(aux[0]))

            aux = str("{0:b}".format(self.carryIn[2] + self.lista_M_02[2] + self.lista_M_03[1]))
            if len(aux) == 1:
                aux = "0" + aux 

            self.Multiplication.append(int(aux[1]))
            self.carryIn.append(int(aux[0]))

            self.Multiplication.append(int(self.lista_M_03[2]))
            
            Label(self.frameOut, text="MULTIPLICATION", font=self.font, bg="orange").place(x=5, y=150)
            Label(self.frameOut, text=self.Multiplication[::-1][2:], font=self.font, bg="orange").place(x=60, y=180)
            
            Label(self.frame_03, text=int("".join(list(map(str, self.Multiplication[::-1]))),2), bg="orange", font=self.font).place(x=310, y=130)

            "Limpando as listas"
            self.Multiplication.clear()
            self.carryIn.clear()

        # Divisão
        elif operacion == "011":
            Label(self.frameOut, text="DIVISION", font=self.font, bg="orange").place(x=38, y=220)
            
            if self.num_B != "001":
                if len(self.Division) == 1:
                    lista = []
                    lista.append(0)
                    lista.append(0)
                    lista.append(self.Division[0])
                    self.Division.clear()
                    self.Division = lista

                elif len(self.Division) == 2:
                    lista = []
                    lista.append(0)
                    lista.append(self.Division[0])
                    lista.append(self.Division[1])
                    self.Division.clear()
                    self.Division = lista

            Label(self.frameOut, text=self.Division, font=self.font, bg="orange").place(x=60, y=250)
            Label(self.frame_03, text=int("".join(list(map(str, self.Division))),2), bg="orange", font=self.font).place(x=310, y=130)

ULA()            