##  Fase 2
Esta es la fase crítica del procesamiento de la señal, donde se construye la estructura de la señal que modulará la portadora de RF.
- **Objetivo Específico 2.1:** Cargar el archivo de audio estéreo en el entorno de desarrollo (GNU Radio).
<img width="1854" height="1048" alt="Fase2_Objetivo Específico 2 1" src="https://github.com/user-attachments/assets/62b4da39-cbf2-472a-8b1b-353c1fab2a41" />

- **Objetivo Específico 2.2:** Implementar los bloques o el código necesario para generar los componentes de la señal MPX:
  - Crear la señal de suma **(L+R)** para compatibilidad monofónica.
  - Generar el tono piloto de 19 kHz, que es la referencia de fase para la demodulación estéreo.
  - Crear la señal de diferencia **(L-R)** y modularla en una subportadora de 38 kHz mediante AM de Doble Banda Lateral con Portadora Suprimida (AM-DSB-SC).
 
<img width="1854" height="1048" alt="Fase2_Objetivo Especifico 2 2y2 3" src="https://github.com/user-attachments/assets/68268a75-0edb-46f1-b01c-560490e1e803" />

- **Objetivo Específico 2.3:** Combinar (sumar) las tres señales anteriores para formar la señal MPX final.

<img width="1854" height="1048" alt="Fase2_Objetivo Especifico 2 2y2 3" src="https://github.com/user-attachments/assets/87b9b594-147f-44aa-81bc-54ce58f3fb2d" />

- **Objetivo Específico 2.4:** Analizar el espectro de la señal MPX resultante y verificar la correcta ubicación y amplitud relativa de cada uno de sus componentes.

<img width="1732" height="339" alt="Fase2_Objetivo Especifico 2 4" src="https://github.com/user-attachments/assets/3641d6eb-8f79-4afb-98ef-11530dfc4d05" />

