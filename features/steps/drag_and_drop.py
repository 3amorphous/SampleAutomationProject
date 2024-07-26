from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

@when('User selects draggable element')
def selectElement(context):
    context.driver.execute_script("window.scrollBy(0,500)")
    context.driver.find_element(By.ID, "draggable")

# Script to hold the draggable element and then drop it to the dropzone
@when('User drops element to dropzone')
def dropElement(context):
    sourceElement = context.driver.find_element(By.ID, "draggable")
    targetElement = context.driver.find_element(By.ID, "droppable")
    actions = ActionChains(context.driver)

    actions.drag_and_drop(sourceElement, targetElement).perform()
    time.sleep(3)

# Used to confirm that the header text on the dropzone has changed and the element has been dragged to the dropzone
@then('User sees "Dropped" text')
def droppedText(context):
    context.driver.find_element(By.XPATH, "//*[@id='droppable']/p")
    time.sleep(3)

@then('User drops element anywhere in the page')
def droppedElement(context):
    sourceElement = context.driver.find_element(By.ID, "draggable")
    actions = ActionChains(context.driver)

    actions.drag_and_drop_by_offset(sourceElement, 500, 250).perform()
    time.sleep(3)

@when('User selects resizeable element')
def findResizeableElement(context):
    context.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    context.driver.find_element(By.ID, "resizable")

# Script to resize the element to a bigger size
@then('User is able to resize an element to be bigger')
def resizeElement(context):
    resizeableElement = context.driver.find_element(By.XPATH, "//div[@id='resizable']/div[3]")
    actions = ActionChains(context.driver)

    actions.drag_and_drop_by_offset(resizeableElement, 250, 250).perform()
    time.sleep(3)
