import unittest
from survey import AnonymousSurvey
class TestAnonmyousSurvey(unittest.TestCase):
    # setUp 函数 在执行测试的时候会先进入setUp来创建对应的实例
    # 这样就不需要在方法中手动的创建实例
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]
        
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()