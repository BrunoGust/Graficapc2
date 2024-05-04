# Representación de símbolos alienígenas para números
La idea del trabajo es poder represnetar símbolos alienigenas para números donde nosotros creamos la data dibujando estos símbolos en un cuadro de canvas.
Se implementó el uso de Redes neuronales.

# Ejecución:
# 1. Cargar los datos para prepararlos
Para la obtener de los datos se desplegó un página web que nos permite dibujar los símbolos en un canva. Estos símbolos, que nos servirán para el modelo, se van guardando en archivos .npy:
- X.npy: píxeles activos por imagen dentro del canva.
- y.npy: el número que se pide dibujar en cada canva.\
Lo que significa que el i-ésimo dibujo representado en X.npy, corresponde al número de la i-esima posición de y.npy.\
Para el trabajo se cargaron en total 563 imagenes de simbolos alienigenas de los números 1, 2, 3 y 4.\
Luego que tengamos suficientes datos procedemos a descargar los archivos y.npy y X.npy.
# 2. Red neuronal
Luego de obtener los datos, pasamos al modelo en colab. 
1. Dividimos nuestros datos en dos conjuntos: uno para entrenamiento y otro para el testeo.
2. Alimentamos estos conjuntos de datos a nuestra red neuronal.
3. Luego de tenerlo entrenado probamos con un dibujo libre.

# 3. Despliegue de la predicción
Para la predicción se creó una ruta dentro de la página inicial. Esta permite dibujar el símbolo alinigena de los númeroa 1,2,3 o 4 para posterior al envío pueda predecir el número correcto.

# Complicaciones
- Por el tamaño del modelo el despliegue disminuye su eficiencia
- La predicción se tiene en el colab ya que el despliegue de la página web no se pudo lograr puesto que trabajos con el protocolo https, protocolo seguro el cual tiene restricciones para correr modelos de tensorflow en python.
