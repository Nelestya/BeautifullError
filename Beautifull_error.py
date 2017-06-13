
MSG_ERROR = "ERROR"



class Beautifull_Error():
    def __init__(self, errorName="ERROR", errorDescription=None, width=60):

        Begin_MSG_ERROR = str().center(width, "*")
        End_MSG_ERROR = str().center(width, '*')
        self.width = width
        self.errorName = errorName
        self.errorDescription = errorDescription
        print(Begin_MSG_ERROR)
        print('*' + MSG_ERROR.center(width - 2, ' ') + '*')
        print(End_MSG_ERROR)
        self.bloc()

    def cutDescription(self):
        """cut the decription for work this"""
        self.Description = []
        while len(self.errorDescription) > self.width / 2 - 2:
            self.Description.append(self.errorDescription[0:int(self.width/2)])
            self.errorDescription = self.errorDescription[int(self.width/2):]

        return self.Description

    def bloc(self):
        "Création du bloc"
        try:
            self.cutDescription()
            self.x = 0
            for desc in self.Description:
                if self.x != 1:
                    print("|" + self.errorName.center(int(self.width / 2 - 2), " ") +
                          "|" + desc.center(int(self.width / 2 - 2), " ") + "|")
                    self.x = 1
                print("|" + " ".center(int(self.width / 2 - 2), " ") +
                      "|" + desc.center(int(self.width / 2 - 2), " ") + "|")
        except Exception as e:
            raise


if __name__ == '__main__':
    err = Beautifull_Error(
        "error", "nudfvgghghdhdhghgihuigheigrhgiehgiuehrugiherghierghierhgireghreiugherihgirehgihegiuehiugerhighreghreghreghreiughrehgirehgrehgrehgureihgiorhgrhgihghrhihbbh")
