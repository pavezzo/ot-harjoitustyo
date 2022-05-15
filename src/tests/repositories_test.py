import unittest
from repositories.highscores_repository import HighscoresRepository

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.highscores_repository = HighscoresRepository(True)

    def test_repository_saves_score(self):
        self.highscores_repository.new_score(123, "testi", 4)
        self.assertEqual(len(self.highscores_repository.get_top_10()), 1)

    def test_repository_returns_in_desc_order(self):
        for i in range(1, 11):
            self.highscores_repository.new_score(i, "user"+str(i), 4)

        scores = self.highscores_repository.get_top_10()

        score = 10
        for row in scores:
            self.assertEqual(row[1], score)
            score -= 1