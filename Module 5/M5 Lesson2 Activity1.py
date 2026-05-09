class IOString:

    def __init__(self):
        self.user_text = ""

    def get_String(self):
        self.user_text = input("Enter your message: ")

    def print_String(self):
        print("Uppercase result:", self.user_text.upper())

# Object creation
string_handler = IOString()

# Call functions
string_handler.get_String()
string_handler.print_String()