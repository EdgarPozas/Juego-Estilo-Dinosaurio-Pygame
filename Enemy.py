import pygame,sys,random
from pygame.locals import *
from numpy import *

class Enemy:
	def __init__(s,data,x):
		s.data=data
		s.x,s.y=x,620
		s.enemyRect=pygame.Rect(s.x,s.y,20,30)
		s.vidas=3
		s.color=(100,0,0)
	def render(s):
		s.enemyRect=pygame.Rect(s.x,s.y,20,30)
		pygame.draw.rect(s.data.ventana,s.color,s.enemyRect)
		s.x-=0.5
	