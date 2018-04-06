class Witness(object):
    def __init__(self,name,killer,place,around):
        """
        Creates a witness (possibly, a killer)
        killer: If it's the killer or not (only one can exist)
        place: The place where he stood during the crime
        around: Which people was around ythe witness
        """
        self.name = name
        self.killer = killer
        self.room = place
        self.around = set(around)
    def answerName(self):
        return "My name is " % self.name
    def answerWorkpace(self):
        return "I'm... rich"
    def answerPlace(self):
        return "I was in the %s" % self.room
    def answerWho(self):
        if len(self.around) == 0:
            return "I was alone"
        else:
            return "I was with: %s" % (",".join(map(lambda x: x.name,self.around)))