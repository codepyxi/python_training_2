# -*- coding: utf-8 -*-

def test_del_contact(app):
    app.contact.delete_contact()
    app.open_home_page()
