"""Prueba previa de coste o integral completa. Un proceso, un hilo BLAS."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import platform
import sys
import threading
import time
from datetime import datetime, timezone

inicio=time.process_time()
pared=time.perf_counter()
for clave in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","BLIS_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[clave]="1"
import numpy as np
import geometria
from evaluador import Evaluador, evaluar


def guardar(ruta,obj):
    with open(ruta,"x",encoding="utf-8") as f:
        json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False)
        f.write("\n")


def vigilar(tope):
    while time.process_time()-inicio<tope-2:
        time.sleep(.25)
    print("Límite preventivo de CPU alcanzado",file=sys.stderr,flush=True)
    os._exit(88)


def ejecutar():
    p=argparse.ArgumentParser()
    p.add_argument("modo",choices=("coste","completo"))
    p.add_argument("n",type=int,choices=(8,16))
    p.add_argument("salida",type=Path)
    args=p.parse_args()
    if args.salida.exists():
        raise FileExistsError(args.salida)
    threading.Thread(target=vigilar,args=(2400 if args.modo=="completo" else 180,),
                     daemon=True).start()
    geo=geometria.preparar(args.n)
    num=len(geo.peso)
    preparacion=time.process_time()-inicio
    meta={"utc":datetime.now(timezone.utc).isoformat(),"modo":args.modo,"nodo":"GL20 nº 10",
          "x":geo.x.tolist(),"paneles_integracion_por_unidad":args.n,"paneles_fuente_por_unidad":256,
          "centros":num,"pares_orientados_posibles":int(geo.posible.sum()),"lineas":geo.L,
          "cpu_preparacion_s":preparacion,"sha256_modelo":geometria.NPZ,
          "python":platform.python_version(),"numpy":np.__version__,"blas_hilos":1}
    if args.modo=="coste":
        motor=Evaluador(geo)
        ids=np.linspace(0,num-1,16,dtype=int).tolist()
        t0=time.process_time()
        for c in ids:
            motor.centro(c)
        gasto=time.process_time()-t0
        meta.update(centros_cronometrados=ids,cpu_muestra_s=gasto,
                    proyeccion_lineal_s=preparacion+num*gasto/len(ids))
    else:
        def progreso(c,partidas):
            if (c+1)%128==0:
                print(f"{c+1}/{num} centros; CPU {time.process_time()-inicio:.2f} s",flush=True)
        total=evaluar(geo,progreso)
        cajas={k:i.tolist() for k,i in total.items()}
        assert all(np.isfinite(lo) and np.isfinite(hi) and lo<=hi for lo,hi in cajas.values())
        q=total["Q2"]
        radio=float(np.nextafter(np.nextafter(q.hi-q.lo,np.inf)*.5,np.inf))
        meta.update(intervalos=cajas,semiancho_superior=radio)
    meta.update(cpu_s=time.process_time()-inicio,pared_s=time.perf_counter()-pared)
    guardar(args.salida,meta)
    print(json.dumps({k:v for k,v in meta.items() if k!="intervalos"},ensure_ascii=True),flush=True)


if __name__=="__main__":
    ejecutar()

