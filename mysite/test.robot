*** Variables ***

${HOSTNAME}             127.0.0.1
${PORT}                 8000
${SERVER}               http://${13.58.213.46}:${80}/
${BROWSER}              chrome


*** Settings ***

Documentation   Django Robot Tests
Library         SeleniumLibrary  timeout=10  implicit_wait=0
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=mysite/mysite  manage=mysite/manage.py  settings=mysite.settings
Suite Setup     Start Django and open Browser
Suite Teardown  Stop Django and close Browser
Stop Django and close browser
  Close Browser
  Stop Django


*** Test Cases ***

Scenario: As a student I can log in with my carnet
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  It worked!
  Page Should Contain  Congratulations on your first Django-powered page.