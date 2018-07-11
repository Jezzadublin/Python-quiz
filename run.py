
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is the smallest county in Ireland?\n(a) County Leitrim\n(b)County Louth\n(c)County Dublin\n(d)County Clare\n",
     "Where in the world could you visit the cities of Monterrey, Puebla, and Toluca?\n(a) Peru\n(b)Chile\n(c)Argentina\n(d)Mexico\n",
     "Who directed the following films; The Color Purple, Schindler’s List, and Jurassic Park?\n(a)Oliver Stone\n(b)Stephen Spielberg\n(c)Quentin Tarantino\n(d)Ridley Scott\n",
     "Kiss Me Kate is a musical version of which William Shakespeare’s work?\n(a)Much Ado About Nothing\n(b)The Merchant of Venice\n(c)The Taming of The Shrew\n(d)Hamlet\n",
     "In The Simpsons, what is the name of Homer’s youngest daughter?\n(a)Marge\n(b)Maggie\n(c)Lisa\n(d)Molly\n"
]

questions = [
     Question(question_prompts[0], "b"),
     Question(question_prompts[1], "d"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "b"),
     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got ", str(score),"/", str(len(questions)), "correct")
 
run_quiz(questions)



