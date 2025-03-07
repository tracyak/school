#2(a)
class Picture:
    def __init__(self,PDescription,PWidth,PHeight,PFrameColour):
        self.__PDescription == PDescription #of type string
        self.__PWidth == PWidth #of type integer
        self.__PHeight = PHeight #of type integer
        self.__PFrameColour = PFrameColour #of type string
#2(b)
    def GetDescription(self):
        return self.__PDescription
    def GetWidth(self):
        return self.__PWidth
    def GetHeight(self):
        return self.__PHeight
    def GetFrameColour(self):
        return self.__PFrameColour
#2(c)
    def SetDecription(self,desc):
        self.PDescription = desc

#2(d)
PictureArray = [Picture("",0,0,"") for i in range(100)] #1D array of type Picture with 100 elements

#2(e) 



