#coding utf-8
#/!\ il faut tester les fonctions dans le module grâce à un IF
#Périmètre d'un carré
def F_carre(c: float) -> float:
    return c + c

#Aire d'un carré
def A_carre(c: float) -> float:
    return c * c
 
#Volume d'un cube
def V_cube(c: float) -> float:
    return c * c * c

#Périmètre d'une cercle
def P_cercle(r: float) -> float:
    return (2 * r) * 3.14

#Aire d'une cercle
def A_sphere(r: float) -> float:
    return (r * r) * 3.14

#Volume d'une sphère
def V_sphere(r: float) -> float:
    return (4/3) * 3.14 * (r*r*r)


if __name__ == '__main__':
    print(f"Périmètre d'un carré {F_carre}")
    print(f"Aire d'un carré {A_carre}")
    print(f"Volume d'un cube {V_cube}")
    print(f"Périmètre d'un cerlce {P_cercel}")
    print(f"Aire d'un cercle {A_sphere}")
    print(f"Volume d'une sphere {V_sphere}")

