import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# This script is executed before the step definition files
def before_scenario(context, scenario):
    print("\nChrome Driver Executed")
    context.driver = webdriver.Chrome(
        service=Service("C:\\Users\\admin\\PycharmProjects\\SampleAutomationProject\\features\\chromedriver.exe"))
    context.driver.maximize_window()
    context.driver.get("https://testautomationpractice.blogspot.com/")

# This script is executed after execution of step definition files
def after_scenario(context, scenario):
    # This line below is used to take a screenshot of the full page whenever the scenario is finished executing may it be PASSED or FAILED
    allure.attach(context.driver.get_screenshot_as_png(), name="scenario", attachment_type=AttachmentType.PNG)

    print("\nChrome Driver Closed")
    context.driver.quit()

# terminal commands
# behave -> run whole test suite (all features)
# behave --tags=<taghere> -> run specific feature
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features -> generate Allure report in JSON format
# allure serve reports -> generate Allure report with UIallure