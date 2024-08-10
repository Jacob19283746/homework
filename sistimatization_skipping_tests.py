import unittest
from simple_unit_tests import RunnerTest
from unit_testing_methods import TournamentTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(suite)
