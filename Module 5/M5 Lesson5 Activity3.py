class England():
    def capital(self):
        print("London is the capital of England.")

    def language(self):
        print("English is the primary language of England.")

    def type(self):
        print("England is a developed country.")

class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan.")

    def language(self):
        print("Japanese is the primary language of Japan.")

    def type(self):
        print("Japan is a developed country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_eng = England()
obj_jap = Japan()
obj_usa = USA()

for country in (obj_eng, obj_jap, obj_usa):
    country.capital()
    country.language()
    country.type()