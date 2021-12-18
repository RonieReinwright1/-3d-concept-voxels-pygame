import numpy
Voxels=[]
def makeVoxel(Color,cords):
    Voxels.append((Color,cords))
def RetVoxelData():
    global Voxels
    try:
        return Voxels
    except:
        None
def Dist3D(cords1,cords2):
    x,y,z=cords1
    x1,y1,z1=cords2
    Dist=(((x1-x)**2+(y1-y)**2+(z1-z)**2)**0.5)
    return Dist