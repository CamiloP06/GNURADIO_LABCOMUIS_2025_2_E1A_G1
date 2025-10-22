"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

# Asegúrate de que el nombre de la clase sea 'blk'
class blk(gr.sync_block):
    """
    Calcula la media y la desviación estándar de la magnitud de un vector de entrada.
    
    Entrada (in[0]): Vector de N items (complex)
    Salida (out[0]): Media de la magnitud (float)
    Salida (out[1]): Desviación estándar de la magnitud (float)
    """

    def __init__(self, vector_size=1024):  # Parámetro para el tamaño del vector
        gr.sync_block.__init__(
            self,
            name='Estadísticas de Amplitud',
            in_sig=[(np.complex64, vector_size)],  # Entrada: Vector de complex64
            out_sig=[np.float32, np.float32]     # Salida 0: float, Salida 1: float
        )
        # (Opcional) Guardar el tamaño si se necesita en work()
        self.vector_size = vector_size 

    def work(self, input_items, output_items):
        """
        input_items[0]: (NumPy array) 2D, forma (num_vectores, vector_size)
        output_items[0]: (NumPy array) 1D, forma (num_vectores,)
        output_items[1]: (NumPy array) 1D, forma (num_vectores,)
        """
        
        # Acceder a los buffers
        in_vectors = input_items[0]
        out_mean = output_items[0]
        out_std = output_items[1]

        # 1. Calcular la magnitud de todas las muestras
        # La forma de 'magnitudes' es (num_vectores, vector_size)
        magnitudes = np.abs(in_vectors)

        # 2. Calcular la media (promedio) a lo largo del eje del vector (axis=1)
        # y asignarla a la primera salida (out[0]).
        # El resultado tiene forma (num_vectores,)
        out_mean[:] = np.mean(magnitudes, axis=1)

        # 3. Calcular la desviación estándar a lo largo del eje del vector (axis=1)
        # y asignarla a la segunda salida (out[1]).
        # El resultado tiene forma (num_vectores,)
        out_std[:] = np.std(magnitudes, axis=1)

        # 4. Retornar el número de items de *salida* producidos
        # (Es igual al número de vectores de *entrada* consumidos)
        return len(out_mean)
