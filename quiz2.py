

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Who is the father of Genetics?\n(a) Gregor Mendel? \n(b)SteveJobs\n(c)Michael Jackson",
     "Who invented Telephone?\n(a) Bill Gates\n(b)Graham Bell\n(c)MelGibson",
     "What is the capital of USA?\n(a) Washington?\n(b)New Jersey\n(c)NewYork"
] 

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               more=input("want to play more? press y to continue and n to exit")
               if more=="y":
                   continue
               else:
                   print("you got", score, "out of", len(questions))
               exit()
run_quiz(questions)
