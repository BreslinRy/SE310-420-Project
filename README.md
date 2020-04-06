# SE310-420-Project
<pre>
KNOWN BUG LIST:<br />
  Bug Name: User can vote for more than one candidate
	Bug Classification: defect
	Bug Location: GUI.py
	Bug Priority: 3
	How to reproduce:
		1.  User Selects both candidates
		2.  User submits vote
  Expected Result:
    Clears users previous input when another candidate is selected.
  Actual Result: 
	  Saves users vote as one for each candidate.
****************************************************************************************************
  Bug Name: Program doesn't save the votes
	Bug Classification: defect
	Bug Location: System Wide
	Bug Priority: 1
	How to reproduce:
		1.  Submits a vote
  Expected Result:
    User vote saved to a database.
  Actual Result: 
	  User vote is lost.
 	****************************************************************************************************
	Bug Name: Exiting the gui before submitting counts the votes
	Bug Classification: defect
	Bug Location: GUI.py
	Bug Priority: 2
	How to reproduce:
		1. User selects a candidate to vote for
		2. User exits the program without submitting vote 
  Expected Result:
    Users session is voided and vote is not counted
  Actual Result: 
	  Vote is counted
****************************************************************************************************
  Bug Name: Count Function can count more or less than one vote per session
	Bug Classification: enhancement
	Bug Location: count.py
	Bug Priority: 4
	How to reproduce:
		1. Any number other than one or zero is used as a parameter to count function
  Expected Result:
    Count function increments by one if vote was passed for a certain user
  Actual Result: 
	  Count function adds the number that was inserted as a parameter to count to the existing data. 
****************************************************************************************************
  Bug Name: Shrinking window results in hidden information in Gui
	Bug Classification: enhancement
	Bug Location: GUI.py
	Bug Priority: 5
	How to reproduce:
		1. User shrinks the program window until the UI is no longer visible
  Expected Result:
    UI is centered as the window shrinks or grows.
  Actual Result: 
	  As  the window shrinks the UI remains anchored to its position on screen even if the window is longer able to view that position.
****************************************************************************************************
</pre>
