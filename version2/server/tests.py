import unittest
from recommender_engine import RecommenderEngine
from cosine_similarity import CosineSimilarity

class EngineTests(unittest.TestCase):

    def test_cosine_similarity_same(self):
        text1 = "happy birthday"
        text2 = "happy birthday"
        cs = CosineSimilarity.cosine_similarity_of(text1, text2)

        #strings used due to floating number problem.
        self.assertEqual("%.2f" % cs, "1.00")

    def test_cosine_similarity_different(self):
        text1 = "hello sir"
        text2 = "good afternoon"
        cs = CosineSimilarity.cosine_similarity_of(text1, text2)

        #strings used due to floating number problem.
        self.assertEqual("%.2f" % cs, "0.00")

    def test_cosine_similarity_some(self):
        text1 = "apple banana orange"
        text2 = "orange berry ananas"
        cs = CosineSimilarity.cosine_similarity_of(text1, text2)

        self.assertEqual("%.2f" % cs, "0.33")

if __name__ == '__main__':
    unittest.main()
