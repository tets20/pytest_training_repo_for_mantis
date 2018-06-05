from random import randrange

def test_delete_random_project(app):
    app.session.login("administrator", "root")
    app.action.go_to_project_page('http://localhost/mantisbt-1.2.20')
    #app.action.create_project('Test_Project','Test_description')
    index=randrange(len(app.action.get_list_of_project()[1:]))
    print(index)
    app.action.delete_project_by_index(index)

