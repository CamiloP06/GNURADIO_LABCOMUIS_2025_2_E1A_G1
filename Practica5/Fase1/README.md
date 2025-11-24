**Comprensión de la Antena Biquad:** A diferencia de la hélice en modo normal, la Biquad es una antena resonante cuyas dimensiones dependen directamente de la longitud de onda (λ). Consiste en dos "cuadrados" (quads) de alambre, donde cada lado del cuadrado mide aproximadamente λ/4. El reflector trasero sirve para dirigir toda la energía hacia adelante, aumentando la ganancia.
**Cálculos Iniciales:**
- **Seleccione la Frecuencia (f):** Elija una frecuencia de interés por debajo de 1 GHz. Puede ser la banda ISM de 915 MHz, una frecuencia de TV Digital (ej. 550 MHz) o una frecuencia de radio FM (ej. 100 MHz).
- **Calcule la Longitud de Onda (λ):** Use la fórmula λ=c/f, donde c es la velocidad de la luz (~3×10^8 m/s).
- **Calcule la Longitud del Lado (L):** La primera aproximación para cada lado de los cuadrados es L=λ/4.

**Creación y Simulación en MATLAB:**
- Abra la aplicación Antenna Designer en MATLAB y busque o cree un objeto biquad o quad. Si no existe de forma nativa, se puede modelar con segmentos de alambre (wire objects).
- Use sus dimensiones calculadas como parámetros iniciales.
- Añada un reflector (reflector) detrás del elemento principal a una distancia inicial (ej. λ/8).
- Defina el rango de simulación centrado en la frecuencia de interés (ej. para 915 MHz, simule de 800 MHz a 1100 MHz).
- Ejecute la simulación y analice el gráfico S11 (Coeficiente de Reflexión).
**Proceso de Ajuste Fino:**
- **Observación:** Es probable que la resonancia no esté exactamente en la frecuencia objetivo debido a los efectos del grosor del alambre y la cercanía del reflector.
Las herramientas de ajuste son:
- La longitud de los lados del Biquad.
- La distancia (spacing) entre el elemento y el reflector.
**Itere:** Ajuste ligeramente estas dos dimensiones y vuelva a simular hasta que el punto más bajo del S11 (resonancia) quede centrado perfectamente en la frecuencia de diseño.

Guarde los resultados: Anote las dimensiones finales optimizadas y guarde las capturas del gráfico S11 y del patrón de radiación, que debe ser claramente direccional (un lóbulo principal hacia adelante).

f = 915 MHz
λ = 0.32786
L = 0.081967
reflector = 0.040983
