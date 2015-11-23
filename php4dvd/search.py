from model.user import User
from model.search import Search
#from selenium_fixture import app


def test_search_with_invalid_credentials(app):
    app.login(app.driver, User.Admin())
    assert app.is_logged_in()
    app.search(Search.Negative())
    assert app.not_found()

def test_search_with_valid_credentials(app):
    app.login(app.driver, User.Admin())
    assert app.is_logged_in()
    app.search(Search.Positive())
    assert app.something_found()


