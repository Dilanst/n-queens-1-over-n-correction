"""Misma cubatura G6, transfiriendo los radios mediante el certificado M16d14."""
import hashlib
import json
from fractions import Fraction as F
import certifica_S as cub

original = cub.input_data

def bridge(g6):
    cc,es_g6,eu_g6,hashes = original(g6)
    folder = cub.BASE.parent/'perfil'
    cert = folder/'certificado_M16d14.json'
    cand = folder/'candidato_M16d14.json'
    data = json.loads(cert.read_bytes())
    assert data['G6_sha256'] == hashes['candidato_coeficientes.json']
    assert data['NK_sha256'] == hashes['res_nk_4096.json']
    assert data['candidato_sha256'] == hashlib.sha256(cand.read_bytes()).hexdigest()
    # Los números impresos por el certificado son cotas superiores decimales.
    # Se redondean además a los siguientes extremos racionales, que dejan margen.
    es,eu = F('1.185e-11'),F('3.709e-14')
    assert F(data['sup_dist_G6']['S']) + F(data['epsilon_S']) < es < es_g6
    assert F(data['sup_dist_G6']['u']) + F(data['epsilon_u']) < eu < eu_g6
    assert F(data['distancia_ponderada']) + F(data['epsilon_S']) < F('1e-6')
    for f in (cert,cand,cub.BASE/'certifica_S_perfil.py'):
        hashes[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
    return cc,es,eu,hashes

if __name__ == '__main__':
    cub.input_data = bridge
    cub.main()
