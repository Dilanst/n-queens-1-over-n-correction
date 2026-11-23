"""Lightweight dependency test. Run from any working directory; does not modify source files."""
import ast
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

BASE = Path(__file__).resolve().parent


def execute(arguments, work=None):
    subprocess.run([sys.executable, "-B", *map(str, arguments)], cwd=work or BASE, check=True,
                   stdout=subprocess.DEVNULL)


def check():
    for filename in BASE.rglob("*.py"):
        ast.parse(filename.read_text(encoding="utf8"))
    with (BASE / "ORIGEN.tsv").open(encoding="utf8") as ledger:
        for row in csv.DictReader(ledger, delimiter="\t"):
            actual = hashlib.sha256((BASE / row["archive_member"]).read_bytes()).hexdigest()
            assert actual == row["distributed_hash"], row["archive_member"]
    with tempfile.TemporaryDirectory() as scratch:
        scratch = Path(scratch)
        log = scratch / "profile.json"
        execute(["perfil/coercividad.py", "perfil/certificado_M16d14.json",
                 "perfil/candidato_M16d14.json", log])
        original = json.loads((BASE / "perfil/log_M16d14.json").read_bytes())
        repeated = json.loads(log.read_bytes())
        for key in ["max_R1", "max_R2", "epsilon_S", "epsilon_u"]:
            assert repeated[key] == original[key], key
        execute(["-c", "import certifica_S_perfil as s; s.bridge(s.cub.BASE.parent/'base')"],
                BASE / "frontera")
        execute(["-c", "import pt2048 as p; p.control(); p.c.perfil(32)"], BASE / "pt")
        execute(["-c", "import medir; import evaluador; import geometria as g; "
                 "g.construir_perfil(8); g.verificar_huella(g.MODELO, g.NPZ)"], BASE / "nodo")
        rc = scratch / "rc.json"
        execute(["nodo/leer_anchura_rc.py", rc])
        assert json.loads(rc.read_bytes())["w_sobre_dos"] == "108349/262144"
    print("Inputs, archive hashes, profile radii, root data, tower product and RC interval validated.")


if __name__ == "__main__":
    check()
