# Created by demetriswilliams at 31/05/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario Outline: Ensure User is able to successfully vote 'Guilty'
    Given user opens the homepage
    And user navigates to the vote page
    When user selects the "<verdict>" radio button
    And user clicks the vote button
    Then user sees the "<verdict_confirmation>" modal pop up

    Examples:
      | verdict | verdict_confirmation |
      | Guilty  | Guilty               |

  Scenario Outline: Ensure User is able to successfully vote 'Not Guilty'
    Given user opens the homepage
    And user navigates to the vote page
    When user selects the "<verdict>" radio button
    And user clicks the vote button
    Then user sees the "<verdict_confirmation>" modal pop up

    Examples:
      | verdict    | verdict_confirmation |
      | Not Guilty | Not Guilty           |


  Scenario Outline: As a User, I want to go back to the home page from the 'Press on a case' page
    Given user opens the homepage
    And user navigates to the next page
    When user clicks the back arrow on the browser
    Then user sees the home page

    Examples:
      | username | password |
      | admin    | admin123 |
      | test     | test     |

