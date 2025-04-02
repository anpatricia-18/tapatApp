# Prototip 2

##  Implementació Prototip 2
[Wireframe Prototip 2](wireframe_prototip2.mermaid)
[Segon Wireframe que vaig fer pensant des de la vista de l'usuari/cuidador/metge](dgm_wireframeprototip2.mermaid)

### Backend:

[Backend Prototip 2](dgm_clase_backendprototip2.mermaid)


***Base de dades***:
- Usuaris: Informació dels cuidadors, infants i metges.
- Infants: Dades específiques de cada nen, incloent el tractament a seguir.
- Relacions: Vincle entre cuidadors i infants per gestionar correctament el tractament.


### Frontend:

[Frontend prototip 2](dgm_clase_frontendprototip2.mermaid)

***Vista d'Autentificació***:
- L'usuari accedeix a la Vista de Login i introduirà el seu nom o correu electrònic i la contrasenya.
- El servidor valida les credencials consultant la base de dades.
- Si l’usuari té autenticació en dos passos (2FA) activada, es demana un codi addicional.
- Si la informació és correcta, es concedeix l’accés i es redirigeix segons el seu rol.

***Vista per Restablir contrasenya***:
- Descripció: formulari per restablir contrasenya 
- Inputs: Email, nova contrasenya
- Botó: "Enviar enllaç de restabliment"
- - Si hi ha errors, es mostra un missatge d’error i es permet la recuperació de contrasenya mitjançant correu electrònic.

***Vista de Registre***:
- Descripció: formulari de Registre d'Usuari 
- Inputs: Usuari (email o username) i Contrasenya
- Botó: "Crear compte"

***Vista de Llistat d'Infants***:
- Descripció: mostra els infants assignats al cuidador
- Opcions: Seleccionar nen
- Botó: "Afegir un nen nou", seleccionar nen (click a sobre)

***Vista per Afegir un infant***:
- Descripció: formulari per afegir nen
- Input: Nom del nen, Edat, tractament (hores o percentatge)
- Botó: "Afegir", "Cancel·lar"

***Vista d'Informació de l'infant***:
- Descripció: pantalla per mostrar informació del nen i estat tap
- Input: estat del tap
- Botó: "Desar canvis", "Cancel·lar"

##  Diagrama d'arquitectura final del Prototip 2
[Arquitectura prototip 2](dgm_arquitecturap2.mermaid)



