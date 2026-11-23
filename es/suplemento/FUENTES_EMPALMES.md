# Fuentes de tres empalmes de la prueba / Sources for three steps of the proof

Los bloques conservan el texto TeX español original. Cada ruta identifica el expediente y el archivo dentro del archivo de trabajo. La huella de origen corresponde al archivo íntegro. Cada huella de extracto incluye sus terminadores de línea originales. Los intervalos de líneas son inclusivos. [Índice de trazabilidad](TRAZABILIDAD.md)

Each block preserves the original Spanish TeX source. Paths identify each file within its source package. The source digest covers the full file. Each extract digest includes the original line endings. Line numbers are inclusive. [Traceability index](TRAZABILIDAD.md)

<a id="interior"></a>

## Media interior a corte fijo / Interior mean at a fixed cutoff

La igualdad de las dos integrales es el dato que se transporta al cierre. El archivo histórico continúa con un argumento condicional que usa el orden del extremo. Para la existencia del límite físico se emplea el tercer pasaje de este dossier.

The equality of the two integrals at fixed cutoff is the input to the final proof. The historical file continues with a conditional argument that uses the endpoint order. The proof of existence for the physical profile is given in the third selection below.

Origen / Source · `p10_cotejo_de_las_dos_medias_20261123T114324Z/04_condicion_y_ensamblaje.tex`  
SHA-256 · `779720eb006a2c313aa891417b7a96f48b54804b8d6db5cec3f832a021f9f1a2`

Líneas / Lines 45–54 · SHA-256 · `4a9af900243d0d7421ff85c31ee11a18c7ad4b1f64b1903ef498a287666f8846`

```tex
Use la parte 12 de la entrega de llegada, con su orden de límites. La parte 03 de esta entrega
identifica el término interior del predictor ordinario. El paso al predictor corregido suma
\((F(b)-1/12)/b-(F(1)-1/12)\) según llegada/11:47--61.
Al escribir \(G={\cal V}+F-1/12\), la suma de ambas expresiones es
\[
 \lim_{n\to\infty}n{\mathbb E}_\mu A^\sharp
  =\int_b^1\frac{d(x)}{x^2}\,dx+\frac{G(b)}b-G(1)
  =\int_b^1\frac{k(x)}{x^2}\,dx,\qquad k=d+G-xG'.
\]
La constante \(F(1)-1/12\) se agrega una vez al recuperar \(R_Q\).
```

<a id="f2"></a>

## Frontera en ocho clases / Boundary term in eight classes

La primera igualdad fija el corte, la orientación y el estado. El segundo paso baja el corte y produce (F2). Las líneas finales asignan la interacción del cuadrado completo una sola vez. El alcance de este extracto termina en esa identificación de frontera.

The first equality holds at fixed cutoff, orientation and state. Taking the cutoff to zero then gives (F2). The last lines count the full-square interaction once. The extract establishes this boundary identification.

Origen / Source · `p10_F2_camino_del_par_20261123T115914Z/06_F2_y_limite.tex`  
SHA-256 · `21a118d1d0d80ef6131fc4ec5fae877edb02c4c8851669e2e54b446a3722462b`

Líneas / Lines 20–53 · SHA-256 · `e1194fbdd9760349433964b9f562a90bbb49d55fd9835fa2f7bfb99b669d8b17`

```tex
En detalle, para cada \(b>0\) admisible fijo, cada orientación y cada estado,
\[
 \lim_{n\to\infty}n{\mathbb E}_{\mu}
 \left[{\bf1}_{F_b}\sum_{(e,f)\in(o,s_0)} p_ep_f B_{\rm fis}(e,f)\right]
 = \int_\Omega w_{o,b}\,q_{o,s_0,b}\,{\cal B}_{o,s_0}(b)\,dr\,dc\,dh_0 .
\]
El orden del par es el de la fila. A longitud de truncación fija esta igualdad,
con los truncados correspondientes, es la de las submedidas; se retiran las
truncaciones por los errores uniformes de la parte 05. En la normalización hay
\(n^3\) ubicaciones geométricas, cuatro factores de tamaño \(1/j\) y la probabilidad
de las cuatro etiquetas vivas \(b^4\). Esto deja
\(w_{o,b}=B_oW_b^0(e)W_b^0(f)=p_b(e)p_b(f)/U_o(b)\).
La excepción en \(F_b\) se descarta a \(b\) fijo por la parte 04 y la difusión.

Sólo ahora se baja \(b\). Las vacancias \(v_b=U_D(b)U_A(b)\) están uniformemente
minoradas, y \(p_b,W_b^0\) son acotados y continuos en \(b\) hasta cero, por llegada/08
y el cotejo 02b:103--113. La minoración da una brecha uniforme del núcleo basal
continuo: por ejemplo \(p_b^*p_b\) tiene núcleo minorado por una constante positiva.
En el espacio de patrones, el operador basal en el bulto anula las fluctuaciones
de media cero a posición fija; en funciones de posición tiene el mismo núcleo \(p_b\).
Los extremos raíz se recuperan por sustitución. Las colas de los recorridos centrados
y de las trazas de la parte 05 son por tanto uniformes para el perfil cerca de cero.
Cada truncado es continuo en el parámetro por convergencia dominada; conserva los
factores de patrón incluso cuando uno de ellos tiende a cero. Se obtiene la continuidad
de las integrales. En cero, las acciones, el cofactor y su corrección de longitud dos
son exactamente los del \(B_2\) continuo que define \(J\) en el punto 9. Se concluye
\[
 \lim_{b\downarrow0}\limsup_{n\to\infty}
 \left|{\cal A}_{n,b}(j^2B_{\rm fis})-{\cal I}_0(B_2)\right|=0 .
 \tag{F2}
\]
Se han usado las dos orientaciones y sus cuatro estados. En el estado con ambos
bits iguales a uno el segundo par conserva el tratamiento de una sola línea, y
la interacción del cuadrado completo queda contabilizada una vez en \(-S\).
```

