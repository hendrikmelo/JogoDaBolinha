from graphics import *
import random


win = GraphWin("Bolinha", 800, 600)
win.setBackground(color_rgb(0, 0, 0))

menu = Text(Point(400, 200), "MENU")
menu.setSize(36)
menu.setStyle("bold")
menu.setTextColor(color_rgb(255, 255, 0))
menu.draw(win)

start = Text(Point(400, 300), "START")
start.setSize(30)
start.setTextColor(color_rgb(255, 255, 0))
info = Text(Point(400, 325), "press enter")
info.setTextColor(color_rgb(255, 255, 0))
start.draw(win)
info.draw(win)

credits = Text(Point(400, 400), "CREDITS")
info2 = Text(Point(400, 425), "press space")
info2.setTextColor(color_rgb(255, 255, 0))
credits.setSize(30)
credits.setTextColor(color_rgb(255, 255, 0))
credits.draw(win)
info2.draw(win)

quit = Text(Point(400, 500), "QUIT")
info3 = Text(Point(400, 525), "press esc")
info3.setTextColor(color_rgb(255, 255, 0))
quit.setSize(30)
quit.setTextColor(color_rgb(255, 255, 0))
quit.draw(win)
info3.draw(win)
proceed = win.getKey()


def main(new, nome):
  linhaSuperior = Line(Point(0, 40), Point(800, 40))
  linhaSuperior.setWidth(10)
  linhaSuperior.setFill(color_rgb(255, 255, 0))
  linhaSuperior.draw(new)

  linhaInferior = Line(Point(0, 550), Point(800, 550))
  linhaInferior.setWidth(3)
  linhaInferior.setFill(color_rgb(255, 255, 0))
  linhaInferior.draw(new)

  col = 390
  lin = 60
  pontuacao = 0

  circulo = Circle(Point(col, lin), 15)
  circulo.setFill(color_rgb(255, 255, 255))
  circulo.draw(new)

  pontos = Text(Point(400, 575), "Pontos: " + str(pontuacao))
  pontos.setTextColor(color_rgb(255, 255, 255))
  pontos.setSize(14)
  pontos.draw(new)

  colIni = 340
  barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
  barra.setFill(color_rgb(255, 255, 0))
  barra.setWidth(10)
  barra.draw(new)

  vida = 3
  vidas = Text(Point(175, 575), "Vidas: " + str(vida))
  vidas.setTextColor(color_rgb(255, 0, 0))
  vidas.setSize(14)
  vidas.draw(new)

  velocidade = 15
  bateu = True
  continuar = True
  while continuar:

      if bateu:
          passo = int(random.random() * 5) + 1
          sorteio = random.random()
          print(sorteio)
          if sorteio < .3:
              print(passo)
              passo = -passo
              print(passo)
          bateu = False

      if (col + passo) > 800:
          passo = -passo

      if (col + passo) < 0:
          passo = - passo

      if (lin + velocidade) < 50:
          velocidade = - velocidade

      if (lin + velocidade) > 510:
          print (vida)
          if colIni < col and col < colIni + 100:
              velocidade = - velocidade
              pontuacao += 1
              pontos.undraw()
              pontos = Text(Point(400, 575), "Pontos: " + str(pontuacao))
              pontos.setTextColor(color_rgb(255, 255, 255))
              pontos.setSize(14)
              pontos.draw(new)
              if pontuacao % 3 ==0:
                  if velocidade < 35:
                      velocidade *= 1.1
              bateu = True


          else:
              vida -= 1
              col = 390
              lin = 60
              velocidade = 15
              vidas.undraw()
              vidas = Text(Point(175, 575), "Vidas: " + str(vida))
              vidas.setTextColor(color_rgb(255, 0, 0))
              vidas.setSize(14)
              vidas.draw(new)

          if vida == 0:
              print(vida)
              continuar = False

      # Nova posição do círculo
      circulo.undraw()
      col += passo
      lin += velocidade
      circulo = Circle(Point(col, lin), 15)
      circulo.setFill(color_rgb(255, 255, 255))
      circulo.draw(new)

      # Movimento horizontal da barra pelas setas direita/esquerda
      tecla = new.checkKey()

      # Sair do joguinho
      if tecla == "Escape":
          continuar = False
          continue

      if tecla == "Right":
          if (colIni + 20) < 701:
              colIni = colIni + 20

      barra.undraw()
      barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
      barra.setFill(color_rgb(255, 255, 0))
      barra.setWidth(10)
      barra.draw(new)

      if tecla == "Left":
          if (colIni - 20) > -1:
              colIni = colIni - 20

      barra.undraw()
      barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
      barra.setFill(color_rgb(255, 255, 0))

      barra.setWidth(10)
      barra.draw(new)

      # Esperar o ser humano reagir
      time.sleep(.035)
  rec = Rectangle(Point(0, 0), Point(800, 600))
  rec.setFill(color_rgb(0, 0, 0))
  rec.draw(new)

  score1 = str(pontuacao)

  score = Text(Point(400, 300), "SUA PONTUAÇÃO, " + str(nome.getText()) +", É : " + score1)
  score.setSize(15)
  score.setTextColor(color_rgb(255, 255, 0))
  score.setStyle('bold')
  score.draw(new)

  piscando = True

  while piscando:
      tryagain = Text(Point(400, 550), "TRY AGAIN ?!?")
      tryagain.setSize(15)
      tryagain.setTextColor(color_rgb(255, 255, 0))
      tryagain.setStyle('bold')
      tryagain.draw(new)
      tryagain.undraw()

      eoq = new.checkKey()
      if eoq == "Escape":
          new.close()

      if eoq == "Return":
          score.undraw()

          piscando = False
          main(new, nome)

  new.getMouse()

