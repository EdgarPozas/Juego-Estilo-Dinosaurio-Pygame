import pygame,sys,random
from pygame.locals import *
from numpy import *

class Player:
	def __init__(s,data):
		s.data=data
		s.playerRect=""
		s.puntos=0
		s.isSalto=False
		s.x,s.y=10,600
		s.cont=0
	def move(s,x,y):
 		s.x+=x
 		s.y-=y
 	def salto(s):
 		s.isSalto=True
	def render(s):
		s.puntos+=0.001
		s.cont+=1
		if s.cont>200:
			s.isSalto=False
			s.cont=0
		s.playerRect=pygame.Rect(s.x,s.y,30,30)
		pygame.draw.rect(s.data.ventana,(100,100,100),s.playerRect)	
		if s.isSalto:
			s.y-=1
			return
		if s.playerRect.colliderect(s.data.lv.suelo):
			s.y+=0
			s.isSalto=False
		else:
			s.y+=2
		for enemy in s.data.lv.obstaculos:
			if s.playerRect.colliderect(enemy.enemyRect):
				s.data.status="Perdiste"
				s.data.indexScene=3;
		

		if s.puntos>=10:
			s.data.status="Ganaste"
			s.data.indexScene=3
			return
