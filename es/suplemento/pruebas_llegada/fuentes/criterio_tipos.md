# El paso entre el rango y la media

Para cada tipo realizable sea h el número de índices de fila y columna, D la dimensión y p el exponente disponible en su cota por soporte. La proposición externa da D≤p−1. Escribir d_rank=h−D y b_tipo=p−D−1. Para los tipos relevantes con conflicto diagonal, h≤4d_rank; por tanto D≤3d_rank. Se deduce 3(d_rank+b_tipo)≥D+b_tipo=p−1≥v−1 y así d_rank+b_tipo−1≥(v−4)/3. Se usa al extraer la potencia de δ_* en la media.

El peso combinatorio previo es C^v (4v²)^(L_s)/c!, con L_s≤b_tipo+2. Al combinarlo con j^(−b_tipo) aparece (v²/j)^b_tipo. Esta cota explica por qué es esencial el alcance v≤8 log n, con j=⌊bn⌋ y n grande, y por qué se conserva el factorial de componentes c!. La base C₁ de la suma final se fija en la clase de referencia. El peso de la prescripción es como máximo δ^(−2v)(j/n)^h exp(C_L v²/j) en la ley original con indicador de la llegada. Los detalles de la estimación completa están en [el acta de tipos, §§2–5](tipos.md). La parte de Cauchy presupone dominio holomorfo, cota exp(Cv) y anulación de jets. La revisión combinatoria no decide esas premisas.


La cota por soporte importada está cubierta por ACTA_jets y su alcance creciente por ACTA_t4_corolario, en las ubicaciones de MAPA.md. Para la cota determinista absoluta se usa directamente D≤p−1, desde v=5; la desigualdad de media (v−4)/3 cumple otra función.
