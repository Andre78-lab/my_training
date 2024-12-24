from pprint import pprint

from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    # создаётся атрибут класса all_results, который будут сохраняться результаты всех тестов
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    # в конце всех методов выводятся all_results по очереди в столбец
    @classmethod
    def tearDownClass(cls):
        for i  in range(1, len(cls.all_results)+1):
            print(cls.all_results[i])

    # создаем 3 объекта класса Runner
    def setUp(self):
        self.run_usen = Runner("Усэйн", 10)
        self.run_adnre = Runner("Андрей", 9)
        self.run_nik = Runner("Ник", 3)


    def testRace_usen_nik(self):
        # Создаем класс Tournament - соревнований
        tournament = Tournament(90, self.run_usen, self.run_nik)
        # Запускаем метод start
        result = tournament.start()
        # Записываем результат в all_results
        self.all_results[1] = result
        # сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна
        self.assertTrue(result[max(result.keys())] == "Ник")

    def testRace_andre_nik(self):
        tournament = Tournament(90, self.run_adnre, self.run_nik)
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def testRace_andre_usen_nik(self):
        tournament = Tournament(90, self.run_adnre, self.run_usen, self.run_nik)
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_test(self):
        tournament = Tournament(90, self.run_nik, self.run_usen, self.run_adnre)
        result = tournament.start()
        dist_= {1:self.run_usen.name, 2: self.run_adnre.name, 3: self.run_nik.name}
        self.assertDictEqual(result, dist_)



if __name__ == "__main__":
    unittest.main



