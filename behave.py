from character import *

#检验胜负
def check(player):
    survival_type = []
    for i in range(0,12):
        if player[i].dead == 0:
            survival_type.append(player[i].type)
    if survival_type.count('狼人') == 0:
        printf('法官：好人胜利')
        result = 1
    elif survival_type.count('平民') == 0:
        printf('法官：平民死完，狼人胜利！')
        result = 2
    elif survival_type.count('预言家') == survival_type.count('女巫') == survival_type.count('猎人') == survival_type.count('守卫') == 0:
        printf('法官：神死完，狼人胜利！')
        result = 3
    else:
        printf('法官：游戏继续')
        result = 0
    return result


#天亮结算
def nightdead(player, suvival_list, day, hunter_num):
    if day != 1:
        printf('法官：第%d天天亮了'%(day))
    dead_list = []
    dead_num = 0
    i = 0
    while i < len(suvival_list):
        p = suvival_list[i]
        if player[p].poisonflag == 1:
            player[p].dead = player[p].dead + 5
        if player[p].healflag == player[p].guardflag == 1:
            player[p].dead = player[p].dead + 5
        if player[p].killflag == 1:
            player[p].dead = player[p].dead + 1
        if player[p].healflag == 1:
            player[p].dead = player[p].dead - 1
        if player[p].guardflag == 1:
            player[p].dead = player[p].dead - 1

        if player[p].dead > 0:
            dead_list.append(suvival_list.pop(i))#在新列表里剔除死亡的
            dead_num = dead_num + 1
        else:
            player[p].dead = 0  # 防止数据崩掉多守
            # if player[p].type == '猎人' and player[p].dead == 0:
            #     suvival_list = hunter(player, suvival_list, hunter_num)[:]#debug
            i = i + 1

    if dead_num == 0:
        printf('法官：昨天晚上是平安夜')
    elif dead_num == 1:
        printf('法官：昨天晚上%d号死亡'%(dead_list[0] + 1))
    elif dead_num == 2:
        printf('法官：昨天晚上%d号和%d号死亡' % (dead_list[0] + 1, dead_list[1] + 1))
    elif dead_num == 3:
        printf('法官：昨天晚上%d号、%d号和%d号死亡' % (dead_list[0] + 1, dead_list[1] + 1, dead_list[2] + 1))
    else:
        printf('BUG')
    if dead_list.count(hunter_num) == 1 and player[hunter_num].poisonflag == 0:
        suvival_list = hunter(player, suvival_list, hunter_num)[:]
    for i in range(0,12):#清理
        player[i].killflag = 0
        player[i].healflag = 0
        player[i].poisonflag = 0
        player[i].guardflag = 0
    return suvival_list

#投票
def vote(player, survival_list, hunter_num):
    p = survival_list
    for i in range(0,12):
        if player[i].dead == 0:
            r = random.randint(0, len(p) - 1)#r是被投位次
            if player[i].cop == 0:
                player[p[r]].vote = player[p[r]].vote + 1
            elif player[i].cop == 1:
                player[p[r]].vote = player[p[r]].vote + 1.5
            print('%s投票给了%s'%(player[i].id, player[p[r]].id))
    vote_result = []
    for i in range(0, 12):
        if player[i].dead == 0:
            print('%s得票%s票'%(player[i].id, player[i].vote))
            vote_result.append(player[i].vote)
    m = max(vote_result) #票数最大值
    vote_num = survival_list[vote_result.index(m)] #index在列表中的位置
    printf('法官：%d号玩家被%d票投出！'%(vote_num + 1, player[vote_num].vote))
    player[vote_num].dead = 1
    survival_list.pop(vote_result.index(m))
    if player[vote_num].type == '猎人':
        survival_list = hunter(player, survival_list, hunter_num)[:]
    #清洁票数
    for i in range(0, 12):
        player[i].vote = 0
    return survival_list

#上警
def oncop(player):
    oncop_list = []
    vote_list = []
    vote_result = []
    for i in range(0,12):
        if player[i].oncop == 1:
            oncop_list.append(i)#list里都是序号，身份号+1
        else:
            vote_list.append(i)
    vnum = len(vote_list)
    cnum = len(oncop_list)
    for i in range(0, vnum):
        r = random.randint(0,cnum-1)
        player[oncop_list[r]].vote = player[oncop_list[r]].vote + 1
        print('%s上票给%s'%(player[vote_list[i]].id, player[oncop_list[r]].id))
    for i in range(0, cnum):
        vote_result.append(player[oncop_list[i]].vote)#的票结果压进去
        print('%s得%d票'%(player[oncop_list[i]].id, player[oncop_list[i]].vote))

    m = max(vote_result)  # 票数最大值
    vote_num = oncop_list[vote_result.index(m)]  # index在列表中的位置,当选人编码
    printf('法官：%d号玩家得%d票，当选警长' % (vote_num + 1, player[vote_num ].vote))
    player[vote_num].cop = 1
    for i in range(0, 12):
        player[i].vote = 0 #清理票


