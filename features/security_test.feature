Feature: Testing Security
	
	Scenario: Try going to the students database without logging in
		Given I go to the admin login page
			When I enter the wrong username "prueba" with "12345" as the password
			Then It should not let me go to the students database
			
	Scenario: Try going to the books download page without logging in 
		Given I go to the student login page
		When I enter a student that does not exist with carnet "00000001"
		Then It should not let me go to the students book download page
		
	Scenario: Try going to the books view page without logging in
		Given I go to the student login page
			When I enter a student that does not exist with carnet "00000002"
			Then It should not let me go to the book viewer page