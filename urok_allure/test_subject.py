import allure
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from subject_page import SubjectPage

db_connection_string = "postgresql://postgres:0107@localhost:5432/QA"
db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)


@pytest.fixture(scope='module')
def db_session():
    session = Session()
    yield session
    session.close()


@allure.suite("Тесты на работу с предметами")
@allure.epic("Предметы")
@allure.severity("blocker")

@allure.story("Создание предмета")
@allure.feature("CREATE")
@allure.title("Создание нового предмета")
def test_insert(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.insert_subject('Astronomiya', 21)
    result = subject_page.get_subject('Astronomiya')
    with allure.step("Проверили, что предмет создался"):
        assert result is not None


@allure.story("Изменение предмета")
@allure.feature("UPDATE")
@allure.title("Корректировка названия предмета")
def test_update(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.update_subject(21, 'Finance')
    res = subject_page.get_subject_by_id(21)
    assert res is not None
    assert res['subject_title'] == 'Finance'


@allure.story("Удаление предмета")
@allure.feature("delete")
@allure.title("Удаление ненужного предмета")
def test_delete(db_session):
    subject_page = SubjectPage(db_session)
    subject_page.delete_subject('Finance')
    res_after_delete = subject_page.get_subject('Finance')
    assert res_after_delete is None
