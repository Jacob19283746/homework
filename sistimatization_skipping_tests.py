import unittest


def skip_if_frozen(func):
    """Декоратор для пропуска теста, если is_frozen установлен в True."""

    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)

    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for par in self.participants:
                par.run()
            for par in self.participants[:]:
                if par.distance >= self.full_distance:
                    finishers[place] = par
                    place += 1
                    self.participants.remove(par)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print({k: str(v) for k, v in result.items()})

    @skip_if_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')

    @skip_if_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')

    @skip_if_frozen
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')

    @skip_if_frozen
    def test_distance_edge_case(self):
        tournament = Tournament(20, self.usain, self.andrey)
        result = tournament.start()
        TournamentTest.all_results[4] = result
        self.assertEqual(list(result.values())[0], 'Усэйн')
        self.assertEqual(list(result.values())[-1], 'Андрей')

    @skip_if_frozen
    def test_tie_case(self):
        custom_runner = Runner('Пользовательский', 10)
        tournament = Tournament(20, self.usain, custom_runner)
        result = tournament.start()
        TournamentTest.all_results[5] = result
        self.assertIn('Усэйн', [str(runner) for runner in result.values()])
        self.assertIn('Пользовательский', [str(runner) for runner in result.values()])


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(suite)
