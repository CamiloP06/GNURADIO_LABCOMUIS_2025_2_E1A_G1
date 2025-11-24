## Resultados, analisis y discusion

**Tabla de Diseño:** Presente los parámetros finales de la antena simulada (Lado del Quad, Distancia al Reflector, Frecuencia).

| Parametro  | Valor | Descripción | 
|------------|-------|-------------|
| Frecuencia central (f)  | ≈ 915 MHz  | Frecuencia objetivo de diseño.  |
| Longitud de Onda (λ)    | ≈ 32.78 cm  | Calculado como λ=c/f.  |
| Longitud del Lado (L)   | ≈ 82 mm  | Dimensión inicial del quad (L=λ/4). |
| Distancia al Reflector  | ≈ 41 mm  | Espaciamiento inicial (λ/8).  |

**Analisis de datos**

La comparación entre la simulación y la medición revela un desplazamiento en la frecuencia de resonancia, pues mientras el diseño en MATLAB se centró en 915 MHz , la medición con el VNA ubicó el punto de mejor acople en 901.2 MHz. Esta diferencia de aproximadamente 14 MHz hacia abajo indica que la antena construida resultó eléctricamente más grande que el modelo teórico. Esto se atribuye principalmente a las tolerancias humanas durante el doblado del alambre, que probablemente excedieron las longitudes calculadas, y a los efectos parásitos capacitivos introducidos por la soldadura y el conector SMA que no fueron contemplados en la simulación ideal.

Análisis Funcional Las pruebas con el analizador de espectro validaron exitosamente la directividad de la antena y su patrón de radiación simulado, el cual proyectaba un lóbulo principal frontal. Al corregir la orientación de la antena hacia la fuente de señal, la potencia recibida aumentó drásticamente de -42.30 dBm a -27.54 dBm. Este incremento de casi 15 dB confirma que el reflector está concentrando la energía eficazmente hacia adelante y rechazando las señales que provienen de otras direcciones.

Análisis del Proceso de Diseño El proceso de diseño asistido por MATLAB fue fundamental para sintonizar la antena antes de la etapa constructiva, permitiendo modificar iterativamente variables críticas como la longitud del lado del cuadrado y la distancia de separación con el reflector. Esta optimización previa aseguró que la resonancia teórica estuviera perfectamente centrada en la frecuencia de diseño, logrando que el prototipo final fuera funcional y eficiente a pesar de los pequeños márgenes de error introducidos durante la manufactura manual
