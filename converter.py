# FUNZIONI
somma = """
def somma(a, b):
    somma = str(a + b)
    print("la somma e': ", somma)
"""
sottrazione = """
def sottrazione(a, b):
    differenza = str(a - b)
    print("la differenza e': ", differenza)
"""
moltiplicazione = """
def moltiplicazione(a, b):
    prodotto = str(a * b)
    print("il prodotto e': ", prodotto)
"""
divisione = """
def divisione(a, b):
    quoziente = str(a / b)
    print("il quoziente e': ", quoziente)
"""

def converti_codice_pyita_a_python(pyita_codice):
    # Sostituisci le corrispondenze delle parole chiave
    # FUNZIONI
    pyita_codice = pyita_codice.replace("somma_f", somma)
    pyita_codice = pyita_codice.replace("sottrazione_f", sottrazione)
    pyita_codice = pyita_codice.replace("moltiplicazione_f", moltiplicazione)
    pyita_codice = pyita_codice.replace("divisione_f", divisione)
    # ESECUZIONE DELLE FUNZIONI
    pyita_codice = pyita_codice.replace("somma(", "somma(")
    pyita_codice = pyita_codice.replace("sottrazzione(", "sottrazzione(")
    pyita_codice = pyita_codice.replace("moltiplicazione(", "moltiplicazione(")
    pyita_codice = pyita_codice.replace("divisione(", "divisione(")
    # COMANDI
    pyita_codice = pyita_codice.replace("definisci", "def")
    pyita_codice = pyita_codice.replace("stampa(", "print(")
    pyita_codice = pyita_codice.replace("per", "for")
    pyita_codice = pyita_codice.replace("nel", "in")
    pyita_codice = pyita_codice.replace("range(", "range(")
    pyita_codice = pyita_codice.replace("intero(", "int(")
    pyita_codice = pyita_codice.replace("se", "if")
    pyita_codice = pyita_codice.replace("altrimenti", "else")
    pyita_codice = pyita_codice.replace("se-altrimenti", "elif")
    pyita_codice = pyita_codice.replace("ritorna", "return")
    pyita_codice = pyita_codice.replace("input(", "input(")

    return pyita_codice

def converti_file_pyita_a_python(input_file, output_file):
    with open(input_file, 'r') as file:
        codice_pyita = file.read()

    codice_python = converti_codice_pyita_a_python(codice_pyita)

    with open(output_file, 'w') as file:
        file.write(codice_python)

if __name__ == "__main__":
    input_file_path = "esempio.pita"
    output_file_path = "esempio.py"

    converti_file_pyita_a_python(input_file_path, output_file_path)
    print(f"Conversione completata. Output salvato in {output_file_path}")