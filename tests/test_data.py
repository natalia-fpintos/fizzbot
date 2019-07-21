### Puzzles
# FizzBuzz
FIZZBUZZ_RULES = [{"number": 3, "response": "Fizz"}, {"number": 5, "response": "Buzz"}]
FIZZBUZZ_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
FIZZBUZZ_SOLUTION = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"

# BeepBoop
BEEPBOOP_RULES = [{"number": 2, "response": "Beep"}, {"number": 5, "response": "Boop"}]
BEEPBOOP_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BEEPBOOP_SOLUTION = "1 Beep 3 Beep Boop Beep 7 Beep 9 BeepBoop"

# MeetTheNoops
MEETTHENOOPS_RULES = [{"number": 3, "response": "Meet"}, {"number": 5, "response": "The"}, {"number": 7, "response": "Noops"}]
MEETTHENOOPS_NUMBERS = [95, 58, 94, 85, 26, 56, 24, 71, 91, 21, 105]
MEETTHENOOPS_SOLUTION = "The 58 94 The 26 Noops Meet 71 Noops MeetNoops MeetTheNoops"

### Get Question
QUESTION = """{{
  "message": "This is a test game!",
  "rules": {rules},
  "numbers": {numbers},
  "exampleResponse": {{"answer": "A good response"}}
}}""".format(rules=FIZZBUZZ_RULES, numbers=FIZZBUZZ_NUMBERS)
PARTIAL_QUESTION = '{"message": "This is a test game!"}'

### Post Answer
# Final response
FINAL_QUESTION = '/question/aMeetTheNoopsQ'
ELAPSED_SECONDS = 15
FINAL_RESPONSE = """{{
  "result": "You finished!",
  "message": "Nicely done",
  "elapsedSeconds": "{seconds}",
  "grade": "{grade}"
}}""".format(seconds=ELAPSED_SECONDS, grade='A+')

# Bad response
ANSWER_BAD_RESPONSE = """{
  "result": "This answer is incomplete!",
  "message": "Test"
}"""

# Second response
NEXT_QUESTION = '/question/aFizzBuzzQ'
ANSWER_RESPONSE_2 = """{{
  "result": "Nice!",
  "message": "Almost there",
  "nextQuestion": "{endpoint}"
}}""".format(endpoint=FINAL_QUESTION)

# Initial response
INITIAL_ENDPOINT = '/questions/1'
ANSWER_RESPONSE = """{{
  "result": "You are doing great!",
  "message": "Best solution ever",
  "nextQuestion": "{endpoint}"
}}""".format(endpoint=NEXT_QUESTION)
