@interact #Script "behave -tags=interact" to only run this feature
Feature: Interact with elements

    Scenario: [TC-006] Tick radio button
    When User ticks Male radio button option
    Then User sees that Male radio button is ticked

    Scenario: [TC-007] Tick check box
    When User ticks Monday to Friday checkboxes
    Then User sees that Monday to Friday checkboxes are ticked

    Scenario: [TC-008] Select from drop down list
    When User scrolls down to drop down list
    When User selects France option
    Then User sees that France is selected

    Scenario: [TC-009] Select from date picker
    When User selects a date
    Then User sees selected date on text field

    Scenario: [TC-010] Click a hyperlink
    When User clicks hyperlink
    Then User is redirected to selected hyperlink page