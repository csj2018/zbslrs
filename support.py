import random
class Player:
    def __init__(self, number, type, oncop):
        self.number = number
        self.type = type
        self.oncop = oncop
        self.cop = 0
        self.dead = 0
        self.vote = 0
        self.killflag = 0
        self.healflag = 0
        self.poisonflag = 0
        self.guardflag = 0
        self.id = ''

    def show(self):#
        print('%d号玩家是%s！'%(self.number, self.type))

def mode(list):
    c = []
    length = len(list)
    for i in range(0,length):
        c.append(list.count(list[i]))
    m = max(c)
    n = c.index(m)
    result = list[n]
    return result

#法官说话专用
def printf(words):
    print('*' * 50)
    print('\033[1;40;32m%s'%(words))  # 字体颜色红色反白处理
    print('\033[0m*' * 50)

def state(player):
    w = []
    p = []
    y = []
    n = []
    l = []
    s = []
    ww = ''
    pp = ''
    for i in range(0, 12):
        if player[i].dead == 0:
            if player[i].type == '狼人':
                w.append(i + 1)
            if player[i].type == '平民':
                p.append(i + 1)
            if player[i].type == '预言家':
                y.append(i + 1)
            if player[i].type == '女巫':
                n.append(i + 1)
            if player[i].type == '猎人':
                l.append(i + 1)
            if player[i].type == '守卫':
                s.append(i + 1)
    for i in range(0, len(w)):
        ww = ww + '[' + str(w[i]) + ']号 '
    for i in range(0, len(p)):
        pp = pp + '[' + str(p[i]) + ']号 '
    print('现在场上的情况：')
    print('狼人：%s'%(ww))
    print('平民：%s' % (pp))
    print('预言家：%s号'%(y))
    print('女巫：%s号' % (n))
    print('猎人：%s号' % (l))
    print('守卫：%s号' % (s))


