# Python_Guess

Guess is a class that has the following structure:

Guess(Minimum, Maximum, Target_number, Filename)
Inputs:
<ol>
<li>Minimum - Integer (0 < Minimum < Maximum), -1 for random game.</li>
<li>Maximum - Integer (Minimum < Maximum < INF) </li>
<li>Target_Number - Integer (Minimum <= Target_number <= Maximum)</li>
<li>Filename - String (Must specify file extension. IE. filename.txt, saved.csv, etc) Can be NONE or blank.</li>
</ol>
<br>If you want to play a random game, set Minimum to -1.<br>
<br>If you want to set a range, but random target within set Target_number to -1<br>
<br>To run call function Guess.playGame()<br>
<br>Automated guessing function (recursive): call Guess.ai_Play()<br>

<br>simple game with error handling<br>
