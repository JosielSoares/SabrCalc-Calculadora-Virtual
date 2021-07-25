'''
SabrCalc calculadora 3d no blender v.0.1.01
Programador: Josiel Soares "Ziga Multimedia"
Youtube: https://www.youtube.com/c/ZigaMultimedia
Framework: Verifique também a implementação com o Framework Kivy
Engine: Futura implementação com o Motor de Jogo UpBGE

Teclas de Atalhos:
    1) Botão Esquerdo e clique em cada tecla para acionar o número
    ou operacão matemática
    2) Botão Direito pressionado com arrastar do mouse para rotacionar
    a cãmera principal em torno da calculadora
    3) Pressionamento da tecla O "ó" para ativar a animaçao de localização
    padrão da câmera

'''
import bge
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
saida = scene.objects['Text']
operacao = "";
# Para acionar o clique do mouse
mbutton = cont.sensors['mbutton']
# Para acionar as teclas numericas
mo_0 = cont.sensors['mo_0']
mo_1 = cont.sensors['mo_1']
mo_2 = cont.sensors['mo_2']
mo_3 = cont.sensors['mo_3']
mo_4 = cont.sensors['mo_4']
mo_5 = cont.sensors['mo_5']
mo_6 = cont.sensors['mo_6']
mo_7 = cont.sensors['mo_7']
mo_8 = cont.sensors['mo_8']
mo_9 = cont.sensors['mo_9']
#Para acionar as teclas de funções
mo_b = cont.sensors['mo_b'] # mouse over no botao de igualdade
mo_c = cont.sensors['mo_c'] # mouse over no botao de soma
mo_d = cont.sensors['mo_d'] # mouse over no botao de subtracao
mo_e = cont.sensors['mo_e'] # mouse over no botao de multiplicacao
mo_f = cont.sensors['mo_f'] # mouse over no botao de divisao 
# o botao de ligar
mo_j = cont.sensors['mo_j']
# o botao de desligar
mo_i = cont.sensors['mo_i']
def ligar():
    own['valor1'] = 0
    own['valor2'] = 0
    own['resultado']  = 0
    own['operacao'] = ""
    own['auxiliar'] = ""
    own['ligado'] = True
def desligar():
    own['valor1'] = 0
    own['valor2'] = 0
    own['resultado']  = ""
    own['operacao'] = ""
    own['auxiliar'] = ""
    own['ligado'] = False
def somar(a,b):
    if (str(own['resultado'] )!=""):
        own['resultado'] =  str(a + b)
def subtrair(a,b):
    if (str(own['resultado'] )!=""):
        own['resultado'] =  str(a - b)
def multiplicar(a,b):
    if (str(own['resultado'] )!=""):
        own['resultado'] =  str(a * b)
def dividir(a,b):
    if (str(own['resultado'] )!=""):
        if own['valor2'] !=0:
            own['resultado'] =  str(a / b)
        else:  
            own['resultado']  = "ERRO"  
def comparar_resultado():
    if own['resultado']  != "":
        own['auxiliar'] = own['resultado']        
if mo_j.positive and mbutton.positive:
    ligar() 
if mo_i.positive and mbutton.positive:
    desligar()          
