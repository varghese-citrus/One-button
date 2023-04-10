Feature:Role Change

  @role_change
  Scenario:One Button Role Change
    Given I load the uam website
    When Provide the username <username> and password <password>
    And Click on the Login button
    Then Login is successful and uam page is loaded and verified
    Then Navigate to Apps menu and Click on one-button redesign
    Then Drag and Drop a user from Wolf_Admin to Sales-Rep
    Then Confirm the Role details and Click on Save.

