class mattbot():
    
    def __init__(self):
        self.response="The command is not recognized."
        
    def message(self, string):
        if (string[2:]=="about"):
            self.response = "Hello, I am MattBot, your translation assistant. I do make translations and jokes. type !!help for more."
        elif (string[2:]=="help"):
            self.response = "Type !!funtranslate with a sentence for a fun translation, !!joke for a joke."
        elif (string[2:]=="joke"):
            self.response = "why dont you see elephants hiding in trees? Because theyre good at it."
        elif (string[2:14]=="funtranslate"):
            translation = ""
            self.response = translation
        else:
            self.response = "The command is not recognized."
        return self.response