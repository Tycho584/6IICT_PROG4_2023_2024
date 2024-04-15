from Levenshtein import distance


class MlChatbot:
    def __init__(self, name):
        self.name = name
        self.conversatie = {}

    def train(self, conversatie):
        self.conversatie = conversatie

    def zoek_antwoord(self, vraag):
        if self.conversatie == {}:
            return f"{self.name} zegt: train, mij eerst!!!"

        vraag = vraag.lower()
        laagste_score, beste_antwoord = 1, ""

        for gekende_vraag, antwoord in self.conversatie.items():
            huidige_score = distance(vraag, gekende_vraag.lower()) / max(len(gekende_vraag), len(vraag))
            if huidige_score < laagste_score:
                laagste_score, beste_antwoord = huidige_score, antwoord

        return f"{self.name} zegt: {beste_antwoord}"

    def vraag_reeks(self):
        print("Zeg 'stop' om de conversatie te stoppen.")

        while True:
            user_input = input(f"Vraag iets aan {self.name}: ")
            if user_input.lower() == "stop":
                break

            bot_response = self.zoek_antwoord(user_input)
            print(bot_response)

if __name__ == "__main__":
    bot = MlChatbot("Marvin")
    print(bot.zoek_antwoord("Test"))
