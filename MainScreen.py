import pygame
import time
import random
import CLG_Keys
import Voxels as Vx
Windows_X=255
Windows_Y=255
pygame.init()
screen = pygame.display.set_mode((Windows_X, Windows_Y))
for i in range(100):
    for a in range(100):
        for b in range(25):
            Vx.makeVoxel((i*2,a*2,b*2),(30+i,30+a,30+b))
Num=len(Vx.RetVoxelData())
Voxels=Vx.RetVoxelData()
Zoom=0
Iterat=0
while True:
    Start=time.time()
    screen.fill((0,0,0))
    Zoom+=1
    if Zoom>=60*2:
        Zoom=0
    CLG_Keys.Press_Close()
    for i in range(Num):
        Color,Cords=Voxels[i]
        R,G,B=Color
        X,Y,Z=Cords
        R2=R+int(max(0,Z-Vx.Dist3D(Cords,(30,30,Zoom))))*2
        G2=G+int(max(0,Z-Vx.Dist3D(Cords,(30,30,Zoom))))*2
        B2=B+int(max(0,Z-Vx.Dist3D(Cords,(30,30,Zoom))))*2
        Color2=(R2,G2,B2)
        Iterat+=1
        try:
            pygame.draw.circle(screen,Color2, (X,Y),int(max(0,Z-Vx.Dist3D(Cords,(30,30,Zoom)))))
        except:
            pygame.draw.circle(screen,Color, (X,Y),int(max(0,Z-Vx.Dist3D(Cords,(30,30,Zoom)))))
    End=time.time()
    print('FPS: ',1/(End-Start),'Iterations per frame:',Iterat)
    Iterat=0
    pygame.display.update()