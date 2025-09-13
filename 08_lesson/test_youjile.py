import pytest
from youjile_project import YoujileProject

api = "https://ru.yougile.com"


@pytest.fixture
def project_youjile():
    token = " "  # Ваш токен
    return YoujileProject(api, token)


def test_create_project(project_youjile):
    name = "Luna"
    resp = project_youjile.create_project(name)
    assert resp.status_code == 201
    assert resp.json() is not None  # Проверка, что ответ не None
    assert 'id' in resp.json(), "Response does not contain 'id'"


def test_get_project_by_id(project_youjile):
    name = "Family"
    resp = project_youjile.create_project(name)
    project_data = resp.json()
    new_id = project_data["id"]
    result = project_youjile.get_project_by_id(new_id)
    assert result.status_code == 200
    result_data = result.json()
    assert result_data["id"] == new_id
    assert result_data["title"] == name


def test_edit_project(project_youjile):
    name = "Theater"
    resp = project_youjile.create_project(name)
    project_data = resp.json()
    new_id = project_data["id"]

    new_name = "Favorite theater"
    result = project_youjile.edit_project(new_id, new_name)
    assert result.status_code == 200
    result_data = result.json()
    assert result_data["id"] == new_id


def test_create_project_negative(project_youjile):
    name = ""
    resp = project_youjile.create_project(name)
    assert resp.status_code == 400, (
        f"Create project failed: {resp.status_code}{resp.text}")
    response_data = resp.json()
    assert 'error' in response_data, (
        "Response does not contain 'error'")


def test_get_project_incorrect_id(project_youjile):
    incorrect_id = "AAAAAAAAAAAAAAAAAAAAAA000000000"
    resp = project_youjile.get_project_by_id(incorrect_id)
    assert resp.status_code == 404, (
        f"Expected 404 status code, got {resp.status_code}")
    resp_data = resp.json()
    assert resp_data["error"] == "Not Found"
    assert resp_data["message"] == "Проект не найден"


def test_edit_project_negative(project_youjile):
    name = "Space"
    resp = project_youjile.create_project(name)
    project_data = resp.json()
    new_id = project_data["id"]

    new_name = ""
    result = project_youjile.edit_project(new_id, new_name)
    assert result.status_code == 400
    result_data = result.json()
    assert result_data["error"] == "Bad Request"
    assert result_data["message"] == ["title should not be empty"]
