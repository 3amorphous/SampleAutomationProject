@dragdrop #Script "behave -tags=dragdrop" to only run this feature
Feature: Drag and drop elements

    Scenario: [TC-003] Drag element to dropzone
    When User selects draggable element
    When User drops element to dropzone
    Then User sees "Dropped" text

    Scenario: [TC-004] Drag element outside of the dropzone
    When User selects draggable element
    Then User drops element anywhere in the page

    Scenario: [TC-005] Resize an element
    When User selects resizeable element
    Then User is able to resize an element to be bigger

