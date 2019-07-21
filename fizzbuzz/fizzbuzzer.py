import ast
import pprint
import requests

BASE_URL = 'https://api.noopschallenge.com'

def get_question(endpoint):
  """Performs a GET request to an endpoint of noopschallenge to get back a question. 
  Returns the relevant data to resolve the question: its rules and example data (numbers)."""

  response = requests.get(BASE_URL + endpoint)

  if response.status_code == 200:
    try:
      json_resp = ast.literal_eval(response.text)
      return {"rules": json_resp['rules'], "numbers": json_resp['numbers']}
    except Exception as e:
      raise Exception('Could not get next question: {}'.format(e))
  
  raise Exception('Invalid URL: {}'.format(BASE_URL + endpoint))


def get_answer(rules, data):
  def apply_rules(number):
    translation = ''
    for rule in rules:
      if number % rule['number'] == 0:
        translation += rule['response']
    
    if translation == '':
      translation = str(number)
    
    return translation

  translated = [apply_rules(i) for i in data]
  return ' '.join(translated)


def post_answer(endpoint, answer):
  """Performs a POST request to an endpoint of noopschallenge, with a json payload to answer a question. 
  Returns an endpoint for the next question or raises an exception if the answer was incorrect."""

  body = {"answer": answer}
  response = requests.post(BASE_URL + endpoint, json=body)

  if response.status_code == 200:
    try:
      text = ast.literal_eval(response.text)
      if 'nextQuestion' in text:
        return text['nextQuestion']
      if 'grade' in text:
        return text
    except Exception as e:
      raise Exception('Error accessing response data: {}'.format(e))
    else:
      raise Exception('Response did not have next question nor grade')
  
  raise Exception('Incorrect answer sent: {}'.format(body))

def _get_question_post_answer(url):
  question = get_question(url)
  answer = get_answer(question['rules'], question['numbers'])
  result = post_answer(url, answer)
  return result

def crack_interview(first_url, answer):
  question_url = post_answer(first_url, answer)
  test_running = True
  result = question_url

  while test_running:
    if 'grade' in result:
      test_running = False
    else:
      result = _get_question_post_answer(result)
  
  return result


if __name__ == "__main__":
  grade = crack_interview('/fizzbot/questions/1', 'Python')
  pprint.pprint(grade)
