

class Beautifull_Error():
    def __init__(self, typeError="ERROR!!", errorName="ERROR", errorDescription=None, width=60):
        # Variables
        Begin_MSG_ERROR = str().center(width, "*")
        End_MSG_ERROR = str().center(width, '*')
        self.width = width
        self.errorName = errorName
        self.errorDescription = errorDescription
        # MESSAGES
        print(Begin_MSG_ERROR)
        print('*' + typeError.center(width - 2, ' ') + '*')
        print(End_MSG_ERROR)
        print(str().center(width + 1, '_'))
        # Function Appel
        self.bloc()
        print(str().center(width + 1, '_') + "\n")

    def cutDescription(self):
        """cut the decription for work this"""

        try:
            if len(self.errorDescription) > self.width / 2 - 2:
                # while len(self.errorDescription) > self.width / 2 - 2:
                self.Description.append(self.errorDescription[0:int(self.width / 2)])
                self.errorDescription = self.errorDescription[int(self.width / 2):]
                self.cutDescription()
            else:

                self.Description.append(self.errorDescription)
        except:
            self.Description = []
            self.cutDescription()

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
                else:
                    print("|" + " ".center(int(self.width / 2 - 2), " ") +
                          "|" + desc.center(int(self.width / 2), " ") + "|")
        except Exception as e:
            raise


################################################################################
# TEST PHASE
if __name__ == '__main__':
    err = Beautifull_Error(
        "error", "lol", "short desc")
    err = Beautifull_Error(
        "error", "lol", "LONNNNNNNNNG DESCRIPTION!!!!!!!!!!!!!")
