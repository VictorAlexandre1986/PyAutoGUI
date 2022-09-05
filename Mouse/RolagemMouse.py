import pyautogui

#deixe o mouse sobre a janela maximizada(em segundo plano) e com conteudo para rolagem
#a janela do editor nao pode estar maximizada

pyautogui . click ()  # click the mouse

#A roda de rolagem do mouse pode ser simulada chamando a função scroll() e
#passando um número inteiro de “cliques” para rolar. A quantidade de rolagem
#em um "clique" varia entre as plataformas.

pyautogui . scroll ( -800 )

#pyautogui . scroll ( 800 )   # scroll up 10 "clicks"
#pyautogui . scroll ( - 10 )  # scroll down 10 "clicks"
#pyautogui . scroll ( 10 , x = 100 , y = 100 )  # move mouse cursor to 100, 200, then scroll up 10 "clicks"


#Nas plataformas OS X e Linux, o PyAutoGUI
#também pode executar a rolagem horizontal chamando a função hscroll ()

#pyautogui . hscroll ( 10 )   # scroll right 10 "clicks"
#pyautogui . hscroll ( - 10 )   # scroll left 10 "clicks"
