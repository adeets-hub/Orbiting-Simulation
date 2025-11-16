import pygame
import math
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,480))
pygame.display.set_caption("ORBITING SIMULATION")
run=True

##DEFINING VARIABLES AND IMAGES
x_earth=350
y_earth=200
x_moon=388
y_moon=200
angle=180
angle_2=180
clock=pygame.time.Clock()

image=pygame.image.load("Sun3.bmp")
image=pygame.transform.scale(image,(60,60))
image2=pygame.image.load("Earth.bmp")
image2=pygame.transform.scale(image2,(50,50))
box1=pygame.image.load("box1.bmp")
box1=pygame.transform.scale(box1,(35,35))
box2=pygame.transform.rotate(box1,180)
box4=pygame.transform.rotate(box1,180)
CtrlPanel=pygame.image.load("CtrlPanel.bmp")
CtrlPanel=pygame.transform.scale(CtrlPanel,(112,112))
Kepler_second_law=pygame.image.load("KEPLER-SECOND-LAW-BUTTON_2.bmp")
Kepler_second_law=pygame.transform.scale(Kepler_second_law,(112,112))
Moon_button=pygame.image.load("Moon_button.bmp")
Moon_button=pygame.transform.scale(Moon_button,(75,75))
Pause_button=pygame.image.load("PAUSE-BUTTON_2.bmp")
Pause_button=pygame.transform.scale(Pause_button,(40,40))
Play_button=pygame.image.load("PLAY-BUTTON.bmp")
Moon=pygame.image.load("Moon.bmp")
Moon=pygame.transform.scale(Moon,(14,14))
Play_button=pygame.transform.scale(Play_button,(40,40))

x=588
y=175
x_2=555
y_2=418
sun_x=218
sun_y=220
timer=0

r=random.randint(0,200)
g=random.randint(0,200)
b=random.randint(0,200)
color=(255,255,255)
Lpoints=[(253,253),(254,253),(255,254)]
L=[]
index_secondlaw=-1
Lcolor=[]
month_L=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
month_label_L=[]
second_law=False
x_major_radius=150
y_minor_axis=125
moon_major_radius=40
moon_minor_axis=40
earth_move=False
moon_show=False
label_show_add=0
label_show=False

##FUNCTION TO SHOW TEXT

def show_text(msg,x,y,color):
    font_obj=pygame.font.SysFont("comicsans",18)
    msg_obj=font_obj.render(msg,False,color)
    return msg_obj
while run==True:
    clock.tick(30)
##CHANGING ANGLE SO THAT EARTH KEEPS MOVING, MADE SURE IT WENT COUNTERCLOCKWISE
    if earth_move==True:
        angle=angle-1
        angle_2=angle_2-13.38
        if angle==1:
            angle=360
        if angle_2<=12.12:
            angle_2=360
    
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
        if event.type==MOUSEBUTTONDOWN:
            if 655<=event.pos[0]<=690 and 375<=event.pos[1]<=410:
                Lcolor=[]
                L=[]
                Lpoints=[(253,253),(254,253),(255,254)]
                y_minor_axis=y_minor_axis-10
            elif 655<=event.pos[0]<=690 and 335<=event.pos[1]<=370:
                Lcolor=[]
                L=[]
                Lpoints=[(253,253),(254,253),(255,254)]
                y_minor_axis=y_minor_axis+10
            elif 610<=event.pos[0]<=645 and 335<=event.pos[1]<=370:
                Lcolor=[]
                L=[]
                Lpoints=[(253,253),(254,253),(255,254)]
                x_major_radius=x_major_radius+10
            elif 610<=event.pos[0]<=645 and 375<=event.pos[1]<=410:
                Lcolor=[]
                L=[]
                Lpoints=[(253,253),(254,253),(255,254)]
                x_major_radius=x_major_radius-10
            elif 610<=event.pos[0]<=645 and 150<=event.pos[1]<=190:
                earth_move=False
                Lcolor=[]
                L=[]
                second_law=False
                Lpoints=[(252.5,252.5),(253,252.5),(253.5,252.5)]
            elif 650<=event.pos[0]<=690 and 150<=event.pos[1]<=190:
                earth_move=True
                Lcolor=[]
                L=[]
                Lpoints=[(252.5,252.5),(253,252.5),(253.5,252.5)]
            elif 595<event.pos[0]<1107 and 240<event.pos[1]<285:
                if second_law==True:
                    second_law=False
                    L=[]
                    Lpoints=[]
                    month_label_L=[]
                    index_secondlaw=-1
                else:
                    second_law=True
                    month_label_L=[]
                    index_secondlaw=-1
            if 500<event.pos[0]<575 and 340<event.pos[1]<415:
                if moon_show==True:
                    moon_show=False
                else:
                    moon_show=True
                    
