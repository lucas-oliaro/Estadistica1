from scipy import stats
import numpy as np

# Ejercicio 8
# (a) Datos de la muestra de los alumnos
muestra_8 = [5, 8.1, 7.9, 3.3, 4.5, 6.2, 6.9, 7.5, 9.1]
n_8 = len(muestra_8)
media_muestral_8 = np.mean(muestra_8)
print(media_muestral_8)
desvio_muestral_8 = np.std(muestra_8, ddof=1)  # Desvío estándar muestral
print(desvio_muestral_8)
nivel_confianza_8 = 0.95
t_95 = stats.t.ppf(1 - (1 - nivel_confianza_8) / 2, n_8 - 1)
print(t_95)


# Intervalo de confianza para la media
margen_error_8 = t_95 * (desvio_muestral_8 / np.sqrt(n_8))
ic_8 = (media_muestral_8 - margen_error_8, media_muestral_8 + margen_error_8)

# (b) Prueba de hipótesis
media_anterior_8 = 7.5
t_stat_8 = (media_muestral_8 - media_anterior_8) / (desvio_muestral_8 / np.sqrt(n_8))
p_value_8 = 2 * (1 - stats.t.cdf(abs(t_stat_8), df=n_8 - 1))
