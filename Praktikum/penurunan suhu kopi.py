# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PXAS52_doJsNK3K_sMqqWP7yiFYPkMYh
"""

import numpy as np
import matplotlib.pyplot as plt
# rentang nilai x dan waktu untuk medan vektor
x = np.arange(0, 3, 0.1)
t = np.arange(0, 4, 0.1)
T, X = np.meshgrid(t, x)

#definisi sistem
dX = -X**2+3*X-2
dT = np.ones(dX.shape)


#plot stream plot
plt.figure(figsize=(10,6))
plt.streamplot(T, X, dT, dX, color=dX, cmap='hot', linewidth=1.5)

#parameter konstanta
k = 0.1 # konstanta pendinginan
Ta = 25 # suhu lingkunan
# definisi sstem persamaan diferensial
def system(T):
  return -k*(Ta-T)
#membuat grid untuk visualisasi
t_vals = np.linspace(0, 50, 20) #rentang waktu
T_vals = np.linspace(0, 50, 20) #rentang suhu
t, T = np.meshgrid(t_vals, T_vals) # Perbakan urutan mashgrid

# menghitung vektor arah
U = np.ones_like(T) #arah horizontal tetap untuk menunjukan perubahan dalam
V = system(T) # arah vertikal mengikuti system persamaan diferensial

#plot medan vektor menggunakan streamplot
plt.figure(figsize=(7,5))
plt.streamplot(t, T, U, V, color='blue')
plt.axhline(Ta, color = 'red', linestyle ='--', label = 'solusi setimbang T=Ta')
plt.xlabel('waktu')
plt.ylabel('suhu')
plt.legend()
plt.grid()
plt.show()