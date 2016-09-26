FA Simulator
============

Written by: Dylan Greene
Updated on: 26 September 2016

To run the simulator, ensure that dfa.py is executable. To ensure this, simply
run the command 'chmod +x dfa.py'.

The simulator must be run with a FA definition file which follows the following
format:
  * Line 1: The name of the FA program.
  * Line 2: The alphabet to be used: only single ASCII letters are allowed,
  comma separated, as in a,b,c,…
  * Line 3: The names of the states, separated by commas, as in q0,q1,… There is
  no constraint on the length of a state name.
  * Line 4: The name of the state that should be considered the start state.
  * Line 5: A comma separated list of state names that should be marked as
  accepting states.
  * Line 6 and beyond: one transition rule per line, in the format:  
  <Initial_State_Name>,<Input_Symbol>,<New_State_Name>

Additionally, a test file must be supplied. The format for the test file is
simply one line for each string to be input to the machine.

To run the simulator with these two files, execute the command './dfa.py
DFA_DEFINITION_FILE TEST_STRING_FILE'. A help message will be displayed if
usage is incorrect.

 Once run, the simulator will print the state transitions for every string, as
 well as if each string is accepted or rejected by the machine.
