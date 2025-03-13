#2(a)
class Picture:
    def __init__(self,PDescription,PWidth,PHeight,PFrameColour):
        self.__PDescription = PDescription #of type string
        self.__PWidth = PWidth #of type integer
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
        self.__PDescription = desc

#2(d)
PictureArray = [Picture("",0,0,"") for i in range(100)] #1D array of type Picture with 100 elements

#2(e) 
def ReadData():
    try:
        file = open("/workspaces/school/google classroom/9618_w21_qp_41 files/Pictures.txt", 'r')
        i = 0
        while file.readline(0) !=  " ":
            Desc = file.readline()
            Width = int(file.readline())
            Height = int(file.readline())
            FrameC = file.readline()
            picture = Picture(Desc,Width,Height,FrameC)
            PictureArray[i] = picture
            i += 1
        return i + 1
    except FileNotFoundError:
        return "Sorry, file was not found!"

print(ReadData())
print(PictureArray)
