Feature: Validate the login feature

  @valid_login
  Scenario:Login with valid credentials
    Given I load the website
    Given Provide the username <username> and password <password>
    And Click on the Login button
    Then Login is successful and the OneButton dashboard is opened
    Then Close the browser
