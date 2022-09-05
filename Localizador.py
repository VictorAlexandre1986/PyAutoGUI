import pyautogui

pyautogui.click()

try:
    #É possivel localizar um item na tela desde que voce tenha uma imagem dele
    caixaTexto = pyautogui.locateOnScreen('procurar.png', confidence = 0.9)

    #x,y = pyautogui.locateCenterOnScreen ('procurar.jpg')
    coordenada = pyautogui.center(caixaTexto)

    print(coordenada)

    pyautogui.moveTo(coordenada.x,coordenada.y)

except :
    print('Não localizou')

