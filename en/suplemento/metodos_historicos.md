# Cómo se identificaron las cancelaciones

Desarrollo de la sección 7 y protocolo de las comprobaciones finitas. Se conservan los rótulos matemáticos del registro original.

La división por $x^2$ cerca de $x=0$ hizo visible una dificultad que quedaba oculta en el interior.
Dos evaluaciones independientes de una fórmula podían concordar si ambas omitían la misma
incidencia. El desacuerdo con la pendiente esperada llevó a variar los pesos de las casillas y a
contar las líneas físicas una por una. Cuando dos casillas comparten otra línea, su vacancia entra
una sola vez. Al aplicar esta regla en los dos órdenes del producto se obtuvieron las correcciones
$\Delta_1,\Delta_2$. El catálogo del suplemento documenta el contraste ciego de implementaciones,
el evaluador por líneas y el uso de deformaciones del perfil para localizar las dos omisiones.

### Cómo conservar el signo al sumar los errores.

Una cota para $|R_Q(n)|$ permite que $nR_Q(n)$ oscile. Para retener el signo comparamos, como en
la Sección 3, las probabilidades de la misma historia detenida bajo las dos
leyes. En la llegada hay grupos cuyo tamaño crece con $n$. Condicionar a las filas implicadas
permite acotar en media la suma de esos grupos, con una constante común a todos los cortes
pequeños. Esa es la estimación que necesita la demostración. El control puntual en cada tablero
es una exigencia más fuerte.

### Del permanente de la máscara al error de un par.

Ocupar el par elimina dos filas y dos columnas. Por tanto, interesa cuánto cambia el error del
permanente al pasar al menor. Divoux y Wang dan el determinante principal en la clase difusa,
McCullagh desarrolla correcciones formales (Divoux–Wang y McCullagh) y Li trata perturbaciones de norma de
línea sublineal (Li). La estimación $(L^*)$ selecciona la primera clase de exceso del
desarrollo gaussiano y controla uniformemente el resto. Para obtener $J$ se mantiene fija la
disponibilidad de los otros dos vértices mientras se varían los pesos del par. La reinserción de
rango dos identifica la respuesta de una sola línea aun cuando las dos diagonales están
disponibles. Así la interacción del cuadrado contribuye una sola vez a $-S$.

### De un control algebraico a una consecuencia del teorema.

La cancelación del término lineal en el extremo se comprobó por ordenador en un sistema de 42
piezas transcritas [O]. La demostración para el perfil físico sigue otro argumento:
dos cortes aproximan la misma cantidad inicial y dan el criterio de Cauchy. Una pendiente
$k'(0)$ distinta de cero produciría una divergencia logarítmica. La convergencia de la integral
truncada obliga a que $k'(0)=0$ (Apéndice F).

### De la fórmula a una cifra.

Las primeras cuadraturas, basadas en unas pocas casillas centrales, daban errores de $10^{-5}$ a
$10^{-3}$ en contribuciones individuales. El método de rectángulos, adaptado de (artículo del término constante, §4),
suma todos los centros de cada patrón en una misma malla. Esta reordenación es exacta. El paso
de la malla al continuo se estima por extrapolación [N]. Refinar el perfil permitió
encerrarlo con radios inferiores a $2{,}1\cdot10^{-15}$ y obtener un intervalo para $Q_2$ en un
nodo real. La traza $S_{13}$ explica por qué el intervalo sigue siendo ancho: al acotar por
separado las entradas del bloque de filas y columnas se pierde su dependencia. La
Sección 6 cuantifica esta limitación.

## Predicciones registradas
En las comprobaciones con tableros finitos, la predicción, los casos y la regla de comparación se
fijaron antes de evaluar, en un archivo con marca de tiempo y huella SHA256. El estudio del
cuadrado, por ejemplo, registró once predicciones: ocho en casos ciegos y tres en controles
conocidos.