if proceed == "Return":


  win.close()

  jan = GraphWin("Bolinha", 800, 600)
  jan.setBackground(color_rgb(0, 0, 0))

  nome = Entry(Point(400, 300), 10)
  nome.draw(jan)

  jan.getMouse()

  if proceed == "Return":
      jan.getKey()
      jan.close()

      new = GraphWin("Bolinha", 800, 600)
      new.setBackground(color_rgb(0, 0, 0))

      main(new, nome)
      new.close()

      new.getKey()
      new.close()

else:
  if proceed == "space":
      win.close()

      newWin2 = GraphWin("Bolinha", 800, 600)
      newWin2.setBackground(color_rgb(0, 0, 0))

      thanks = Text(Point(400, 50), "Made by:")
      thanks.setStyle("italic")
      thanks.setSize(30)
      thanks.setTextColor(color_rgb(255, 255, 0))
      thanks.draw(newWin2)

      nome = Text(Point(400, 150), "HENDRIK RODRIGUES MELO")
      nome.setSize(20)
      nome.setTextColor(color_rgb(255, 255, 0))
      nome.draw(newWin2)

      nome = Text(Point(400, 250), "PAOLA DAGHER DE ALMEIDA")
      nome.setSize(20)
      nome.setTextColor(color_rgb(255, 255, 0))
      nome.draw(newWin2)

      nome = Text(Point(400, 350), "RODRIGO LLURDA MENEZES SANTOS")
      nome.setSize(20)
      nome.setTextColor(color_rgb(255, 255, 0))
      nome.draw(newWin2)

      nome = Text(Point(400, 450), "THAYLANE KAREM FORNAZIERE XAVIER")
      nome.setSize(20)
      nome.setTextColor(color_rgb(255, 255, 0))
      nome.draw(newWin2)

      newWin2.getKey()
      newWin2.close()


  win = GraphWin("Bolinha", 800, 600)
  win.setBackground(color_rgb(0, 0, 0))

  menu = Text(Point(400, 200), "MENU")
  menu.setSize(36)
  menu.setStyle("bold")
  menu.setTextColor(color_rgb(255, 255, 0))
  menu.draw(win)

  start = Text(Point(400, 300), "START")
  start.setSize(30)
  start.setTextColor(color_rgb(255, 255, 0))
  info = Text(Point(400, 325), "press enter")
  info.setTextColor(color_rgb(255, 255, 0))
  start.draw(win)
  info.draw(win)

  credits = Text(Point(400, 400), "CREDITS")
  info2 = Text(Point(400, 425), "press space")
  info2.setTextColor(color_rgb(255, 255, 0))
  credits.setSize(30)
  credits.setTextColor(color_rgb(255, 255, 0))
  credits.draw(win)
  info2.draw(win)

  quit = Text(Point(400, 500), "QUIT")
  info3 = Text(Point(400, 525), "press esc")
  info3.setTextColor(color_rgb(255, 255, 0))
  quit.setSize(30)
  quit.setTextColor(color_rgb(255, 255, 0))
  quit.draw(win)
  info3.draw(win)
  proceed = win.getKey()

  if proceed == "Escape":
      win.close()

  if proceed == "Return":

      win.close()

      jan = GraphWin("Bolinha", 800, 600)
      jan.setBackground(color_rgb(0, 0, 0))


      nome = Entry(Point(400, 300), 10)
      nome.draw(jan)

      jan.getMouse()

      if proceed == "Return":
          jan.getKey()
          jan.close()

          new = GraphWin("Bolinha", 800, 600)
          new.setBackground(color_rgb(0, 0, 0))
          main(new, nome)
          new.close()

          new.getKey()
          new.close()

