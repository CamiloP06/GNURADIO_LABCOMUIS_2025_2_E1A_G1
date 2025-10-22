"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

# Asegúrate de que el nombre de la clase sea 'blk'
# GRC busca este nombre por defecto.
class blk(gr.sync_block):
    """
    Calcula la potencia promedio de un vector de entrada.
    
    Entrada (in[0]): Vector de N items (complex)
    Salida (out[0]): 1 item (float)
    """

    def __init__(self, vector_size=1024):  # Parámetro para el tamaño del vector
        gr.sync_block.__init__(
            self,
            name='Estimador de Potencia',
            in_sig=[(np.complex64, vector_size)],  # Entrada: Vector de complex64
            out_sig=[np.float32]                  # Salida: Item de float32
        )
        # (Opcional) Guardar el tamaño si se necesita en work()
        self.vector_size = vector_size 

    def work(self, input_items, output_items):
        """
        input_items[0]: (NumPy array) 2D, forma (num_vectores_recibidos, vector_size)
        output_items[0]: (NumPy array) 1D, forma (num_vectores_recibidos,)
        """
        
        # Acceder a los buffers
        in_vectors = input_items[0]
        out_power = output_items[0]

        # 1. Calcular el cuadrado de la magnitud (|x|^2) para todos los vectores
        # La forma resultante es (num_vectores_recibidos, vector_size)
        mag_sq = np.abs(in_vectors)**2

        # 2. Calcular la media (promedio) a lo largo del eje del vector (axis=1)
        # Esto calcula el promedio para *cada* vector de entrada
        # La forma resultante es (num_vectores_recibidos,)
        avg_pwr = np.mean(mag_sq, axis=1) 

        # 3. Asignar los resultados al buffer de salida
        out_power[:] = avg_pwr

        # 4. Retornar el número de items de *salida* producidos
        # (Es igual al número de vectores de *entrada* consumidos)
        return len(out_power)
