El éxito de esta misión depende de su habilidad para solicitar (mediante "prompts") a la IA exactamente lo que necesita.
1. **Definición del Bloque 1:** Estimador de Potencia:
- **Función:** Este bloque debe recibir una ventana (vector) de muestras complejas y calcular su potencia promedio.
- **Cálculo:** La potencia promedio de un vector x[n] 
- **Acción:** Formule un prompt para la IA. Pídale que genere el código para un bloque Embedded Python Block de GNU Radio.
- **Ejemplo de Prompt (Formal):** "Necesito el código para un bloque 'Embedded Python Block' de GNU Radio. El bloque debe tener una entrada (vector, tipo complex) y una salida (un solo ítem, tipo float). La función work debe calcular la potencia promedio de la ventana de entrada. La potencia se define como la media del cuadrado de la magnitud de las muestras. Asegúrese de importar la biblioteca numpy."

El prompt utilizado fue el siguiente:
Necesito el código para un bloque 'Embedded Python Block' de GNU Radio. El bloque debe tener una entrada (vector, tipo complex) y una salida (un  solo ítem, tipo float). La función work debe calcular la potencia promedio de la ventana de entrada. La potencia se define como la media del cuadrado de la magnitud de las muestras. Asegúrese de importar la biblioteca numpy.

2. **Definición del Bloque 2:** Estadísticas de Amplitud:
- **Función:** Este bloque debe recibir una ventana de muestras complejas y calcular dos valores: la media de la magnitud y la desviación estándar de la magnitud.
- **Cálculo:** Debe calcular la magnitud de x[n] para cada muestra, y sobre ese vector de magnitudes, calcular la media y la desviación estándar.
- **Acción:** Formule un prompt para la IA. Este bloque es más complejo.
- **Ejemplo de Prompt (Formal):** "Genere el código para un 'Embedded Python Block' de GNU Radio con una entrada (vector, tipo complex) y dos salidas (un solo ítem por salida, ambas tipo float). La salida out[0] debe ser la media de la magnitud de las muestras de entrada (calculada como numpy.mean(numpy.abs(in_sig[0]))). La salida out[1] debe ser la desviación estándar de la magnitud de esas mismas muestras."

El prompt utilizado fue el siguiente:
Necesito el código para un 'Embedded Python Block' de GNU Radio con una entrada (vector, tipo complex) y dos salidas (un solo ítem por salida, ambas tipo float). La salida out[0] debe ser la media de la magnitud de las muestras de entrada (calculada como numpy.mean(numpy.abs(in_sig[0]))). La salida out[1] debe ser la desviación estándar de la magnitud de esas mismas muestras.

**Revisión del Código:** Analice el código generado por la IA. Verifique que importe numpy y que la lógica en la función work sea correcta. Preste atención a cómo maneja las variables de entrada (in_sig[0]) y salida (out[0], out[1]).

Dentro de esta carpeta se encuentra los codigos obtenidos gracias a la inteligencia artificial gemini.