def adicionar_numeros():
    if len(saida['Text']) <8 and own['ligado']==True:
        #Para adicionar o primeiro valor:
        if own['operacao']  == "" and own['valor1'] == 0 and own['valor2'] == 0:
            if mo_0.positive and mbutton.positive:
                if own['operacao']!="":
                    own['valor1'] = 0
                    own['resultado']  = 0               
                else:
                    own['valor2'] = 0
                    own['resultado']  =  0              
            if mo_1.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = 1
                    own['resultado']  =  1
                else:
                    own['valor2'] = 1  
                    own['resultado']  =  1          
            if mo_2.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = 2
                    own['resultado']  =  2
                else:
                    own['valor2'] = 2  
                    own['resultado']  =  2          
            if mo_3.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = 3
                    own['resultado']  =  3
                else:
                    own['valor2'] = 3    
                    own['resultado']  =  3         
            if mo_4.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = 4
                    own['resultado']  =  4
                else:
                    own['valor2'] = 4   
                    own['resultado']  =  4          
            if mo_5.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = 5
                    own['resultado']  =  5
                else:
                    own['valor2'] = 5    
                    own['resultado']  =  5         
            if mo_6.positive and mbutton.positive:   
                if own['operacao']=="":
                    own['valor1'] = 6
                    own['resultado']  =  6
                else:
                    own['valor2'] = 6  
                    own['resultado']  =  6            
            if mo_7.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = 7
                    own['resultado']  =  7
                else:
                    own['valor2'] = 7      
                    own['resultado']  =  7       
            if mo_8.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = 8
                    own['resultado']  =  8
                else:
                    own['valor2'] = 8    
                    own['resultado']  =  8         
            if mo_9.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = 9
                    own['resultado']  =  9
                else:
                    own['valor2'] = 9   
                    own['resultado']  =  9
        #Agora para adicionar caso ja exista algum numero
        else:
            if mo_0.positive and mbutton.positive:
                if own['operacao']!="":
                    own['valor1'] = int(saida['Text'] + str(0))
                    own['resultado']  =  int(saida['Text']+ str(0))            
                else:
                    own['valor2'] = int(saida['Text'] + str(0))
                    own['resultado']  =  int(saida['Text']+ str(0))            
            if mo_1.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(1))
                    own['resultado']  =  int(saida['Text']+ str(1))
                else:
                    own['valor2'] = int(saida['Text'] + str(1))  
                    own['resultado']  =  int(saida['Text']+ str(1))          
            if mo_2.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(2))
                    own['resultado']  =  int(saida['Text']+ str(2)) 
                else:
                    own['valor2'] = int(saida['Text'] + str(2))  
                    own['resultado']  =  int(saida['Text']+ str(2))           
            if mo_3.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(3))
                    own['resultado']  =  int(saida['Text']+ str(3))
                else:
                    own['valor2'] = int(saida['Text'] + str(3))   
                    own['resultado']  =  int(saida['Text']+ str(3))         
            if mo_4.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(4))
                    own['resultado']  =  int(saida['Text']+ str(4))
                else:
                    own['valor2'] = int(saida['Text'] + str(4))  
                    own['resultado']  =  int(saida['Text']+ str(4))          
            if mo_5.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(5))
                    own['resultado']  =  int(saida['Text']+ str(5))
                else:
                    own['valor2'] = int(saida['Text'] + str(5))    
                    own['resultado']  =  int(saida['Text']+ str(5))         
            if mo_6.positive and mbutton.positive:   
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(6))
                    own['resultado']  =  int(saida['Text']+ str(6))
                else:
                    own['valor2'] = int(saida['Text'] + str(6))  
                    own['resultado']  =  int(saida['Text']+ str(6))            
            if mo_7.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(7))
                    own['resultado']  =  int(saida['Text']+ str(7))
                else:
                    own['valor2'] = int(saida['Text'] + str(7))      
                    own['resultado']  = int(saida['Text']+ str(7))       
            if mo_8.positive and mbutton.positive: 
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(8))
                    own['resultado']  =  int(saida['Text']+ str(8))
                else:
                    own['valor2'] = int(saida['Text'] + str(8))    
                    own['resultado']  =  int(saida['Text']+ str(8))         
            if mo_9.positive and mbutton.positive:
                if own['operacao']=="":
                    own['valor1'] = int(saida['Text'] + str(9))
                    own['resultado']  =  int(saida['Text']+ str(9))
                else:
                    own['valor2'] = int(saida['Text'] + str(9))  
                    own['resultado']  =  int(saida['Text']+ str(9))
# Eventos disparados ao clicar no botao "="          
if mo_b.positive and mbutton.positive and own['auxiliar'] == "":
    if own['operacao'] == "soma":
        somar(own['valor1'],own['valor2'])
    if own['operacao'] == "subtracao":
        subtrair(own['valor1'],own['valor2'])
    if own['operacao'] == "multiplicacao":
        multiplicar(own['valor1'],own['valor2'])
    if own['operacao'] == "divisao":
        dividir(own['valor1'],own['valor2'])
    own['operacao'] = ""
    own['valor1'] = 0
    own['valor2'] = 0
elif mo_b.positive and mbutton.positive and own['auxiliar'] != "":
    if own['operacao'] == "soma":
        somar(float(own['auxiliar']),own['valor2'])
    if own['operacao'] == "subtracao":
        subtrair(float(own['auxiliar']),own['valor2'])
    if own['operacao'] == "multiplicacao":
        multiplicar(float(own['auxiliar']),own['valor2'])
    if own['operacao'] == "divisao":
        dividir(float(own['auxiliar']),own['valor2'])
    own['operacao'] = ""
    own['valor1'] = 0
    own['valor2'] = 0
if mo_c.positive and mbutton.positive:
    comparar_resultado()
    own['resultado']  = ""
    own['operacao'] = "soma"      
if mo_d.positive and mbutton.positive:
    comparar_resultado()
    own['resultado']  = ""
    own['operacao'] = "subtracao"
if mo_e.positive and mbutton.positive:
    comparar_resultado()
    own['resultado']  = ""
    own['operacao'] = "multiplicacao"
if mo_f.positive and mbutton.positive:
    comparar_resultado()
    own['resultado']  = ""
    own['operacao'] = "divisao"           
adicionar_numeros()
#Para mostrar o resultado no display com o limite de 8 caracteres
saida['Text'] = str(own['resultado'][0:9])
