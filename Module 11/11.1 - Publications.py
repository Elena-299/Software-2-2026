class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print("Book information:")
        print(f"-name: {self.name}\n"
              f"-author: {self.author}\n"
              f"-page count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print("Magazine information:")
        print(f"-name: {self.name}\n"
              f"-chief editor: {self.chief_editor}\n")

publication1 = Book("Compartment No. 6", "Rosa Liksom", 192)
publication2 = Magazine("Donald Duck", "Aki Hyyppä")

publication1.print_information()
publication2.print_information()

