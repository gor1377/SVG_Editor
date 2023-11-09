from bs4 import BeautifulSoup

class Xml_Editor():
    def __init__(self, file):
        self.content = []
        self.bs_content = None
        self.tag = None
        self.xml_file = file

    def create_content(self):
        with open(self.xml_file, "r") as file:
            xml_string = file.readlines()

        self.content = "".join(xml_string)

    def change_value(self, tag, atr, value):
        self.bs_content = BeautifulSoup(self.content, features="xml")
        ch_tag = self.bs_content.find(tag)
        ch_tag[atr] = value
        self.save_ch_file()

    def save_ch_file(self):
        with open(self.xml_file, 'w') as f:
            f.write(str(self.bs_content.prettify()))  # записываем в файл

file = "sq1.svg"
tag = "rect"
atr = "width"
value = "85"

chfile = Xml_Editor(file)
chfile.create_content()
chfile.change_value(tag, atr, value)


