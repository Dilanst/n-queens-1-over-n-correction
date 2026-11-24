# El cambio del predictor al imponer una línea con dos casillas

El apéndice H.3 del artículo presenta el desarrollo en notación unificada. Para verificar una reducción en concreto se puede consultar aquí el texto del que procede. Los números a la izquierda son las líneas originales; el texto que sigue a la barra está transcrito literalmente. El índice [ORIGEN.tsv](ORIGEN.tsv) identifica los intervalos y la huella del archivo original completo.

| Pregunta | Dónde comprobarla |
|---|---|
| ¿De dónde sale la inversa acotada en norma del supremo? | [Parte 04](parte_04.txt), aplicación al operador y lema con prueba de la cota en norma del supremo. |
| ¿En qué clase son uniformes las siete variables? | [Parte 08](parte_08.txt), líneas 6–38 y 59–111. Las constantes dependen del techo de las masas y de la brecha de torres. |
| ¿Cómo se construye el punto de prueba y se controla el error de Newton? | [Potencial dual](parte_05.txt), [desplazamiento](parte_06.txt), [energía y resto cúbico](parte_07.txt) y [cotas del par](parte_09.txt). |
| ¿Por qué se distingue la componente diagonal del gradiente de la componente después de aplicar la inversa? | [Gradiente y valor en el punto de prueba](parte_10.txt) y [parte 11](parte_11.txt), pasos (c)–(f). En el primer caso queda un término lineal en p+q. El complemento de Schur lo cancela en el segundo caso. |
| ¿Cómo se obtiene el término de traza? | [Parte 14 completa desde el enunciado](parte_14.txt) y [continuación de su prueba](parte_15.txt), desde la línea 4. La traza cuadrática da ocho veces el producto de los pesos al cuadrado, antes del factor 1/4. |
| ¿Cómo se eliminan las sumas sobre las demás casillas? | [Parte 15](parte_15.txt), lema de reducción local y demostración final. Se indica qué sustituciones cuestan como máximo una constante de clase por la quinta potencia del tamaño inverso. |
| ¿Cómo se reproduce el coeficiente? | [Comparación exacta](../cuadrado/comprobar_una_linea.py), [fórmula local](../cuadrado/orden4.py) y [series racionales](../cuadrado/series.py). Ejecutar desde la carpeta cuadrado: `python -B comprobar_una_linea.py`. |

La prueba archivada está en punto10_texto_v8_revisado_20261122T1629Z/tex. Las marcas históricas en sus líneas describen el momento de escritura. La cronología posterior figura en [trazabilidad de torres](../traza_torres.md). El cálculo exacto verifica el polinomio de grado cuatro. El control analítico de las cinco potencias procede del desarrollo en la clase indicada. El resultado se usa para un solo par de casillas en filas y columnas distintas.
