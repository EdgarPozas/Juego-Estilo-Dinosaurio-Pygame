import pygame,sys,random
from pygame.locals import *
from numpy import *
from Enemy import Enemy

class Level:
	def __init__(s,data):
		s.data=data
		
		
	def initlevel(s):
		s.obstaculos=[]
		s.data.pl.puntos=0
		s.suelo=pygame.Rect(0,650,1000,30)
		for x in xrange(1,100):
			s.obstaculos.append(Enemy(s.data,x*150*random.randint(1,9)))
	def render(s):
		pygame.display.set_caption("Nivel")
		for item in s.obstaculos:
			item.render()
		pygame.draw.rect(s.data.ventana,(155,155,155),s.suelo)

		s.data.mis.createText("Puntos: "+str(s.data.pl.puntos)+" / 10",50,(200,30))