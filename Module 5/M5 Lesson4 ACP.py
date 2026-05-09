class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_words(self):
        
        words = self.s.split()
        reversed_list = words[::-1]
        return " ".join(reversed_list)

user_input = input("Enter a sentence to reverse: ")

string_reverser = Reverse(user_input)

print("Reversed string:", string_reverser.reverse_words())