
import sys
import unittest
from unittest.mock import patch

import test_data
from fizzbuzz.fizzbuzzer import get_question, get_answer, post_answer, crack_interview, BASE_URL


class TestResponse:
    def __init__(self, code, text):
      self.status_code = code
      self.text = text

class TestFizzBuzzer(unittest.TestCase):
  @patch('requests.get')
  def test_get_question_correct_url(self, get_mock):
    get_mock.return_value = TestResponse(200, test_data.QUESTION)
    response = get_question('/question/1')

    self.assertEqual(response, {'rules': test_data.FIZZBUZZ_RULES, 'numbers': test_data.FIZZBUZZ_NUMBERS})
    self.assertTrue(get_mock.called)

  @patch('requests.get')
  def test_get_question_incorrect_url(self, get_mock):
    get_mock.return_value = TestResponse(400, test_data.QUESTION)

    self.assertRaisesRegex(Exception, "Invalid URL", get_question, '/question/invalid')
    self.assertTrue(get_mock.called)

  def test_get_answer_fizzbuzz(self):
    answer = get_answer(test_data.FIZZBUZZ_RULES, test_data.FIZZBUZZ_NUMBERS)
    self.assertEqual(answer, test_data.FIZZBUZZ_SOLUTION)

  def test_get_answer_beepboop(self):
    answer = get_answer(test_data.BEEPBOOP_RULES, test_data.BEEPBOOP_NUMBERS)
    self.assertEqual(answer, test_data.BEEPBOOP_SOLUTION)

  def test_get_answer_meetthenoops(self):
    answer = get_answer(test_data.MEETTHENOOPS_RULES, test_data.MEETTHENOOPS_NUMBERS)
    self.assertEqual(answer, test_data.MEETTHENOOPS_SOLUTION)

  @patch('requests.post')
  def test_post_answer_correct_response(self, post_mock):
    post_mock.return_value = TestResponse(200, test_data.ANSWER_RESPONSE)

    response = post_answer('/question/1', 'A good response')
    self.assertEqual(response, test_data.NEXT_QUESTION)
    self.assertTrue(post_mock.called)

  @patch('requests.post')
  def test_post_answer_incorrect_response(self, post_mock):
    post_mock.return_value = TestResponse(400, test_data.ANSWER_BAD_RESPONSE)

    self.assertRaisesRegex(Exception, "Incorrect answer sent", post_answer, '/question/1', 'A bad response :(')
    self.assertTrue(post_mock.called)

  @patch('requests.post')
  def test_post_answer_missing_next_data(self, post_mock):
    post_mock.return_value = TestResponse(200, test_data.ANSWER_BAD_RESPONSE)

    self.assertRaisesRegex(Exception, "Response did not have next question nor grade", post_answer, '/question/1', 'Response is incomplete')
    self.assertTrue(post_mock.called)

  @patch('requests.get')
  @patch('requests.post')
  def test_crack_interview(self, post_mock, get_mock):
    def side_effect(url, json):
      if url == BASE_URL + test_data.FINAL_QUESTION:
        return TestResponse(200, test_data.FINAL_RESPONSE)
      elif url == BASE_URL + test_data.INITIAL_ENDPOINT:
        return TestResponse(200, test_data.ANSWER_RESPONSE)
      else:
        return TestResponse(200, test_data.ANSWER_RESPONSE_2)

    get_mock.return_value = TestResponse(200, test_data.QUESTION)
    post_mock.side_effect = side_effect

    result = crack_interview('/questions/1', 'Python')
    self.assertEqual(result['grade'], 'A+')


if __name__ == '__main__':
  unittest.main()