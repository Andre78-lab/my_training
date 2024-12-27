from rt_with_exceptions import Runner, Tournament
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Проверка методы walk класса Runner"""
        try:
            runner_walk = Runner("Myname_walk", -3)
            for i in range(11):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 55)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """Проверка методы run класса Runner"""
        try:
            runner_run = Runner(4)
            for i in range(11):
                runner_run.run()
            self.assertEqual(runner_run.distance, 110)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Сравнение результатов после методов walk и run класса Runner"""
        run_1 = Runner("Myname_run1")
        run_2 = Runner("Myname_run2")
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1, run_2, "Тест провален")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
    

