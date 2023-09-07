Feature: Application menu functionality


   Scenario: Enable/Disable widgets
    Given Open Login page
    When Login as "admin"
    Then Verify user is logged in on the Home page
    And Verify no widgets are present on the Home page
    When Click "Customize" button on the Home page
    Then Verify 'Edit widgets' modal-container is opened on the Home page
    When Select "Weather" widget in modal-container on the Home page
    And Close modal-container on the Home page
    Then Verify "Weather" widget is "VISIBLE" on the Home page


  Scenario: Photo/Video opening
    Given Open Login page
    When Login as "admin"
    Then Verify user is logged in on the Home page
    When Click "photos" in app menu on the Home page
    Then Verify App Navigation list is "VISIBLE" on the Photos page
    When Select "Photos" item in App Navigation menu on the Photos page
    And Select "Vineyard.jpg" image on the Photos page
    Then Verify modal-container is opened on the Photos page
    When Close modal-container on the Photos page
    And Select "Videos" item in App Navigation menu on the Photos page
    And Select "Nextcloud intro.mp4" video on the Photos page
    Then Verify modal-container is opened on the Photos page


  Scenario: Activity logging
    Given Open Login page
    When Login as "admin"
    Then Verify user is logged in on the Home page

    When Click "deck" in app menu on the Home page
    And Create a new "Activity logging" board on the Deck page
    And Click "activity" in app menu on the Home page
    Then Verify "You have created a new board Activity logging" message is "VISIBLE" on the Activity page

    When Click "deck" in app menu on the Home page
    And Open menu for "Activity logging" board on the Activity page
    And Select "Delete board" option from menu on the Activity page

    And Click "activity" in app menu on the Home page
    Then Verify "You have deleted the board Activity logging" message is "VISIBLE" on the Activity page
