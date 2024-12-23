from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Проверка методы walk класса Runner"""
        runner_walk = Runner("Myname_walk")
        for i in range(11):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 55)

    def test_run(self):
        """Проверка методы run класса Runner"""
        runner_run = Runner("Myname_run")
        for i in range(11):
            runner_run.run()
        self.assertEqual(runner_run.distance, 110)

    def test_challenge(self):
        """Сравнение результатов после методов walk и run класса Runner"""
        run_1 = Runner("Myname_run1")
        run_2 = Runner("Myname_run2")
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1, run_2, "Тест провален")


if __name__ == "__main__":
    unittest.main