def calc_v(height:list)->int:
    """Возвращает заполняемый объем"""

    #убираем максимум одиночку и присваиваем ему значение второго максимума
    if height.count(max(height))==1:
        height[height.index(max(height))]=sorted(height)[-2]

    #производим рассчет объема
    max_height = 0
    ind_max_heigh=0
    vol=0
    for ind,val in enumerate(height):

        if val>=max_height:
            if max_height!=0:
                if (ind-ind_max_heigh)>1:
                    for i in range(ind_max_heigh,ind):
                        vol+=max_height-height[i]
            ind_max_heigh=ind
            max_height=val
    return vol