# Домашнее задание по теме "Систематизация и пропуск тестов".
"""
Цель: понять на практике как объединять тесты при помощи TestSuite.
Научиться пропускать тесты при помощи встроенных в unittest декораторов.
"""
import unittest
from module_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    #is_frozen = True
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('Walker')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('Nimble')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = Runner('Den')
        runner_2 = Runner('Max')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    #is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.ran_1 = Runner('Усэйн', 10)
        self.ran_2 = Runner('Андрей', 9)
        self.ran_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f'test: {i}')
            for key, value in j.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_1(self, num=1):
        tournament = Tournament(90, self.ran_1, self.ran_3)
        all_results = tournament.start()
        self.assertTrue(all_results[2] == self.ran_3.name)
        self.all_results[num] = all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_2(self, num=2):
        tournament = Tournament(90, self.ran_2, self.ran_3)
        all_results = tournament.start()
        self.assertTrue(all_results[2] == self.ran_3.name)
        self.all_results[num] = all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_3(self, num=3):
        tournament = Tournament(90, self.ran_1, self.ran_2, self.ran_3)
        all_results = tournament.start()
        self.assertTrue(all_results[3] == self.ran_3.name)
        self.all_results[num] = all_results


if __name__ == "__main__":
    unittest.main()