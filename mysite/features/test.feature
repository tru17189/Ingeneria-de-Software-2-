Feature: showing off behave
	
	Scenario: run a simple test
		Given we have behave installed
			When we implement a test	
			Then behave will test it for us!
			
	Scenario: Search for an existing student
		Given I search for an existing student
		Then the resulting page will include "Nombre"