## Fase 1: Diseño y Configuración del Modulador (Preparación Técnica)
1. **Montaje del Entorno de Software:** Instale y configure el diagrama de bloques necesario para controlar su SDR. Asegúrese de que los controladores del SDR estén correctamente instalados y el dispositivo sea reconocido por el sistema.
2. **Creación de los Diagramas de Flujo:** Diseñe Un diagrama para generar una señal en Amplitud Modulada (AM).
3. **Preparación de las Señales Moduladoras:** Configure las fuentes de señal (bloques en el software) que se utilizarán como "mensaje" o información a modular:

    - Señal Periódica 1: Una onda sinusoidal pura (ej. 1 kHz).
    - Señal Periódica 2: Una onda cuadrada (ej. 1 kHz).
    - Señal de Audio: Un bloque de fuente de audio que capture desde un micrófono Audio Source.
4. **Definición de Parámetros:** Establezca los parámetros iniciales para la señal portadora, priorizando la seguridad del equipo:

   - Frecuencia de la Portadora: Elija una frecuencia en una banda de uso libre o experimental (ej. 433 MHz), el uso de banda libres pueden consultarlas a traves de la plataforma de la ANE CNABF.

    - Tasa de Muestreo (Sample Rate): Acorde a su SDR y al ancho de banda deseado (25e6/N). (Nota: N es una potencia de 2; puede elegir 2, 4, 8, 16, 32, 64)

    - Ganancia de Transmisión (TX Gain): Inicie con el valor más bajo posible (0 dB) para evitar daños en el puerto de entrada del osciloscopio o el analizador de espectro.
