#!/usr/bin/env python3
from schemas.person import PersonSchema
from services.person import PersonCRUD

from utils.database import db_curriculum_vitae

engine, SessionLocal, Base = db_curriculum_vitae()

def run():
    db_cv_session = SessionLocal()
    person_CRUD = PersonCRUD()

    # Add a person
    person = PersonSchema(
        id=1,
        name='Angel',
        last_name='Henao',
        email='angel@outlook.com',
        phone='+57 3005505050',
        title='Developer',
        gender='M'
    )

    person_CRUD.add_person(db=db_cv_session, person=person)

    # Read the person with id 1
    person = person_CRUD.get_person(db=db_cv_session, id=1)
    print(person)

    # Update the person with id 1
    person_update = person
    person_update.email = 'angel100@gmail.com'

    person_CRUD.update_person(db=db_cv_session, person=person_update)

    person = person_CRUD.get_person(db=db_cv_session, id=1)
    print(person)

    # Delete the person with id 1
    person_CRUD.delete_person(db=db_cv_session, id=1)

if __name__ == '__main__':
    run()