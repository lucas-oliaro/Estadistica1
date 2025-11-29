from scipy import stats
import numpy as np

# Ejercicio 7
# (a) Cálculo del intervalo de confianza
media_muestral_7 = 52.3
sigma_7 = 0.05
n_7 = 20
nivel_confianza_7 = 0.99
z_99 = stats.norm.ppf(1 - (1 - nivel_confianza_7) / 2)
print(z_99)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

# Intervalo de confianza para la media
margen_error_7 = z_99 * (sigma_7 / np.sqrt(n_7))
print(margen_error_7)
ic_7 = (media_muestral_7 - margen_error_7, media_muestral_7 + margen_error_7)

# (b) Cálculo del tamaño de muestra necesario para una longitud de 0.03
L_7 = 0.03
n_muestra_7 = (2 * z_99 * sigma_7 / L_7) ** 2
n_muestra_7 = np.ceil(n_muestra_7)  # Redondeamos hacia arriba al entero más cercano
