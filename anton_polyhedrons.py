def anton_poly():
    a = int(input())
    b = 0
    for i in range(a):
        c = str(input())
        if c == "Tetrahedron":
            b += 4
        if c == "Cube":
            b += 6
        if c == "Octahedron":
            b += 8
        if c == "Dodecahedron":
            b += 12
        if c == "Icosahedron":
            b += 20

    return b

print(anton_poly())
