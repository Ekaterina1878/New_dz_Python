import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SubjectPage import SubjectPage

db_connection_string = "postgresql://postgres:здесь должен быть пароль@localhost:5432/QA"
db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)


@pytest.fixture(scope='module')
def db_session():
    session = Session()
    yield session
    session.close()


def test_insert(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.insert_subject('Astronomiya', 21)
    result = subject_page.get_subject('Astronomiya')
    assert result is not None


def test_update(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.update_subject(21, 'Finance')
    res = subject_page.get_subject_by_id(21)
    assert res is not None
    assert res['subject_title'] == 'Finance'


def test_delete(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.delete_subject('Finance')
    res_after_delete = subject_page.get_subject('Finance')
    assert res_after_delete is None
