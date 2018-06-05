# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper
from project.project import Project
import time
import random
import string




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


class ProjectAction:

    def __init__(self, app):
        self.app = app


    def go_to_project_page(self,project_url):
        wd = self.app.wd
        wd.get(str(project_url) + '/manage_proj_page.php')
        time.sleep(3)


    def create_project(self,project):
        wd = self.app.wd
        wd.find_element_by_xpath('//table[3]/tbody/tr[1]/td/form').click()
        wd.find_element_by_name('name').send_keys(project.name)
        wd.find_element_by_name('description').send_keys(project.discription)
        wd.find_element_by_css_selector('input.button').click()
        time.sleep(3)


    def get_list_of_project(self):
        wd = self.app.wd
        list = []
        for project in wd.find_elements_by_xpath('//table[3]/tbody/tr'):
            list.append(project)
        #print(len(list))
        #print(list[2:])
        return list[2:]


    def delete_project_by_index(self,index):
        wd = self.app.wd
        '''all_list = []
        for elem in wd.find_elements_by_xpath('//table[3]/tbody/tr'):
            all_list.append(elem)
        list_proj = all_list[2:]
        for project in list_proj[index]:'''
        wd.find_element_by_xpath('//table[3]/tbody/tr['+ str(index+2) + ']/td[1]/a').click()
        time.sleep(2)
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        #time.sleep(1)
        wd.find_element_by_css_selector("input.button").click()
        time.sleep(5)

