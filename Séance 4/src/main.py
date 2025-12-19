#coding:utf8

"""
Notes :
- revoir la mise en forme (taille)
- revoir le nom des axes etc 
- vérifier que les images sont cohérente
- uniformiser la distribution sur un nombre ??
- relire le code pour le comprendre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint, binom, poisson, norm, lognorm, uniform, chi2, pareto
from scipy.special import gamma

# ============================================================
# Fonctions moyenne et écart-type
# ============================================================

def moyenne_ecart_type_dirac(valeur):
    return valeur, 0.0

def moyenne_ecart_type_uniforme_discrete(a, b):
    moyenne = (a + b) / 2
    variance = ((b - a + 1) ** 2 - 1) / 12
    return moyenne, np.sqrt(variance)

def moyenne_ecart_type_binomiale(n, p):
    return n * p, np.sqrt(n * p * (1 - p))

def moyenne_ecart_type_poisson(lambda_):
    return lambda_, np.sqrt(lambda_)

def moyenne_ecart_type_zipf_mandelbrot(s, q, N):
    k = np.arange(1, N + 1)
    pk = 1 / (k + q) ** s
    pk = pk / np.sum(pk)
    moyenne = np.sum(k * pk)
    variance = np.sum(k**2 * pk) - moyenne**2
    return moyenne, np.sqrt(variance)

def moyenne_ecart_type_poisson_continue(lambda_):
    return lambda_, np.sqrt(lambda_)

def moyenne_ecart_type_normale(mu, sigma):
    return mu, sigma

def moyenne_ecart_type_lognormale(mu, sigma):
    moyenne = np.exp(mu + sigma**2 / 2)
    ecart_type = np.sqrt((np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2))
    return moyenne, ecart_type

def moyenne_ecart_type_uniforme_continue(a, b):
    return (a + b) / 2, (b - a) / np.sqrt(12)

def moyenne_ecart_type_chi2(k):
    return k, np.sqrt(2 * k)

def moyenne_ecart_type_pareto(a, xm=1):
    if a <= 1:
        return np.nan, np.nan
    if a <= 2:
        return a * xm / (a - 1), np.nan
    moyenne = a * xm / (a - 1)
    ecart_type = np.sqrt(a * xm**2 / ((a - 1)**2 * (a - 2)))
    return moyenne, ecart_type

# ============================================================
# Fonction d'affichage μ / σ
# ============================================================

def afficher_stats(ax, moyenne, ecart_type):
    texte = f"μ = {moyenne:.2f}\nσ = {ecart_type:.2f}"
    ax.text(
        0.95, 0.95, texte,
        transform=ax.transAxes,
        ha="right", va="top",
        fontsize=9,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
    )

# ============================================================
# Figure et axes (2 lignes, 6 colonnes)
# ============================================================

fig, axes = plt.subplots(2, 6, figsize=(24, 10))
fig.suptitle("Distributions statistiques : discrètes et continues", fontsize=16, y=0.97)
axes = axes.flatten()

# ============================================================
# Ligne 1 : Variables discrètes
# ============================================================

fig.text(0.5, 0.93, "Variables discrètes", ha='center', fontsize=14)

# Dirac
val_dirac = 5
axes[0].bar([val_dirac], [1.0], color='skyblue', edgecolor='black')
axes[0].set_title("Dirac (X=5)")
m, s = moyenne_ecart_type_dirac(val_dirac)
afficher_stats(axes[0], m, s)

# Uniforme discrète
x = np.arange(1, 11)
y = randint(1, 11).pmf(x)
axes[1].bar(x, y, color='lightgreen', edgecolor='black')
axes[1].set_title("Uniforme discrète")
m, s = moyenne_ecart_type_uniforme_discrete(1, 10)
afficher_stats(axes[1], m, s)

# Binomiale
n, p = 100, 0.1
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)
axes[2].bar(x, y, color='salmon', edgecolor='black')
axes[2].set_title("Binomiale (n=100, p=0.1)")
m, s = moyenne_ecart_type_binomiale(n, p)
afficher_stats(axes[2], m, s)

# Zipf-Mandelbrot
s_z, q, N = 1.5, 2, 50
k = np.arange(1, N + 1)
pk = 1 / (k + q) ** s_z
pk = pk / np.sum(pk)
axes[3].bar(k, pk, color='lightblue', edgecolor='black')
axes[3].set_title("Zipf-Mandelbrot")
m, s = moyenne_ecart_type_zipf_mandelbrot(s_z, q, N)
afficher_stats(axes[3], m, s)

# Poisson discrète
lam = 20
x = np.arange(0, 31)
y = poisson.pmf(x, mu=lam)
axes[4].bar(x, y, color='orange', edgecolor='black')
axes[4].set_title("Poisson (λ=20)")
m, s = moyenne_ecart_type_poisson(lam)
afficher_stats(axes[4], m, s)

axes[5].axis("off")

# ============================================================
# Ligne 2 : Variables continues
# ============================================================

fig.text(0.5, 0.45, "Variables continues", ha='center', fontsize=14)

# Poisson continue
mu = 20
x = np.linspace(0, 40, 400)
y = (mu**x / gamma(x + 1)) * np.exp(-mu)
axes[6].plot(x, y)
axes[6].set_title("Poisson continue")
m, s = moyenne_ecart_type_poisson_continue(mu)
afficher_stats(axes[6], m, s)

# Normale
mu, sigma = 0, 1
x = np.linspace(-4, 4, 400)
y = norm.pdf(x, mu, sigma)
axes[7].plot(x, y)
axes[7].set_title("Normale")
m, s = moyenne_ecart_type_normale(mu, sigma)
afficher_stats(axes[7], m, s)

# Log-normale
x = np.linspace(0.001, 20, 400)
y = lognorm.pdf(x, sigma, scale=np.exp(mu))
axes[8].plot(x, y)
axes[8].set_title("Log-normale")
m, s = moyenne_ecart_type_lognormale(mu, sigma)
afficher_stats(axes[8], m, s)

# Uniforme continue
a, b = 0, 10
x = np.linspace(a, b, 400)
y = uniform.pdf(x, loc=a, scale=b - a)
axes[9].plot(x, y)
axes[9].set_title("Uniforme")
m, s = moyenne_ecart_type_uniforme_continue(a, b)
afficher_stats(axes[9], m, s)

# Chi-2
k = 4
x = np.linspace(0.001, 20, 400)
y = chi2.pdf(x, df=k)
axes[10].plot(x, y)
axes[10].set_title("Chi-2")
m, s = moyenne_ecart_type_chi2(k)
afficher_stats(axes[10], m, s)

# Pareto (CDF)
a = 3
x = np.linspace(1.001, 10, 400)
y = pareto.cdf(x, b=a)
axes[11].plot(x, y)
axes[11].set_title("Pareto")
m, s = moyenne_ecart_type_pareto(a)
afficher_stats(axes[11], m, s)

# ============================================================
# Ajustements finaux
# ============================================================

plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.93])
plt.savefig("graphiques_seance_4", dpi=300)
