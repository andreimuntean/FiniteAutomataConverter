#!/usr/bin/python3
import sys
from enum import Enum

"""finiteAutomataConverter.py: Converts nondeterministic finite automata into deterministic finite automata."""

__author__ = "Andrei Muntean"

class AutomatonType(Enum):
    undefined = 0
    nondeterministic = 1
    deterministic = 2

class FiniteAutomaton:
    """Represents a finite automaton."""

    def __init__(self):
        pass

    def __init__(self, path):
        self.load(path)

    def load(self, path):
        """Loads the finite automaton from the specified path."""

        with open(path) as file:
            lines = file.readlines()

            for line in lines:
                pass

    def type(self):
        """Determines the type of this automaton."""

        return AutomatonType.undefined

def run():
    """Runs the program."""
    
    if len(sys.argv) > 1:
        automaton = FiniteAutomaton(sys.argv[1])
    else:
        automaton = FiniteAutomaton(input('> '))

run()