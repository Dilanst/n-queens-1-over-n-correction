# Índice de trazabilidad / Traceability index

Para reconstruir el argumento de la constante hay que seguir dos contribuciones hasta la misma cantidad del tablero inicial. La media interior se calcula con el corte fijo. La contribución del par de frontera se identifica en las dos orientaciones y sus cuatro estados. La comparación de dos cortes permite después bajar el corte y determinar la pendiente física en el extremo.

Two contributions must be traced back to the same initial-board quantity. The interior mean is evaluated at a fixed cutoff. The boundary-pair contribution is identified for both orientations and all four states. Comparing two cutoffs then gives the limit and determines the endpoint slope for the physical profile.

## Del artículo a la fuente / From paper to source

| Paso / Step | Ubicación en el artículo / Location in the paper | Operación que se verifica / Claim to check | Fuente documental / Source extract |
|---|---|---|---|
| Media interior / Interior mean | [ES](../articulo/partes/prueba_interior.tex) · [EN](../../en/paper/partes/prueba_interior.tex) | Con \(b>0\) fijo, la corrección del predictor convierte la media en \(I(b)\). / With \(b>0\) fixed, the predictor correction turns the mean into \(I(b)\). | [Cotejo, 04, líneas 45–54](FUENTES_EMPALMES.md#interior) |
| Par de frontera / Boundary pair | [ES](../articulo/partes/prueba_frontera.tex) · [EN](../../en/paper/partes/prueba_frontera.tex) | (F2) identifica el término del par al tomar primero el límite en \(n\) y después en \(b\). La interacción del cuadrado entra una vez. / (F2) identifies the pair term by taking the limit in \(n\) first, then in \(b\). The square interaction is counted once. | [F2, 06, líneas 20–53](FUENTES_EMPALMES.md#f2) |
| Límite y extremo físico / Limit and physical endpoint | [ES](../articulo/partes/prueba_cierre.tex) · [EN](../../en/paper/partes/prueba_cierre.tex) | Dos cortes del mismo tablero dan el criterio de Cauchy. La finitud de \(I(b)\) obliga luego a anular el coeficiente logarítmico. / Two cutoffs of the same board give the Cauchy criterion. Finiteness of \(I(b)\) then forces the logarithmic coefficient to vanish. | [Cierre, 07, líneas 3–12 y 51–89](FUENTES_EMPALMES.md#cierre) |

El cotejo histórico se usa aquí únicamente para la identidad a corte positivo. La comparación de dos cortes proporciona el cierre vigente para el perfil físico. / The historical comparison is used here only for the identity at a positive cutoff. The two-cutoff argument supplies the final closure for the physical profile.

## Mapas y comprobaciones / Source maps and checks

| Tema / Topic | Localizador / Where to look |
|---|---|
| Dependencias del argumento con signo, incluido el control de llegada / Dependencies of the signed argument, including the arrival estimate | [Argumento con signo / Signed argument](traza_prueba.md) |
| Torres, influencias y patrones locales / Rooks, influences and local patterns | [Fuentes de las torres / Rook sources](traza_torres.md) |
| Evolución de los métodos, con las vías exploratorias / Development of the methods, including exploratory approaches | [Catálogo de técnicas / Methods catalogue](CATALOGO.md) |
| Procedencia de las afirmaciones numéricas / Sources for numerical claims | [Trazabilidad del cálculo / Numerical source map](traza_numeros.md) |
| Alcance de los resultados y de las verificaciones / Scope of results and checks | [Estado / Status](ESTADO.md) |
| Reproducción y procedencia de archivos numéricos / Numerical reproduction and file provenance | [Instrucciones / Instructions](REPRODUCIR.md) · [Registro de procedencia / Provenance table](ORIGEN_NUMERICO.tsv) |
