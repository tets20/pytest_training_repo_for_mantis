# -*- coding: utf-8 -*-
from fixture.application import Application
#from fixture.db import DbFixture
#import jsonpickle
import importlib
import os.path
import pytest
import json

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser,base_url=web_config["baseUrl"])

    return fixture



@pytest.fixture(scope="session",autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action ="store",default="firefox" )
    parser.addoption("--target", action="store", default="target.json")
    #parser.addoption("--check_ui", action="store_true")#Store_true -автоматически, если она есть и отдает False, если нет.





'''
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")#Булево, либо она есть при запуске, либо ее нет.
    '''


'''
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            Testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, Testdata,ids=[str(x) for x in Testdata])
        elif fixture.startswith("json_"):
            Testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, Testdata,ids=[str(x) for x in Testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).Testdata

def load_from_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
'''
