import numpy as np
import matplotlib.pyplot as plt

# Paramètres
omega = 1.0  # vitesse angulaire (rad/s)
V_uniforme = np.array([0.0, 0.0])  # champ uniforme (Vx, Vy)
rayon_disque = 3.0

# Grille de points
x = np.linspace(-4, 4, 15)
y = np.linspace(-4, 4, 15)
X, Y = np.meshgrid(x, y)

# Vecteurs rotation: v = omega × r = (-omega*y, omega*x)
U_rot = -omega * Y
V_rot = omega * X

# Masque pour le disque
distance = np.sqrt(X**2 + Y**2)
masque = distance <= rayon_disque

# Vitesse totale
U = np.where(masque, U_rot + V_uniforme[0], V_uniforme[0])
V = np.where(masque, V_rot + V_uniforme[1], V_uniforme[1])

# Affichage
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, alpha=0.8)
circle = plt.Circle((0, 0), rayon_disque, fill=False, color='red', linestyle='--')
plt.gca().add_patch(circle)
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.title('Disque en rotation + Champ uniforme')
plt.xlabel('x')
plt.ylabel('y')
plt.show()