# Примените подход TDD для создания нового класса MoodAnalyser, который оценивает настроение
# выраженное во фразах.

import unittest
from mood_analyser import MoodAnalyser


class TestMoodAnalyser(unittest.TestCase):    
    def tes_fun(self):
        self.analyser = MoodAnalyser()
        self.assertEqual(self.analyser.mood_analyser('Мне весело'), 'весело')
        
    def test_sad(self):
        self.analyser = MoodAnalyser()
        self.assertEqual(self.analyser.mood_analyser('Мне грустно'), 'грустно')
        
    def test_happy(self):
        self.analyser = MoodAnalyser()
        self.assertEqual(self.analyser.mood_analyser('я счастлив'), 'счастлив')
        
    def test_none(self):
        self.analyser = MoodAnalyser()
        self.assertEqual(self.analyser.mood_analyser('qwerasdf'), 'неизвестно')
        
        
if __name__ == '__main__':
    unittest.main()