import pyautogui

#Obtendo as dimensões da resolução da tela
screenWidth , screenHeight = pyautogui . size ()

#Vai mover o mouse para o centro da tela tanto na vertical quanto na horizontal
pyautogui . moveTo ( screenWidth / 2 , screenHeight / 2 )

#Movimentação do mouse :
#pyautogui . moveTo ( 100 , 200 )   # moves mouse to X of 100, Y of 200.
#ou pyautogui . moveTo ( None , 500 )  # moves mouse to X of 100, Y of 500.
#ou pyautogui . moveTo ( 600 , None )  # moves mouse to X of 600, Y of 500.


#Normalmente, o cursor do mouse se moverá instantaneamente para as novas
#coordenadas. Se você quiser que o mouse se mova gradualmente para o novo local,
#passe um terceiro argumento pela duração (em segundos) que o movimento deve
#tomar. Por exemplo:

#pyautogui . moveTo ( 100 , 200 , 2 )   # moves mouse to X of 100, Y of 200 over 2 seconds


pyautogui.moveTo(100,200,8)

#Se você quiser mover o cursor do mouse sobre alguns pixels em relação à sua posição atual,
#use a função move() . Essa função tem parâmetros semelhantes como moveTo()

#pyautogui . dragTo ( 100 , 200 , button = 'left' )     # drag mouse to X of 100, Y of 200 while holding down left mouse button
#pyautogui . dragTo ( 300 , 400 , 2 , button = 'left' )  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
#pyautogui . drag ( 30 , 0 , 2 , button = 'right' )   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button








#Uma função de interpolação ou atenuação dita o progresso do mouse conforme ele se move para seu destino.
#Normalmente, ao mover o mouse por um período de tempo
pyautogui . moveTo ( 100 , 100 , 2 , pyautogui . easeInElastic )
pyautogui . moveTo ( 200 , 100 , 2 , pyautogui . easeInQuad )     # start slow, end fast
pyautogui . moveTo ( 300 , 100 , 2 , pyautogui . easeOutQuad )    # start fast, end slow
pyautogui . moveTo ( 400 , 100 , 2 , pyautogui . easeInOutQuad )  # start and end fast, slow in middle
pyautogui . moveTo ( 500 , 100 , 2 , pyautogui . easeInBounce ) 


