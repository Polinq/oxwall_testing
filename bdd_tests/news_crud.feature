#language: ru

Feature: Newsfeed (status) feature
  Description: User can add a news with photo and without photo.
  The news appears on Dashboard in few seconds after posting without page reloading.
  This news is displayed on Main page too.
  User can delete news added by him. Only admin can delete every news.

  Scenario Outline: Add newsfeed without photo (status)
    Given initial news in Oxwall database
    Given a news with text <text> and without any photo
    Given I as a logged admin
    When I add the news
    Then a new newsfeed block appears before old list of news
    Then this newsfeed block is with this text and author as Admin

    Examples:
    | text                |
    | !@#%^&<a *%^*{}))_+ |
    | New 1234098765!     |
    | Привіт!             |
