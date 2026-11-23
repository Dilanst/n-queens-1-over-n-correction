"""Extremos del certificado existente para las entradas R,C. No integra de nuevo."""
from pathlib import Path
from fractions import Fraction
import json
import sys
import time
t=time.process_time()
from geometria import MODELO, NPZ, verificar_huella
import numpy as np

verificar_huella(MODELO,NPZ)
with np.load(MODELO,allow_pickle=False) as datos:
    hoja=datos["hoja"]
    R=np.flatnonzero(hoja==0)[:,None]
    C=np.flatnonzero(hoja==1)[None,:]
    assert R.max()<C.min()
    ix=R*len(hoja)-R*(R+1)//2+C
    delta=datos["L_max"][ix].astype(np.int64)-datos["L_min"][ix].astype(np.int64)
    w=Fraction(int(delta.min()))*2**Fraction(int(datos["potencia_dos"]))
    assert w>0
    res={"casillas_RC":int(ix.size),"ticks_minimos":int(delta.min()),"ancho_minimo":str(w),
         "w_sobre_dos":str(w/2),"decimal_binario_exacto":float(w/2),"huella_NPZ":NPZ,
         "cpu_s":time.process_time()-t}
with open(sys.argv[1],"x",encoding="utf-8") as f:
    json.dump(res,f,indent=2)
print(res)

