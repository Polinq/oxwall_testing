def test_login_as_admin(app, admin):
    app.main_page.sign_in_link.click()
    assert app.login_window.is_here()
    assert app.login_window.username_field.placeholder == "Username/Email"
    assert app.login_window.password_field.placeholder == "Password"
    app.login_window.username_field.input(admin.username)
    app.login_window.password_field.input(admin.password)
    app.login_window.click_sing_in_btn()
    assert app.dash_page.is_here()


def test_login(app, regular_user):
    app.main_page.sign_in_link.click()
    assert app.login_window.is_here()
    app.login_window.username_field.input(regular_user.username)
    app.login_window.password_field.input(regular_user.password)
    app.login_window.click_sing_in_btn()
    assert app.dash_page.is_here()
