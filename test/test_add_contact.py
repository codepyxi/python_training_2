# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Pierre", middlename="sto", lastname="stop", nickname="nik", title="title", company_name="Company", address="3096- rue goyer", home_phone="514", mobile_phone="515",
                               work_phone="516", fax="517", email="1@sto.com", second_email="2@sto.com", third_email="3@sto.com", homepage="sto.com", birthdate="18", birthmonth="January", birth_year="1971",
                               anniversary_day="18", anniversary_month="February", anniversary_year="2018", second_address="address second", second_home="home second", notes="notes"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middlename="", lastname="", nickname="", title="", company_name="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", second_email="", third_email="", homepage="", birthdate="-", birthmonth="-", birth_year="",
                               anniversary_day="-", anniversary_month="-", anniversary_year="", second_address="", second_home="", notes=""))
    app.session.logout()