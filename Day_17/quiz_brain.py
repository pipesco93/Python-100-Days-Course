class QuizBrain:

    def __init__(self, q_list) -> None: #These are attribute
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        #if self.question_number < len(self.question_list):
        #    return True
        #else:
        #    False
            # Lo anterioro es lo mismo que
        return self.question_number < len(self.question_list)


    def next_question(self): #This is a method
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your curret score is: {self.score}/{self.question_number}")
        print("\n")


