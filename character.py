from support import *

def guard(player, survial_list, guard_num, guard_target):
    printf('法官：守卫请选择自己要守护的人')
    if player[guard_num].dead == 0:
        r = random.randint(0, len(survial_list) - 1)
        while survial_list[r] == guard_target:
            r = random.randint(0, len(survial_list) - 1)
            printf('法官：不可以连续两天守同一个人！')
        guard_target = survial_list[r]
        player[guard_target].guardflag = 1
        print('%s守护了%s'%(player[guard_num].id, player[guard_target].id))
        return guard_target
def hunter(player, survival_list, hunter_num):
    printf('法官：猎人死了是否选择开枪')
    r = random.randint(0,1)
    if r == 0:
        print('%s不开枪'%(player[hunter_num].id))
    else:
        r = random.randint(0,len(survival_list) - 1)
        player[survival_list[r]].dead = 1
        print('%s开枪带走%s'%(player[hunter_num].id, player[survival_list[r]].id))
        survival_list.pop(r)
    return survival_list
#天黑请闭眼狼人请杀人
def killer(player, survival_list):
    printf("法官：天黑请闭眼狼人请杀人")
    kill_list = []
    survival_number = len(survival_list)
    for i in range(0,12):
        if (player[i].type == '狼人') and (player[i].dead == 0):
            r = random.randint(0,survival_number-1)
            target = survival_list[r]
            print('%s指刀%s'%(player[i].id, player[target].id))
            kill_list.append(target)
    kill_target = mode(kill_list)
    print('法官：狼人团体请统一意见！')
    print('狼人团体决定刀%s' % (player[kill_target].id))
    player[kill_target].killflag = 1
    return kill_target
#女巫
def witch(player, survival_list, kill_target, witch_num, healdrug, poison):
    printf('法官：女巫是否使用解药？')
    printf('法官：女巫是否使用毒药？')
    healdrug_new = healdrug
    poison_new = poison
    if player[witch_num].dead == 0:
        if healdrug == 1:
            r = random.randint(0, 1)
            if (r == 1) or (kill_target == witch_num):#判定成功和女巫自救
                print('%s选择救%s，解药消失'%(player[witch_num].id, player[kill_target].id))
                heal_target = kill_target
                player[heal_target].healflag = 1
                healdrug_new = 0
            else:
                print('女巫不救%s'%(player[kill_target].id))
        else:
            print('没有解药了')
        if poison == 1:
            r = random.randint(0, 1)
            if r == 1:
                r = random.randint(0, len(survival_list) - 1)
                if survival_list[r] == witch_num:
                    print('%s竟然想自毒！' %(player[witch_num].id))
                else:
                    poison_target = survival_list[r]
                    player[poison_target].poisonflag = 1
                    poison_new = 0
                    print('%s毒杀%s，毒药消失' % (player[witch_num].id, player[poison_target].id))
            else:
                print('女巫不毒')
        else:
            print('没有毒药了')
    return healdrug_new, poison_new