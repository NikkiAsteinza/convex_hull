from math import sqrt
import pygame
import time
import random
import collections
import time
import sys
import operator
#Iniciar pygame
pygame.init()
#Tamaño de pantalla
size = [800,800]
#Inicializar pantalla
screen = pygame.display.set_mode(size)
#Carga imagen de fondo
background_image = pygame.image.load("abstract_bg.jpg").convert()
#Mostrarla
screen.blit(background_image, [0, 0])
#Actualizar pantalla
pygame.display.flip()
#Titulo
pygame.display.set_caption("Convex Hull")
#Cargar burbujas para puntos del ConvexHull
bubble= pygame.image.load('nikkibubble.png')
#Puntos definidos por tuplas
NewPoint = collections.namedtuple("NewPoint", "x y")
#Diccionario de colores
Colors = {"green":(0,230,0),"white":(255,255,255),"red":(230, 0,0),"blue":(0,0,230), "white":(255,255,255), "black":(0,0,0)}
#Función para dibujar un punto p de un color definido en el diccionario
def drawPoint(p, color, width=2):
    pygame.draw.rect(screen, Colors[color], pygame.Rect(p.x,p.y,5,5),width)
    #Refrescar pantalla
    pygame.display.flip()
#Función para dibujar una linea de origin a target de un color definido en el diccionario
def drawLine(origin, target, color, width=2):
    pygame.draw.line(screen, Colors[color],origin,target,width)
    #Refrescar pantalla
    pygame.display.flip()
#Función para crear un polígono un polígono de n puntos aleatorios
def randomPolygon(n):
    #lista de puntos
    PointList =[]
    #Limitando valores pseudoaleatorios
    Top=NewPoint(random.randint(80,750),80)
    PointList.append(Top)
    drawPoint(Top,"white",4)
    Bottom=NewPoint(random.randint(80,750),750)
    PointList.append(Bottom)
    drawPoint(Bottom,"white",4)
    Left=NewPoint(80,random.randint(80,750))
    PointList.append(Left)
    drawPoint(Left,"white",4)
    Right=NewPoint(750,random.randint(80,750))
    PointList.append(Right)
    drawPoint(Right,"white",4)
    i=4
    #bucle creación de puntos
    while i<n:
        #Nuevo punto aleatorios
        p = NewPoint(random.randint(0,600),random.randint(0,600))
        #Añadir punto a lista de puntos
        PointList.append(p)
        drawPoint(PointList[i],"green",4)
        #Dibujar punto
        #Aumentar iterador
        i=i+1
    return PointList
#Función para ordenar polígno p segun criterio i
def sortPolygon(p,i):
    return sorted(p, key=lambda x: x[i])
#Función para añadir puntos contenidos en una lista l al polígono p
def addPoints2Polygon(l,p):
    #iterador
    e=0
    #bucle para añadir puntos de la lista al poligono
    while e< len(l):
        #punto a añadir
        point2Add= l[e]
        #añadir punto l[e] a p
        p.append(point2Add)
        e=e+1
def distance2Line(p1, p2,P):
    a=p1.y-p2.y
    b=p2.x-p1.x
    c=p1.x+p2.y-p2.x*p1.y
    return abs(a*P.x+b*P.y+c/sqrt(a*a+b*b))
#Función para calcular si un punto p está dentro de un polígono P
def divide(p1,p2,P):
    above=[]
    below=[]
    #linea vertical
    if p2.x - p1.x == 0:
        return above, below
    #traduccion de y=mx+o
    m=(p2.y-p1.y)/(p2.x-p1.x)
    c=-m*p1.x+p1.y

    #iterar por los puntos:
    for point in P:
        #y>mx is above the linea
        if point.y>m*(point.x)+c:
            above.append(point)
        #si no esta detrás:
        elif point.y<m*(point.x)+c:
            below.append(point)
    return above, below

def convexHull(Polygon):
    if len(Polygon)<=2:
         return Polygon

    Convex_Hull=[]
    sort=sorted(Polygon, key=lambda x:x[0])
    p1=sort[0]
    p2=sort[-1]
    drawLine(p1,p2,"white")
    drawPoint(p1,"red",3)
    drawPoint(p2,"red",3)
    #Lo añadimos al ConvexHull
    Convex_Hull = Convex_Hull + [p1,p2]
    print("First Hull = Horizontal limits added to the list:"+str(Convex_Hull))
    #borramos de la lista los Puntos
    sort.pop(0)
    sort.pop(-1)
    print("Point list before removing hull points:"+str(sort))
    above, below=divide(p1,p2,sort)
    print("Above points list:"+str(above))
    print("Below points list:"+str(below))
    Convex_Hull= Convex_Hull+quickHull2(p1,p2,above,"above")
    Convex_Hull= Convex_Hull+quickHull2(p1,p2,below,"below")

    return Convex_Hull

#Función  para calcular el ConvexHull
def quickHull2(p1,p2,division,flag):
    #Caso base para salir de la recursión
    if division ==[] or p1 is None or p2 is None:
        return[]
    #Set de puntos
    convex_hull=[]
    #Distancia de cada punto al segmento:
    farthest_distance=-1
    farthest_point=None
    for point in division:
        distance = distance2Line(p1,p2,point)
        if distance > farthest_distance:
            farthest_distance=distance
            farthest_point=point
    #Añadir el punto mas lejano al Hull
    convex_hull=convex_hull+[farthest_point]
    #Borrar el punto añadido
    division.remove(farthest_point)
    #Dividir el conjunto de puntos resultantes
    point1above,point1below =divide(p1,farthest_point,division)
    point2above,point2below =divide(p2,farthest_point,division)

    if flag == "above":
        convex_hull=convex_hull+quickHull2(p1,farthest_point,point1above,"above")
        convex_hull=convex_hull+quickHull2(farthest_point,p2,point2above,"above")
    else:
        convex_hull=convex_hull+quickHull2(p1,farthest_point,point1below,"below")
        convex_hull=convex_hull+quickHull2(farthest_point,p2,point2below,"below")
    return convex_hull

def printHull(H):
    print("Final Hull:",H)
    for point in H:
        screen.blit(bubble,(point.x,point.y))
        drawPoint(point,"red",4)
        pygame.display.flip()
        #drawPoint(point,"red",4)


Polygon=[]
RandomPoints = randomPolygon(15)
addPoints2Polygon(RandomPoints,Polygon);
print("Polygon"+str(Polygon))
Result=convexHull(Polygon)
printHull(Result)


#convexHullA(Polygon,2)

time.sleep(25.5)
pygame.quit()
