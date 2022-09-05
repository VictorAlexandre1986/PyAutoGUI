import pyautogui

#A função click() simula um único clique no botão esquerdo do mouse na posição atual do mouse.
#Um "clique" é definido como apertar o botão e liberá-lo

pyautogui . click ()  # click the mouse

#Para combinar uma chamada moveTo() antes do clique,
#passe inteiros para o argumento de palavra-chave y :

pyautogui . click ( x = 100 , y = 200 )  # move to 100, 200, then click the left mouse button.

#Para especificar um botão diferente do mouse para clicar, passe 'left' , 'middle' ou 'right'

pyautogui . click ( button = 'right' )  # right-click the mouse




#Para fazer vários cliques, passe um inteiro para o argumento da palavra-chave clicks . Opcionalmente,
#você pode passar um float ou inteiro para o argumento de palavra-chave interval para especificar a quantidade de
#pausa entre os cliques em segundos

#pyautogui . click ( clicks = 2 )  # double-click the left mouse button
#pyautogui . click ( clicks = 2 , interval = 0.25 )  # double-click the left mouse button, but with a quarter second pause in between clicks
#pyautogui . click ( button = 'right' , clicks = 3 , interval = 0.25 )  ## triple-click the right mouse button with a quarter second pause in between clicks




##Como um atalho conveniente, a função doubleClick() executará um duplo clique do botão esquerdo do mouse.
pyautogui . doubleClick ()  # perform a left-button double click


pyautogui . mouseDown ();
