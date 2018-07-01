def test_login_as_admin(app, admin):
    app.main_page.sign_in_link.click()
    assert app.login_window.is_here()
    app.login_window.username_field.send_keys(admin.username)
    app.login_window.password_field.send_keys(admin.password)
    app.login_window.click_sing_in_btn()
    assert app.dash_page.is_here()
