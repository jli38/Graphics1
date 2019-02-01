f = open('image.ppm', 'w')
f.write('P3\n 500 \n 500 \n 255\n')

for value in range(500):
    for val in range(500):
        r = (value * 2) % 256
        g = (value / 2) % 256
        b = val % 256
        f.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' \n')
f.close()
