<MeuScreenManager>:
    CalculoScreen:
        id: calculo_screen
        name: "calculo_screen"
    SobreScreen:
        id: sobre_screen
        name: "sobre_screen"
    AjudaScreen:
        id: ajuda_screen
        name: "ajuda_screen"
<AjudaScreen>: 
    BoxLayout:
        orientation: "vertical"  
        Label:        
            text: "Tela de Ajuda"  
            size_hint_y: 0.9
        Button:
            text: "Voltar"
            size_hint_y: 0.1
            on_release: app.root.current = "calculo_screen"
<CalculoScreen>:
    display: display 
    BoxLayout:
        orientation: "vertical"  
        Label:  
            size_hint_y: 0.1
            text: "Ziga Calculadora"
        TextInput: 
            id: display  
            size_hint_y: 0.1
            hint_text: " 0"
            disabled: True
        GridLayout: 
            cols: 4
            rows: 6
            size_hint_y: 0.6
            Button:
                id: btn_once
                text: "ON | CE"
                on_release: root.ids.display.text = app.on_ce()
            Button:
                id: btn_mrc
                text: "MRC"
                on_release: root.ids.display.text="MRC"
            Button:
                id: btn_mmen
                text: "M-"
                on_release: root.ids.display.text="M-"
            Button:
                id: btn_mma
                text: "M+"
                on_release: root.ids.display.text="M+"
            Button:
                id: btn_off
                text: "OFF"
                on_release: 
                    root.ids.display.text = "OFF"  
                    #app.desligar()
            Button:
                id: btn_raiz
                text: "√"
                on_release: app.calcular("raiz")
            Button:
                id: btn_porc
                text: "%"
                on_release:  
                    root.ids.display.text="Porcentagem"
                    #app.calcular("porcentagem")
            Button:
                id: btn_div
                text: "÷"
                on_release:  app.calcular("razao")
            Button:
                id: btn_sete
                text: "7"
                on_release: root.ids.display.text = app.digitos("7", app.txt_display, app.operacao)
            Button:
                id: btn_oito
                text: "8"
                on_release: root.ids.display.text = app.digitos("8", app.txt_display, app.operacao)
            Button:
                id: btn_nove
                text: "9"
                on_release: root.ids.display.text = app.digitos("9", app.txt_display, app.operacao)
            Button:
                id: btn_vez
                text: "x"
                on_release: app.calcular("produto")
            Button:
                id: btn_quatro
                text: "4"
                on_release: root.ids.display.text = app.digitos("4", app.txt_display, app.operacao)
            Button:
                id: btn_cinco
                text: "5"
                on_release: root.ids.display.text = app.digitos("5", app.txt_display, app.operacao)
            Button:
                id: btn_seis
                text: "6"
                on_release: root.ids.display.text = app.digitos("6", app.txt_display, app.operacao)
            Button:
                id: btn_menus
                text: "-"
                on_release: app.calcular("diferenca")
            Button:
                id: btn_um
                text: "1"
                on_release: root.ids.display.text = app.digitos("1", app.txt_display, app.operacao)
            Button:
                id: btn_dois
                text: "2"
                on_release: root.ids.display.text = app.digitos("2", app.txt_display, app.operacao)
            Button:
                id: btn_trez
                text: "3"
                on_release: root.ids.display.text = app.digitos("3", app.txt_display, app.operacao)
            Button:
                id: btn_mais
                text: "+"
                on_release:  
                    #root.ids.display.text = " "
                    app.calcular("soma")
            Button:
                id: btn_zero
                text: "0"
                on_release: root.ids.display.text = app.digitos("0", app.txt_display, app.operacao)
            Button:
                id: btn_dec
                text: "."
                on_release: root.ids.display.text="Decimal"
            Button:
                id: btn_rnd
                text: "Rnd"
                on_release: root.ids.display.text="Aleatório"
            Button:
                id: btn_igual
                text: "="
                on_release: root.ids.display.text = app.igualdade(app.opr)
        BoxLayout:
            orientation: "vertical"
            size_hint_y: 0.2
            Button:
                text: "Ajuda?" 
                on_release: app.root.current = "ajuda_screen"
            Button:
                text: "Sair"   
                on_release: app.stop()
<SobreScreen>:  
    BoxLayout:
        orientation: "vertical"     
        Label:        
            text: "Tela de Sobre"
        Button:
            text: "Ajuda?"
            on_release: app.root.current = "ajuda_screen"
