import pytest
import klasser

STEIN = 0
SAKS = 1
PAPIR = 2

# Enkel test:
def test_stein_saks_papir():
    assert klasser.stein_saks_papir(SAKS, STEIN) == STEIN


# Test med parametere:
@pytest.mark.parametrize("type1,type2,resultat", [
    (STEIN, SAKS, STEIN),
    (PAPIR, STEIN, PAPIR),
    (PAPIR, SAKS, SAKS),
    (STEIN, STEIN, STEIN),
])
def test_stein_saks_papir_parameter(type1, type2, resultat):
    assert klasser.stein_saks_papir(type1, type2) == resultat
