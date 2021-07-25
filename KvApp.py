from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
Builder.load_file("KvGui.kv")
class CalculoScreen(Screen):
    display = ObjectProperty(None)
class SobreScreen(Screen):
    pass
class AjudaScreen(Screen):
    pass
class MeuScreenManager(ScreenManager):
    pass
class ZigaCalculadora(App):
    cs = MeuScreenManager().get_screen('calculo_screen')  
    num1 = 0 
    num2 = 0 
    resultado = 0
    operacao = "nenhuma"
    txt_display = ""
    var = StringProperty("")
    opr = ""
    ligada = True
    def digitos(self, num, resultado, op):
        if resultado == "":
            self.num1 = float(num)             
        if op ==  "nenhuma":            
            self.txt_display += num 
            self.num1 = self.txt_display           
        elif op !=  "nenhuma":                 
            self.txt_display = num
            self.num1 = self.txt_display
            self.operacao = "nenhuma"
        return self.txt_display 
    def on_ce(self):
        self.num1 = 0 
        self.num2 = 0 
        self.txt_display = " 0"
        self.operacao = "nenhuma"
        self.ligada = True
        return self.txt_display
    def desligar(self):
        self.ligada = False
    def igualdade(self, op):
        self.num2 = float(self.txt_display)        
        if op == "soma":   
            self.resultado = str(float(self.num1) + float(self.num2))
            self.num1 = self.resultado            
            return self.resultado
        elif op == "diferenca":                    
            self.resultado =  str(float(self.num1) - float(self.num2))
            self.num1 = self.resultado        
            return self.resultado
        elif op == "produto":                        
            self.resultado =  str(float(self.num1) * float(self.num2))
            self.num1 = self.resultado            
            return self.resultado
        elif op == "razao":            
            if self.num2 != 0:                                
                self.resultado =  str(float(self.num1) / float(self.num2))
                self.num1 = self.resultado                
                return self.resultado
            else:
                return "ERRO"
        elif op == "raiz":                         
            self.resultado = str(round((float(self.num2) ** (0.5)),3))
            self.num1 = self.resultado
            self.num2 = 0
            return self.resultado
        elif op == "porcentagem":
            return "Não Implementado"                   
        if op == "produto":
            return  str(self.num1 * self.num2)              
    def calcular(self,  op):                
        self.txt_display = " "        
        if op == 'soma':                        
            self.opr = "soma"
            #return 'soma'
        elif op == 'diferenca':                        
            self.opr = "diferenca"
            #return 'diferenca'
        elif op == 'produto':                        
            self.opr = "produto" 
            #return 'produto'
        elif op == 'razao':                        
            self.opr = "razao"
            #return 'razao'
        elif op == 'porcentagem':                        
            self.opr = "porcentagem" 
            #return 'porcentagem'
        elif op == 'raiz':                        
            self.opr = "raiz"
            #return 'raiz'
    def build(self):
        App.title = "Ziga Calculadora"
        Window.size = (320,480)
        MeuScreenManager().current = "calculo_screen"
        return MeuScreenManager()
if __name__ == "__main__":
    ZigaCalculadora().run()