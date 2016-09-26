#!/usr/bin/python

# Imports
# =============================================================================

import getopt
import sys
import os

# Global variables
# =============================================================================

PROGRAM_NAME    = os.path.basename(sys.argv[0])
FA_DEF_FILE     = ''
FA_IN_FILE    = ''

# Functions

def error(message, exit_code = 1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code = 0):
    error('''Usage: {} [ -h ] DFA_DEFINITION_FILE DFA_TEST_FILE

    Options:

        -h Show this help message'''
        .format(PROGRAM_NAME, exit_code))

# Parse command line arguments
# =============================================================================

try:
    options, arguments = getopt.getopt(sys.argv[1:], "h")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    else:
        usage(1)

if len(arguments) < 2 or len(arguments) > 2:
    usage(1)
else:
    FA_DEF_FILE = arguments[0]
    FA_IN_FILE = arguments[1]

# Main Execution
# =============================================================================

# Open the FA machine defition file and load its contents
with open(FA_DEF_FILE) as f:
    definition_lines = f.readlines()
# Strip the trailing whitespace from each line in the def file
for i in range(len(definition_lines)):
    definition_lines[i] = definition_lines[i].rstrip()

# Print the machine name
print definition_lines[0]
# Parse the rest of the machine defition
alphabet = definition_lines[1].split(",")
states = definition_lines[2].split(",")
start_state = definition_lines[3]
accepting_states = definition_lines[4].split(",")
rules = definition_lines[5:]
# Print the rules with associated rule number
rule_n = 0
for rule in rules:
    rule_n = rule_n + 1
    print "{}: {}".format(rule_n, rule)

# Print the name of the test file
print "Test File: {}".format(FA_IN_FILE)
# Open the FA test file and load its contents
with open(FA_IN_FILE) as f:
    input_lines = f.readlines()
# Strip the trailing whitespace from each line in the test file
for i in range(len(input_lines)):
    input_lines[i] = input_lines[i].rstrip()

# Loop over each of the test strings
for line in input_lines:
    print "String: {}".format(line) # Print the test string
    transitions = list(line) # Split the test string up
    next_state = start_state
    step = 0
    # Loop over each of the transitions in the test string
    for transition in transitions:
        curr_state = next_state
        next_state = None
        step = step + 1
        if not (transition in alphabet):
            error("{} not in the aplhabet".format(transition))
        rule_n = 0
        # Find a matching rule for the transition and current state
        for rule in rules:
            rule = rule.split(",")
            rule_n = rule_n + 1
            if rule[0] == curr_state and rule[1] == transition:
                next_state = rule[2]
                print "{}#{}: {},{},{}".format(step, rule_n,
                    curr_state, transition, next_state)
        if next_state is None:
            break
    if next_state in accepting_states:
        print "Accepted"
    else:
        print "Rejected"
