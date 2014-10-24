# Generates a palette of random GLSL vec3 colors

import random

paletteSize = 50

if __name__ == "__main__":

    f = open('palette', 'w')

    f.write('const vec3 palette[' + str(paletteSize) + '] = vec3[' + str(paletteSize) + '](\n')

    for x in range(0, paletteSize):
        r = random.uniform(0.0, 1.0)
        g = random.uniform(0.0, 1.0)
        b = random.uniform(0.0, 1.0)
        if (x < paletteSize-1):
            f.write('vec3(' + str(r) + ', ' + str(g) + ', ' + str(b) + '),\n')
        else:
            f.write('vec3(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')\n);')

    f.close()        
