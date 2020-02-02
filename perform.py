from behave import *

#主函数
def perform(imax):
    result =[]
    for j in range(0,imax):
        survival_list = []#本版里面都装序号
        player = []
        day = 1
        healdrug = 1
        poison = 1
        guard_target = 13
        card = ['平民','平民','平民','平民','狼人','狼人','狼人','狼人','预言家','女巫','猎人','守卫']
        for i in range(0,12): #这里是一个左闭右开:
            r = random.randint(0, 11-i)
            r_oncop = random.randint(0,1)#这里是一个闭区间
            player.append(Player(i + 1, card.pop(r), r_oncop))#向player列表添加元素编号、类型、上警
            survival_list.append(i)
            # player[i].show()
            if player[i].type == '女巫':
                witch_num = i
            elif player[i].type == '守卫':
                guard_num = i
            elif player[i].type == '猎人':
                hunter_num = i

            player[i].id = str(i + 1) + '号玩家（' + player[i].type + '）'#称号编号

        state(player)#厂商情况
        for i in range(0,6):
            #入夜狼人杀人
            kill_target = killer(player, survival_list)
            #女巫
            witch_result = witch(player, survival_list, kill_target, witch_num, healdrug, poison)
            healdrug = witch_result[0]
            poison = witch_result[1]
            #猎人
            #守卫守人
            guard_target = guard(player, survival_list, guard_num, guard_target)
            #上警
            if day == 1:
                printf('法官：第1天天亮了，现在开始竞选警长！')
                oncop(player)

            #夜里情况结算
            survival_list = nightdead(player, survival_list, day, hunter_num)
            resulto = check(player)
            state(player)
            if resulto != 0:
                break
            #白天投票
            survival_list = vote(player, survival_list, hunter_num)
            resulto = check(player)
            if resulto != 0:
                break
            #一天结束
            day = day + 1
        result.append(resulto)
    return result