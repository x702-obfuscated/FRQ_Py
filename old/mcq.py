import random


from helpers import *

class MCQ():

    def __init__(self, prompt, answer, *choices):
        self.prompt: str = prompt
        self.answer: str = answer
        self.choices: list[str] = list(choices)

        self.randomize()
        self.choice_map = self.gen_choice_map()

    def randomize(self) -> None:
        self.choices.insert(random.randint(0,len(self.choices)), self.answer)

    def gen_choice_map(self)-> dict[str:str]:
        
        choice_map: dict[str:str] = {}
        
        for i, e in enumerate(self.choices):
            choice_map[chr(i+65)] = e

        return choice_map
    
    def display(self, output = True) -> str:
        prompt = self.prompt + "\n"
        for key, value in self.choice_map.items():
            prompt+= (f"{key}: {value}.\n")

        if output:
            print(prompt)

        return prompt
        
    def check_answer(self) -> bool:
        response = self.choice_input()
        return self.choice_map[response] == self.answer
    
    def choice_input(self) -> str:
        length = len(self.choices)
        pattern = f"^[a-{chr(length+97)}qA-{chr(length+65)}Q]" + r"{1}$"

        user_in = check_input(
            pattern,
            self.display(False),
            f"Please type only single character from A-{chr(length+65)}",
        )


        return user_in





 





if __name__ == "__main__":
    question = MCQ(
    '''
What is the result of the following code block?

    x = 1
    y = 2

    if x == y:
        print("A")
    else:
        print("B")
    ''',
    "B",
    "A",
    "X",
    "y"
    )
    
    print(question.check_answer())
