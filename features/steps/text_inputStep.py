from behave import *
from selenium.webdriver.common.by import By
import time

expectedName = "Angel"
expectedEmail = "sample_email@gmail.com"
expectedPhone = "+639123456789"
expectedAddress = "Manila, Philippines"

# Send a text input on each of the text fields
@when('User enters a name')
def enterName(context):
    context.driver.find_element(By.ID, "name").send_keys(expectedName)

@when('User enters an email')
def enterEmail(context):
    context.driver.find_element(By.ID, "email").send_keys(expectedEmail)

@when('User enters a phone number')
def enterPhoneNumber(context):
    context.driver.find_element(By.ID, "phone").send_keys(expectedPhone)

@when('User enters an address')
def enterAddress(context):
    context.driver.find_element(By.ID, "textarea").send_keys(expectedAddress)

# Script to verify that the text input by the user is correctly placed on each text field
@then('User sees that all fields are fulfilled')
def fulfilledFields(context):

    actualName = context.driver.find_element(By.ID, "name")
    assert actualName.get_attribute('value') == expectedName

    actualEmail = context.driver.find_element(By.ID, "email")
    assert actualEmail.get_attribute('value') == expectedEmail

    actualPhone = context.driver.find_element(By.ID, "phone")
    assert actualPhone.get_attribute('value') == expectedPhone

    actualAddress = context.driver.find_element(By.ID, "textarea")
    assert actualAddress.get_attribute('value') == expectedAddress
    time.sleep(3)

# Script to verify that the text input by the user is correctly placed on each text field
@when('User sees that all fields are currently fulfilled')
def currentlyFulfilled(context):

    actualName = context.driver.find_element(By.ID, "name")
    assert actualName.get_attribute('value') == expectedName

    actualEmail = context.driver.find_element(By.ID, "email")
    assert actualEmail.get_attribute('value') == expectedEmail

    actualPhone = context.driver.find_element(By.ID, "phone")
    assert actualPhone.get_attribute('value') == expectedPhone

    actualAddress = context.driver.find_element(By.ID, "textarea")
    assert actualAddress.get_attribute('value') == expectedAddress
    time.sleep(3)

# Script to clear all the fulfilled text fields
@when('User deletes all fulfilled text fields')
def deleteTextInput(context):
    context.driver.find_element(By.ID, "name").clear()
    context.driver.find_element(By.ID, "email").clear()
    context.driver.find_element(By.ID, "phone").clear()
    context.driver.find_element(By.ID, "textarea").clear()

# Script to verify that the text fields are cleared
@then('User sees that text fields are cleared')
def step_impl(context):

    actualName = context.driver.find_element(By.ID, "name")
    assert actualName.get_attribute('value') == ""

    actualEmail = context.driver.find_element(By.ID, "email")
    assert actualEmail.get_attribute('value') == ""

    actualPhone = context.driver.find_element(By.ID, "phone")
    assert actualPhone.get_attribute('value') == ""

    actualAddress = context.driver.find_element(By.ID, "textarea")
    assert actualAddress.get_attribute('value') == ""
    time.sleep(3)
