Feature: Media/Photos functionality


#  Scenario: Admin login
#    Given Open Login page
#    When Login as "admin"
#    Then Verify user is logged in on the Home page
#    When Click "photos" in app menu on the Home page
#    And Select "Documents" folder on the Files page
#    And Select "Welcome to Nextcloud Hub" file on the Files page
#    Then Verify office document is opened on the Files page


  Scenario: Dashboard
    Given Open Login page
    When Login as "admin"
    Then Verify user is logged in on the Home page
    And Verify no widgets are present on the Home page
    When Click "Customize" button on the Home page
    Then Verify 'Edit widgets' modal-container is opened on the Home page
    When Select "Weather" widget in modal-container on the Home page
    And Close modal-container on the Home page
    Then Verify "Weather" widget is "VISIBLE" on the Home page
