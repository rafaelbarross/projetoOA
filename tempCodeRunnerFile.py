from PySimpleGUI import PySimpleGUI as sg
from time import sleep

sg.theme('DarkBlue')

layout = [
    [sg.Text("""\n  === Olá estudante, isso é um Objeto de Aprendizagem (OA) ===
- O assunto que iremos ver é: The Present Continuous Tense/Inglês -\n
Não se preocupe, iremos tirar todas as suas duvidas (-_-)7

Bons estudos! :) \n""")]
]

janela = sg.Window("Tela de boas vindas", layout)