##FIGURING OUT DISTANCE FROM THE EARTH TO THE SUN
    distance_x=sun_x-x_earth
    distance_y=250-y_earth
    d=math.sqrt(distance_x**2+distance_y**2)
    
##DISTANCE AND ORBITAL SPEED RELATIONSHIP EQUATION
    V=math.sqrt(10000/d)
    t=(angle*math.pi)/180
    t_2=(angle_2*math.pi)/180
    
##MATH FOR ELLIPSE
    x_earth=math.cos(t)*x_major_radius+V+250
    y_earth=math.sin(t)*y_minor_axis+V+250
    x_moon=math.cos(t_2)*moon_major_radius+V+x_earth
    y_moon=math.sin(t_2)*moon_minor_axis+V+y_earth
    screen.fill((0,0,0))
    
##SHOWING THE VELOCITY AS TEXT
    msg="Velocity= "+str(round(V,2))
    msg2="Ellipse Radius Lengths"
    msg3="X-axis"
    msg4="Y-axis"
    
##SUN FOCI CALCULATIONS
    sun_x=((2*(x_major_radius-30)*147)/299)+(250-x_major_radius)
    
##SHOWING KEPLER'S SECOND LAW
    timer=timer+1
    if second_law==True:
        Lpoints.append((x_earth,y_earth))
        if timer%30==0:
            index_secondlaw=index_secondlaw+1
            if index_secondlaw==12:
                index_secondlaw=0
            if len(L)==12:
                L=[]
            L.append(Lpoints)
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            ran_color=(r,g,b)
            Lcolor.append(ran_color)
            Lpoints=[(253,253),(254,253),(255,254)]
        for i in range(0,len(L),1):
            pygame.draw.polygon(screen,Lcolor[i],L[i])
            if len(month_label_L)>=2:
                month_label_L.pop(0)   
            month_label_L.append([month_L[index_secondlaw],(x_earth,y_earth)])
        for month_display in range(0,len(month_label_L),1):
            pygame.draw.rect(screen,(0,0,0),(month_label_L[0][1][0]+15,month_label_L[0][1][1]+15,35,25))
            screen.blit(show_text(month_label_L[0][0],x,y,color),(month_label_L[0][1][0]+19,month_label_L[0][1][1]+19))

##DRAWING AND BLITTING IMAGES
    rect=pygame.draw.rect(screen,(0,0,0),(250-x_major_radius,250-y_minor_axis,2*x_major_radius,2*y_minor_axis),2)
    screen.blit(image,(sun_x,sun_y))
    pygame.draw.ellipse(screen,(255,255,255),rect,2)
    screen.blit(image2,(x_earth-25,y_earth-25))
    screen.blit(box1,(610,375))
    screen.blit(box2,(655,335))
    screen.blit(box1,(655,375))
    screen.blit(box4,(610,335))
    screen.blit(CtrlPanel,(600,25))
    screen.blit(Kepler_second_law,(595,210))
    screen.blit(Pause_button,(610,150))
    screen.blit(Play_button,(650,150))
    screen.blit(Moon_button,(500,340))
    if moon_show==True:
        screen.blit(Moon,(x_moon-7,y_moon-7))
    pygame.display.update()
pygame.quit()



