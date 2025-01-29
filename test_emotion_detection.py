import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_1(self):
        test = emotion_detector("I am glad this happened")
        self.assertEqual(test["dominant_emotion"], "joy")

    def test_2(self):
        test = emotion_detector("I am really mad about this")
        self.assertEqual(test["dominant_emotion"], "anger")

    def test_3(self):
        test = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test["dominant_emotion"], "disgust")

    def test_4(self):
        test = emotion_detector("I am so sad about this")
        self.assertEqual(test["dominant_emotion"], "sadness")

    def test_5(self):
        test = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test["dominant_emotion"], "fear")

unittest.main()