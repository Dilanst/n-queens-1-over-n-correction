# Coeficiente del cuadrado / Square coefficient

## Comprobación de una sola línea (apéndice H.3)

Ejecutar `python -B comprobar_una_linea.py` desde esta carpeta. El control evalúa el modelo
de `orden4.py` en siete variables formales. Compara el polinomio completo hasta grado total cuatro
con los tres monomios de H.3 y termina con error si difiere cualquier coeficiente. El factor
uniforme del resto de grado cinco se justifica mediante las estimaciones analíticas del artículo.

## Comprobación del cuadrado

Desde esta carpeta ejecute / From this directory run:

```sh
python -B cuadrado.py
```

**ES.** El programa usa aritmética racional y 18 variables formales, con truncación en grado total cuatro.
Compara el predictor del cuadrado \(01,23\) con los de las dos restricciones \(01\) y \(23\) por separado,
evaluadas sobre la misma máscara. Las cuatro primeras variables \(p_0,p_1,p_2,p_3\) son los pesos de las
casillas. La función `modelo_cuadrado` implementa la actualización del operador y su complemento de Schur.
`variables` fija los argumentos compartidos del cuadrado y de los dos pares. La salida en grados 0, 1,
2 y 3 es cero; en grado 4 es `+ 2*p0*p1*p2*p3`. El resto uniforme de quinto orden procede
de la estimación de Taylor del apéndice «De la marginal doble al cuadrado». La combinación con
el coeficiente del logaritmo de evitación, \(-1\), da \(-1-(+2)=-3\).

**EN.** The program uses rational arithmetic in 18 formal variables, truncated at total degree four.
It compares the predictor with both restrictions \(01,23\) to the two single-pair predictors on the same mask.
The first four variables \(p_0,p_1,p_2,p_3\) are the square weights. `modelo_cuadrado` implements the operator
update and its Schur complement. `variables` fixes the arguments shared by the square and the two pairs.
The output in degrees 0, 1, 2 and 3 is zero; in degree 4 it is `+ 2*p0*p1*p2*p3`. The uniform fifth-order
remainder follows from the Taylor estimate in the appendix “From the two-square marginal to the square”.
Combining this coefficient with the log avoidance coefficient, \(-1\), gives \(-1-(+2)=-3\).

Python sólo usa la biblioteca estándar. Los tres archivos del cálculo original se incluyen íntegros.
 / Python uses only its standard library. All three original calculation files are included in full.
