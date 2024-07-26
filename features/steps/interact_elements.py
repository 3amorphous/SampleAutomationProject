from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Script to tick "Male" radio button
@when('User ticks Male radio button option')
def tickRadiobutton(context):
    context.driver.find_element(By.ID, "male").click()

# Script to confirm that "Male" radio button is selected
@then('User sees that Male radio button is ticked')
def verifyRadiobutton(context):
    context.driver.find_element(By.ID, "male").is_selected()
    time.sleep(3)

# Script to check all checkboxes from Monday to Friday
@when('User ticks Monday to Friday checkboxes')
def tickCheckboxes(context):
    context.driver.execute_script("window.scrollBy(0,350)")
    context.driver.find_element(By.ID, "monday").click()
    context.driver.find_element(By.ID, "tuesday").click()
    context.driver.find_element(By.ID, "wednesday").click()
    context.driver.find_element(By.ID, "thursday").click()
    context.driver.find_element(By.ID, "friday").click()

# Script to confirm that all checkboxes on weekdays are checked
@then('User sees that Monday to Friday checkboxes are ticked')
def verifyCheckboxes(context):
    context.driver.find_element(By.ID, "monday").is_selected()
    context.driver.find_element(By.ID, "tuesday").is_selected()
    context.driver.find_element(By.ID, "wednesday").is_selected()
    context.driver.find_element(By.ID, "thursday").is_selected()
    context.driver.find_element(By.ID, "friday").is_selected()
    time.sleep(3)

# Script to scroll to element
@when('User scrolls down to drop down list')
def openDropdown(context):
    context.driver.execute_script("window.scrollBy(0,350)")

# Script to open drop down and select "France" option
@when('User selects France option')
def selectFrance(context):
    dropdown = context.driver.find_element(By.ID, "country")
    dropdownOption = Select(dropdown)
    dropdownOption.select_by_visible_text("France")

# Script to verify that "France" option is selected
@then('User sees that France is selected')
def verifyFrance(context):
    activeDropdown = context.driver.find_element(By.ID, "country")
    select = Select(activeDropdown)

    currentOption = select.first_selected_option
    assert currentOption.get_attribute('value') == "france"
    time.sleep(3)

# Script to scroll down to date picker and click date picker
@when('User selects a date')
def selectDate(context):
    context.driver.execute_script("window.scrollBy(0,900)")
    context.driver.find_element(By.ID, "datepicker").click()
    time.sleep(1)

    context.driver.find_element(By.LINK_TEXT, "31").click()

# Script to verify that correct date is selected
@then('User sees selected date on text field')
def verifySelectedDate(context):
    actualDate = context.driver.find_element(By.ID, "datepicker")
    assert actualDate.get_attribute('value') == "07/31/2024"
    time.sleep(3)

# Script to scroll down and click hyperlink
@when('User clicks hyperlink')
def clickHyperlink(context):
    context.driver.execute_script("window.scrollBy(0,900)")
    context.driver.find_element(By.LINK_TEXT, "orange HRM").click()
    time.sleep(3)

# Script to verify that user is redirected to new page
@then('User is redirected to selected hyperlink page')
def verifyPage(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/h5')
    time.sleep(3)

