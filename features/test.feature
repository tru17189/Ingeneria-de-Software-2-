Feature: Testing Functionality
	
	Scenario: Go to the admin view
		Given I go to the admin login page
			When I enter the username "val17102" with the password	
			Then I will go to the admin view
			
	Scenario: Search for an existing student and load instructions
		Given I search for an existing student with carnet "17102"
		Then the resulting page will be the instructions
		
	Scenario: Go to the books page
		Given I search for an existing student with carnet "31082019"
			When I go to the instructions page and continue	
			Then I will go to the books view