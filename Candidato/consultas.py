from Candidato.modelo import Candidato, Candidato_apoyo
import db


def obtener_candidatos_db():
    """
    Obtener todos los candidatos
    query:
        select * from candidato;
    """
    candidato = db.session.query(Candidato).all()
    return candidato


def obtener_candidato_por_cedula(cedula: str):
    candidato = db.session.query(Candidato).where(Candidato.cedula == cedula).first()

    if not candidato:
        return None

    candidato_dict = {
        "cedula": candidato.cedula,
        "nombre": candidato.nombre,
        "apellidos": candidato.apellidos,
        "email": candidato.email,
        "celular": candidato.celular,
        "fotografia": candidato.fotografia,
    }
    return candidato_dict

def crear_candidato_query(candidato: Candidato_apoyo):

    # se crea la variable candidato_bd basados en el modelo candidato
    candidato_bd = Candidato(
        cedula = candidato.cedula,
        nombre = candidato.nombre,
        apellidos = candidato.apellidos,
        email = candidato.email,
        celular = candidato.celular,
        fotografia = candidato.fotografia,
    )

    try: # Si la insercion sale bien nos dice "El candidato se ha creado"
        db.session.add(candidato_bd)
        db.session.commit()
        return "El candidato se ha creado"
    except: # Si no sale bien nos dice "No se ha creado el candidato"
        return "No se ha creado el candidato"
