########## LIBRERÍAS
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import numpy as np

from PIL import Image


xw, yw = 500, 500 # Tamaño de la ventana 
dnear, dfar = 1.0, 1000.0 # Posición de los planos de recorte próximo y lejano
angle = 45 # Ángulo de visión
aspect = xw/yw # Proporciones

# Ángulo de giro
alpha = 0


def LoadTextures():
    ### Textura
    texture = Image.open("earth.jpg")
    xtexture = texture.size[0]
    ytexture = texture.size[1]

    texturebyte = texture.tobytes("raw", "RGBX", 0, -1)
    
    surface = glGenTextures(1)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, xtexture, ytexture, 0, GL_RGBA, GL_UNSIGNED_BYTE, texturebyte)

    # Parámetros de la textura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return surface

def sphere():
    """
    Definimos la figura esfera
    """
    global Tierra
    
    # Creamos la lista Tierra que va a contener a nuestra esfera
    Tierra = glGenLists(1)
    
    # Creamos la cuádrica esfera, y le damos los parámetros adecuados
    esfera = gluNewQuadric()
    gluQuadricDrawStyle(esfera, GLU_FILL)
    gluQuadricNormals(esfera, GLU_SMOOTH)
    gluQuadricTexture(esfera, GL_TRUE)
    glNewList(Tierra, GL_COMPILE)  
    
    # Cargamos la textura DENTRO de la lista (no fuera)
    surface = LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, surface)

    # Creamos una esfera
    gluSphere(esfera, 10, 100, 100)
    
    # Eliminamos la esfera una vez creada
    gluDeleteQuadric(esfera)
    glDisable(GL_TEXTURE_2D)

    glEndList()
    
def init():
    # Color blanco de fondo
    glClearColor(0.0, 0.0, 0.0, 0.0)
    
    # Activamos el test de profundidad
    glClearDepth(1.0)  # Habilitamos el borrado del buffer de profundidad
    glDepthFunc(GL_LESS) # Indicamos el tipo de test de profundidad que queremos que realice
    glEnable(GL_DEPTH_TEST)

    # Corrección de perspectiva
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST); 
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(angle, aspect, dnear, dfar)
    
def dibujo():
    global psi, phi, theta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()# Inicio del paréntesis
    glTranslatef(0,0,-50)# Finalmente colocamos la esfera
    glRotatef(10, 1, 0, 1)# Las dos rotaciones colocan el eje en la posición ->
    glRotatef(12, 0, 0, 1)## -> que simula la de la Tierra
    glRotatef(alpha, 0, 1, 0)# realizamos la rotación sobre su eje (animación)
    glRotatef(-90, 1,0,0)# Colocamos en posición vertical la esfera

    glCallLists(Tierra)
    glPopMatrix()# Final del paréntesis

    glutSwapBuffers()

def idle():
    global alpha
    alpha = setangle(alpha + 1)
    glutPostRedisplay()
    
def setangle(alpha):
    if alpha >=360:
        return(alpha - 360)
    if alpha < 0:
        return (alpha + 360)
    return(alpha)
        
def reshape(newwidth, newheight):
    if newheight == 0:
        newheight = 1
    
    glViewport(0, 0, newwidth, newheight)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()# Reseteamos la matriz de proyección 
    gluPerspective(angle, newwidth/newheight, dnear, dfar)
    glMatrixMode(GL_MODELVIEW)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowPosition(0, 0)
glutInitWindowSize(xw, yw)
glutCreateWindow("Rotación de la Tierra sobre su eje")

init()
sphere()

glutDisplayFunc(dibujo)
glutIdleFunc(idle)
glutReshapeFunc(reshape)
glutMainLoop()
