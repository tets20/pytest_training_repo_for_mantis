from test_data.testdata import Testdata



def test_add_project(app):
    app.session.login("administrator", "root")
    app.action.go_to_project_page('http://localhost/mantisbt-1.2.20')
    app.action.create_project(Testdata)
