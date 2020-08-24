# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.ebok -t test_ebok.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.ebok.testing.MEDIALOG_EBOK_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_ebok.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Ebok
  Given a logged-in site administrator
    and an add ebok form
   When I type 'My Ebok' into the title field
    and I submit the form
   Then a ebok with the title 'My Ebok' has been created

Scenario: As a site administrator I can view a Ebok
  Given a logged-in site administrator
    and a ebok 'My Ebok'
   When I go to the ebok view
   Then I can see the ebok title 'My Ebok'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ebok form
  Go To  ${PLONE_URL}/++add++Ebok

a ebok 'My Ebok'
  Create content  type=Ebok  id=my-ebok  title=My Ebok


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the ebok view
  Go To  ${PLONE_URL}/my-ebok
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ebok with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ebok title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
