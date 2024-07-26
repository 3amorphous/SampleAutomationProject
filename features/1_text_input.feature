@textInput #Script "behave -tags=textInput" to only run this feature
Feature: Text Input

    Scenario: [TC-001] Fulfill blank text fields
    When User enters a name
    When User enters an email
    When User enters a phone number
    When User enters an address
    Then User sees that all fields are fulfilled

    Scenario: [TC-002] Fulfill blank text fields and then clear them
    When User enters a name
    When User enters an email
    When User enters a phone number
    When User enters an address
    When User sees that all fields are currently fulfilled
    When User deletes all fulfilled text fields
    Then User sees that text fields are cleared