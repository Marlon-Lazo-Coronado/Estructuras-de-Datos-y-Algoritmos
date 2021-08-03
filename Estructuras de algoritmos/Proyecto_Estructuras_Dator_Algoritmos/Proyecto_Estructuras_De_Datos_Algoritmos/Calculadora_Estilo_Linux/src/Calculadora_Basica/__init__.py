import wx
import string
from pythonds import Stack
#wx.TextCtrl permite ingrezar una cadena de caracteres y puede mostrar la info en el
#xw.StaticText() no permite editar pero si mostrar

class Calculadora(wx.Frame):
    def __init__(self, parent, title): #Parametros de la ventana
        wx.Frame.__init__(self, parent = parent, title = title, size = (400,300)) #Constructor
        ubicador = wx.BoxSizer(wx.VERTICAL) #Para no poner cordenadas del los controles
        mensaje_1 = wx.StaticText(self, -1, u"infix to postfix Calculator");
        mensaje_1.SetForegroundColour("#FFFF")
        self.cuadro_texto = wx.TextCtrl(self, style = wx.TE_MULTILINE) #Cuadro de texto con salto del linea
        self.boton_calcular_posfix = wx.Button(self, -1, u"Calcular postfix", size = (90,20)) #Boton
        self.boton_calcular_infix_postfix = wx.Button(self, -1, u"INFIX a POSTFIX", size = (90,20)) #Boton
        self.boton_borrar = wx.Button(self, -1, u"Borrar", size = (90,20)) #Boton
        
        ubicador.Add(mensaje_1, 1, wx.EXPAND | wx.ALL, 5)
        ubicador.Add(self.cuadro_texto,10, wx.EXPAND | wx.ALL, 5) #(control,proporcion,ubicacion y expancion con pixeles de margen)
        ubicador.Add(self.boton_calcular_posfix,3, wx.ALIGN_LEFT | wx.ALL, 3)
        ubicador.Add(self.boton_calcular_infix_postfix,3, wx.ALIGN_LEFT | wx.ALL, 3)
        ubicador.Add(self.boton_borrar,3, wx.ALIGN_LEFT | wx.ALL, 3) #Le ponemos self. a los botones por si ocupamos usarlos como variable
        
        #Color de fondo de la ventana
        color = wx.Colour(20, 30, 300)
        self.SetBackgroundColour(color)
        self.Refresh()#eraseBackground=True, rect=None
        
        #Eventos
        #Poner aqui la funcion que se va a invocar con el boton
        self.Bind(wx.EVT_BUTTON, self.calcular, self.boton_calcular_posfix) #(tipo de evento, funcion de la clase que recibe, de donde viene el evento)
        self.Bind(wx.EVT_BUTTON, self.infix_postfix, self.boton_calcular_infix_postfix)
        self.Bind(wx.EVT_BUTTON, self.borrar, self.boton_borrar)
        
        #Invocaciones
        self.SetSizer(ubicador)
        self.Centre(True)
        self.Show()
        
    #Funcion que invoca boton_borrar 
    def borrar(self,event): #Esos argumentos son obligatorios
        #Con esta funcion podemos distingir los botones, creo que eso sirve mas si usamos una sola funcion para todos los botones y no repetir tanto codigo
        #Si se hace esto, quitar los nombre del los botones en la funcion de eventos y dejar solo una
        boton_i = event.GetEventObject().GetLabel();
        if boton_i == u"Borrar":
            self.cuadro_texto.SetLabelText(boton_i)
            print(1+3-8)
        else:
            print("No se seleciono el boton: ", boton_i) #Esta parte no funciona porque solo self.boton_borrar llama a esta funcion
            
    def infix_postfix(self,event): #Esos argumentos son obligatorios
        strin = self.cuadro_texto.GetValue() #Con esta funcion obtenemos lo que se escribio en el cuadro
        self.cuadro_texto.SetLabelText("El resultado es:  " + self.infixToPostfix(strin))
        
    def calcular(self,event): #Esos argumentos son obligatorios
        strin = self.cuadro_texto.GetValue() #Con esta funcion obtenemos lo que se escribio en el cuadro
        self.cuadro_texto.SetLabelText("El resultado es:  " + str(self.postfixEval(self.infixToPostfix(strin))))
        #print(self.infixToPostfix(strin))
        #a = 100;
        #numero_prueba = str(a)
        #self.cuadro_texto.SetLabelText(numero_prueba) #Con esto podemos imprimir el resultado como string
        
        
    def infixToPostfix(self,infixexpr):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = Stack()
        postfixList = []
        tokenList = infixexpr.split()

        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                        postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)
            

    def postfixEval(self,postfixExpr):
        operandStack = Stack()
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = self.doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()

    def doMath(self,op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

    #return postfixEval('7 8 + 3 2 + /')

if __name__ == '__main__':
    app = wx.App()
    frame = Calculadora(None, u"Calculadora Estilo Linux")
    app.MainLoop()
