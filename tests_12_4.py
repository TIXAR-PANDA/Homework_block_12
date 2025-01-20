#  Домашнее задание по теме "Логирование"
"""
Цель: получить опыт использования простейшего логирования совместно с тестами.
"""

import logging
import traceback
import unittest
import runner_plus_file


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = runner_plus_file.Runner('Walker', -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError :

            logging.warning("Неверная скорость для Runner")

            logging.warning(traceback.format_exc())


    def test_run(self):
        try:
            runner = runner_plus_file.Runner( 6754 , 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning("Неверное имя для Runner")
            logging.warning(traceback.format_exc())


    def test_challenge(self):
        runner_1 = runner_plus_file.Runner('Walker')
        runner_2 = runner_plus_file.Runner('Nimble')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
        logging.info('"test_challenge" выполнен успешно')

if __name__ == '__main__':
    unittest.main()