from enum import Enum

#定义权值表
def key_value():
    class TupleType(Enum):
        # tuple is empty
        Blank = 0
        # tuple contains a black chess
        B = 1
        # tuple contains two black chesses
        BB = 2
        # tuple contains three black chesses
        BBB = 3
        # tuple contains four black chesses
        BBBB = 4
        # tuple contains a white chess
        W = 5
        # tuple contains two white chesses
        WW = 6 
        # tuple contains three white chesses 
        WWW = 7 
        # tuple contains four white chesses 
        WWWW = 8 
        # tuple does not exist 
        Virtual = 9 
        # tuple contains at least one black and at least one white 
        Polluted = 10

    tupleScoreTable = [0] * len(TupleType)
    tupleScoreTable[TupleType.Blank.value] = 7;
    tupleScoreTable[TupleType.B.value] = 35;
    tupleScoreTable[TupleType.BB.value] = 800;
    tupleScoreTable[TupleType.BBB.value] = 15000;
    tupleScoreTable[TupleType.BBBB.value] = 800000;
    tupleScoreTable[TupleType.W.value] =15;
    tupleScoreTable[TupleType.WW.value] =400;
    tupleScoreTable[TupleType.WWW.value]=1800;
    tupleScoreTable[TupleType.WWWW.value]=100000;
    tupleScoreTable[TupleType.Virtual.value]=0;
    tupleScoreTable[TupleType.Polluted.value]=0;

    return tupleScoreTable

tupleScoreTable = key_value()#权值表


initChessList = []          #保存的是棋盘坐标
initRole = 1                #1：代表白棋； 2：代表黑棋
resultFlag = 0              #结果标志

class StornPoint():
    def __init__(self,x,y,value):
        '''
        :param x: 代表x轴坐标
        :param y: 代表y轴坐标
        :param value: 当前坐标点的棋子：0:没有棋子 1:白子 2:黑子
        '''
        self.x = x            #初始化成员变量
        self.y = y
        self.value = value

def initChessSquare(x,y):     #初始化棋盘
    for i in range(15):       # 每一行的交叉点坐标
        rowlist = []
        for j in range(15):   # 每一列的交叉点坐标
            pointX = x+ j*40
            pointY = y+ i*40
            sp = StornPoint(pointX,pointY,0)
            rowlist.append(sp)
        initChessList.append(rowlist)

