# Activitats
1- (testunitaris.md) Què són els tests unitaris?

Són tests automàtics que comproven que les parts individuals del codi (funcions, mètodes o classes) funcionen bé. Ajuden a: 
- **Detectar falles abans de la seva publicació**. 
- **Assegurar que el codi opera com es vol.**
- **Fer més senzill el manteniment del codi.** 

2- (testunitaris.md) Fes una recerca de llibreries de test amb Python. Com funciona específicament la llibreria unittest de Python?

# Llibreries conegudes per a proves en Python

- **unittest**: (inclosa dins de la biblioteca estàndard).  

- Basat en el framework de proves unitàries de Java (JUnit).
- Permet crear proves amb **TestCase**, **assertEqual**, **setUp**, **tearDown**...

## **pytest** (més simple i fliexible).  

- No requereix classes per escriure proves.
- Compatible amb **unittest**.
- Permet fixtures (cosa fixa), parametrització i plugins.

## **nose2** (millora de `nose`, que funciona amb `unittest`).  

- Extend a **unittest** i ofereix auto-descobriment de proves.
- Menys popular que **pythest** peò amb utilitat.

## **doctest** (natiu): 
- Permet escriure proves dintre de la documentació de proves.
- Compara la sortida esperada amb la real directament en docstrings.

## **hypothesis**:
- Permet proves basades en propietats generant dades aleatòries.
- Útil per proves de casos límit i entrades inesperades.

## Com opera unittest?

`unittest` és un sistema basat en JUnit (Java). Es fa servir així:

- Crear una classe que hereti de `unittest.TestCase`.  
- Definir mètodes que comencin amb `test_`.  
- Utilitzar assertaments per comprovar els resultats.


3-  (prototip3/testsuma.py) Exercici exemple test.
Creació i execució d’un test senzill  amb Python per exemple testejar una funció de suma. Genera un fitxer python que testeji aquesta funció.

def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

4- (prototip3/testfuncions.py) Exercici exemple varies  funcions.
Testeja més funcions, afegeix una resta i una divisió (que retorni un error quan la divisió és per 0)  

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

5-  (testunitaris.md) Fes una Llista de les assertions més importants en unittest i explica per a que  serveixen.

- **assertEqual(a,b)**: Revisa que a sigui igual a b.
- **assertNotEqual(a,b)**: Revisa que a sigui diferent a b.
- **assertTrue(x)**: Revisa que x sigui certa.
- **assertFalse(x)**: Comprova que x no sigui correcta.
- **assertIs(a,b)**: Revisa que a sigui el mateix objecte que b.
- **assertIsNone(a,b)**: Revisa que a estigui en b (llista, diccionari...).
- **assertRaises(Error, funció)**: Revisa que la funció llença una excepció.

6-  (prototip3/testBackend.py)  Fes els tests Unitaris dels teus DAO i webservice del prototip 2 que tens a la carpeta prototip 3