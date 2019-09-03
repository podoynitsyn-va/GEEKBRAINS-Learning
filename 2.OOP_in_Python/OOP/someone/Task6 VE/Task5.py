
class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part

class Sentence:
    def __init__(self, data, content):
        self.data = data
        self.content = content
    def show(self):
        output = [self.data[n].text for n in self.content]
        result = ""
        for n in output:
            result = f"{result} {n}"
        return result
    def show_parts(self):
        output = [self.data[n].part for n in self.content]
        output = set(output)
        result = ""
        for n in output:
            result = f"{result} {n}"
        return result





