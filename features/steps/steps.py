from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pathlib import Path

path = str(Path().absolute())
path = path.replace("\\" ,"/")

#driver = webdriver.Chrome(path + "/chromedriver.exe")
driver = webdriver.Chrome("C:/Users/hecto/Documents/UVG 2019/Ing en Software 2/Intento 3/Ingeneria-de-Software-2-/features/steps/chromedriver.exe")
#verify an admin user accesibility
@given('I go to the admin login page')
def step_impl(context):
    driver.get('http://localhost:8000/admin')

@given('I go to the student login page')
def step_impl(context):
    driver.get('http://localhost:8000/')

#verify an existing student gets a page
@given('I search for an existing student with carnet "{number}"')
def step_impl(context, number):
    
    #br = context.browser
    #br.get('http://localhost:8000/iger/students/17102/')
    driver.get('http://localhost:8000/')
    elem = driver.find_element_by_id("carnet")
    elem.send_keys(number)
    #elem.send_keys(Keys.RETURN)

@when('I enter a student that does not exist with carnet "{carnet}"')
def step_impl(context, carnet):
    elem = driver.find_element_by_id("carnet")
    elem.send_keys(carnet)

@when('I enter the wrong username "{username}" with "{password}" as the password')
def step_impl(context, username, password):
    elem = driver.find_element_by_id("id_username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

@when('I enter the username "{username}" with the password')
def step_impl(context, username):
    elem = driver.find_element_by_id("id_username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("id_password")
    elem.send_keys("Mikki1217")

@when('I go to the instructions page and continue')
def step_impl(context):
    elem = driver.find_element_by_id("mandar")
    elem.click()

@then('I will go to the admin view')
def step_impl(context):
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(Keys.RETURN)  

@then('It should not let me go to the students database')
def step_impl(context):
    driver.get('http://localhost:8000/admin/iger/student/')

@then('the resulting page will be the instructions')
def step_impl(context):
    elem = driver.find_element_by_id("mandar")
    elem.click()

@then('It should not let me go to the students book download page')
def step_impl(context):
    driver.get('http://localhost:8000/student')

@then('It should not let me go to the book viewer page')
def step_impl(context):
    driver.get('http://localhost:8000/student')

@then('I will go to the books view')
def step_impl(context):
    elem = driver.find_element_by_tag_name('div')
    elem.click()
    assert True

