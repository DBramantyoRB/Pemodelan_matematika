# -*- coding: utf-8 -*-
"""SIR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18zsq9-6lbvqEaQSsz7M9G7zC3j35NUnG
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
beta = 0.2
gamma= 1/10
n = 1000
SO = n-1
IO = 1
RO = 0
t = np.linspace(0, 160, 160)
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I/N
  dIdt = beta * S * I/N-gamma*I
  dRdt = gamma * I
  return[dSdt, dIdt, dRdt]
yO = [SO, IO, RO]
solution = odeint(sir_model, yO, t, args=(n, beta, gamma))
S,I,R = solution.T
plt.figure(figsize=(10, 6))
plt.plot(t, S, label = 'susceptible', color = 'blue')
plt.plot(t, I, label = 'Infectable', color = 'red')
plt.plot(t, R, label = 'Recovery', color = 'green')
plt.ylabel('Hari')
plt.title('Simulasi model SIR')
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import ipywidgets as widgets
from IPython.display import display
beta = 0.2
gamma= 1/10
n = 1000
SO = n-1
IO = 1
RO = 0
t = np.linspace(0, 160, 160)
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I/N
  dIdt = beta * S * I/N-gamma*I
  dRdt = gamma * I
  return[dSdt, dIdt, dRdt]

def update_sir(beta, gamma, SO, IO, Tmax):
  N = SO +IO
  RO = 0
  t = np.linspace(0, Tmax, Tmax)
  yO = [SO, IO, RO]
  solution = odeint(sir_model, yO, t, args=(n, beta, gamma))
  S, I, R = solution.T
  plt.figure(figsize=(10, 6))
  plt.plot(t, S, label = 'susceptible', color = 'blue')
  plt.plot(t, I, label = 'Infectable', color = 'red')
  plt.plot(t, R, label = 'Recovery', color = 'green')
  plt.xlabel('Hari')
  plt.ylabel('Jumlah')
  plt.title('Simulasi model SIR')
  plt.legend()
  plt.grid()
  plt.show()
widgets.interactive(update_sir,
                    beta=widgets.FloatSlider(min=0.01, max=1, step=0.0001, value=0.2, description = 'b'),
                    gamma=widgets.FloatSlider(min=0.01, max=1, step=0.01, value=1/10, description = 'v'),
                    SO=widgets.IntSlider(min=1, max=1000, step=1, value=997, description = 'SO'),
                    IO=widgets.IntSlider(min=1, max=100, step=1, value=3, description = 'IO'),
                    Tmax=widgets.IntSlider(min=10, max=200, step=10, value=100, description = 'Tmax'))