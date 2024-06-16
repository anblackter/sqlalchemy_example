from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from models.person import Person
from schemas.person import PersonSchema


class PersonCRUD():
    """Person CRUD to handle the operations: Create, Read, Update and Delete within the database"""


    def add_person(self, db: Session, person: PersonSchema) -> None:
        """ADD person register from the person(PersonSchema) object to the database

            :param db: SQLAlchemy Session of the corresponding DB.
            :param person: Person to add in PersonSchema format
        """
        new_person = Person(**person.model_dump(exclude={'id'}))
        db.add(new_person)
        db.commit()


    def get_person(self, db: Session, id: int) -> PersonSchema:
        """GET the Person by the given id

            :param db: SQLAlchemy Session of the corresponding DB.
            :param id: id of the person to by found
        """
        try:
            person = db.query(Person).where(Person.id==id).one()
            person_schema = PersonSchema(**person.__dict__)
        except NoResultFound:
            return None
        except Exception as e:
            return None
        else:
            return person_schema


    def update_person(self, db: Session, person: PersonSchema) -> None:
        """UPDATE person information from the person(PersonSchema) object to the database.

            :param db: SQLAlchemy Session of the corresponding DB.
            :param person: Person to update in PersonSchema format
        """

        try:
            person_db = db.query(Person).where(Person.id==person.id)
        except NoResultFound:
            return None
        except Exception as e:
            return None
        else:
            person_db.update(values=person.model_dump(exclude={'id'}))
            db.commit()


    def delete_person(self, db: Session, id: int) -> None:
        """DELETE person by the given id.

            :param db: SQLAlchemy Session of the corresponding DB.
            :param id: id of the person to by deleted
        """

        try:
            person = db.query(Person).where(Person.id==id).one()
        except NoResultFound:
            return None
        except Exception as e:
            return None
        else:
            db.delete(person)
            db.commit()
