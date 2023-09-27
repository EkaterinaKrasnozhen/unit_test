class MoodAnalyser:
    def mood_analyser(self, msg: str) -> str:
        words = ('весело', 'грустно', 'счастлив')
        for word in words:
            if word in msg:
                return word
        return 'неизвестно'