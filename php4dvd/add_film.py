from model.user import User
from model.film import Film
#from selenium_fixture import app

def add_film(app):

    app.login(app.driver, User.Admin())
    assert app.is_logged_in()
    app.add_film(Film.Positive())
    assert app.film_added()
    app.logout(app.driver)
    assert app.is_not_logged_in()


def add_film_with_invalid_credential(app):

    app.login(app.driver, User.Admin())
    assert app.is_logged_in()
    app.add_film(Film.Negative())
    app.show_error()
    app.logout(app.driver)
    assert app.is_not_logged_in()