<a id="cierre"></a>

## Comparación de dos cortes / Two-cutoff comparison

El primer bloque define el tablero inicial, la aproximación truncada y la constante de frontera. El segundo establece el criterio de Cauchy y deduce la anulación de la pendiente para el perfil físico a partir de la finitud de la integral truncada. Las tres estimaciones de entrada están identificadas por separado en el mapa del argumento con signo.

The first block defines the initial-board quantity, its cutoff approximation and the boundary constant. The second establishes the Cauchy criterion. Finiteness of the truncated integral then forces the slope to vanish for the physical profile. The signed-argument source map identifies the three input estimates.

Origen / Source · `p10_cierre_por_dos_cortes_20261123T123435Z/07_cierre.tex`  
SHA-256 · `ef04115e0bb5bc7c7fb5c42c329b61a6bee6b7b266013c049e469d349588584d`

Líneas / Lines 3–12 · SHA-256 · `a486750968adc28488c7f3e88b81d44a3312db3c740724d84219f22aa4bc8400`

```tex
\paragraph{Lema.}
En el perfil físico, ponga \(a_n=nR_Q(n)\), \(A=F(1)-1/12\) y \(H=P_T+J-S\),
donde \(J=-B2+L2\). Sea \(G=\mathcal V+F-1/12\) y \(k=d+G-xG'\).
Con los márgenes y \(\delta\) fijados como en la estimación de llegada, sea \(b>0\)
un corte admisible y \(j=\lfloor bn\rfloor\). Existen cortes admisibles arbitrariamente pequeños.
Defina, por ahora sólo para estos cortes,
\[
 I(b)=\int_b^1\frac{k(x)}{x^2}\,dx,\qquad \Phi(b)=A+I(b)+H.
\]
Entonces \(\Phi(b)\) tiene límite finito \(\Phi_0\) al bajar el corte y \(a_n\to\Phi_0\).
```

Líneas / Lines 51–89 · SHA-256 · `bb47a3811d797a52a7c3662741269d0325e6c5aa94b8c534882fbab050457cc2`

```tex
\paragraph{Demostración del lema.}
Los límites superiores se toman primero con \(b\) fijo. Las tres entradas dan
\[
 \limsup_{n\to\infty}|a_n-\Phi(b)|\le C_\delta b+\eta(b)=:\varepsilon(b).
\]
Para dos cortes fijos \(b,b'\), el número \(a_n\) corresponde al mismo tablero inicial.
Para cada \(n\) suficientemente grande para ambos cortes se cumple
\[
 |\Phi(b)-\Phi(b')|\le|\Phi(b)-a_n|+|a_n-\Phi(b')|.
\]
Al tomar el límite superior en \(n\), el lado derecho queda acotado en límite superior
por \(\varepsilon(b)+\varepsilon(b')\). Esta cota tiende a cero cuando ambos cortes bajan.
Por el criterio de Cauchy y la completitud de \(\mathbb R\), existe \(\Phi_0\in\mathbb R\).
Para cada corte admisible suficientemente pequeño,
\[
 \limsup_{n\to\infty}|a_n-\Phi_0|\le\varepsilon(b)+|\Phi(b)-\Phi_0|.
\]
El lado izquierdo es independiente de \(b\). Hacer \(b\downarrow0\) prueba \(a_n\to\Phi_0\).

\paragraph{Identificación del límite y corolario para el perfil físico.}
Por el lema, \(I(b)=\Phi(b)-A-H\) tiene límite finito a lo largo de los cortes admisibles.
Por el orden cero revisado, \(k(0)=0\). Por la parte (a) del teorema de regularidad de
\(k\) (Extremo, paso al límite/04, líneas 91--96 y 108--111), \(k\) y \(G\) son analíticas
cerca de cero. Fijando \(x_0>0\) en ese entorno, se tiene
\(k(x)=k'(0)x+x^2h(x)\) con \(h\) analítica y acotada en \([0,x_0]\).
Por tanto, para \(0<b<x_0\),
\[
 I(b)=I(x_0)+k'(0)\log(x_0/b)+\int_b^{x_0}h(x)\,dx ,
\]
donde \(I(x_0)\) denota la integral ordinaria desde \(x_0\) hasta uno.
El último sumando permanece acotado. La convergencia por los cortes admisibles fuerza
\(k'(0)=0\). De \(k'=d'-xG''\) se deduce también \(d'(0)=0\) para el perfil físico.
Así \(k(x)/x^2\) tiene singularidad evitable y la integral converge absolutamente
para el límite inferior ordinario. Con \(P_0=P_T+J\) se obtiene
\[
 \lim_{n\to\infty}n\bigl(\log Q(n)-\log Q_{\rm pred}(n)\bigr)
 =\Phi_0=\mathcal C_0+P_0-S,\qquad
 \mathcal C_0=F(1)-\tfrac1{12}+\int_0^1\frac{k(x)}{x^2}\,dx .
\]
```
