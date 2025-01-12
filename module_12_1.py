import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Walker')
        for i in range(10):
        #for i in range(11): 
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner = Runner('Nimble')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner_1 = Runner('Walker')
        runner_2 = Runner('Nimble')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()