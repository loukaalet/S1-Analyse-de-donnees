#coding:utf-8

# Exercice 5 : Modules 

import geoshape as geo


c = 2
r = 6

print("Voici les calculs réalisé grâce au module geoshape :\n")

périmètre_cercle = geo.F_carre(c)
print("\nLes résultats des cubes/carrés\n"périmètre_cercle)

aire = geo.A_carre(c)
print("\n"aire)

volume_cube = geo.V_cube(c)
print("\n"volume_cube)

périmètre_cercle = geo.P_cercle(r)
print("\nLes résultats des sphères/cercles\n"périmètre_cercle)

aire_sphère = geo.A_sphere(r)
print("\n"aire_sphère)

volume_sphère = geo.V_sphere(r)
print("\n"volume_sphère)