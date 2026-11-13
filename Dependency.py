class Printer:
    def print_text(self, text):
        print(f"Printing: {text}")

class Document:
    def __init__(self, content):
        self.content = content

    def send_to_printer(self, printer):
        printer.print_text(self.content)

doc = Document("Quarterly Report")
office_printer = Printer()