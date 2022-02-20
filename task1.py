def calc_v(height: list, vol=0) -> int:
    """Возвращает заполняемый объем"""

    # убираем максимум одиночку и присваиваем ему значение второго максимума

    if len(height) > 1:
        if height.count(max(height)) == 1:
            height[height.index(max(height))] = sorted(height)[-2]
    else:
        return vol
    # производим рассчет объема
    max_height = 0
    ind_max_heigh = 0

    for ind, val in enumerate(height):

        if val >= max_height:

            if (ind - ind_max_heigh) > 1:
                for i in range(ind_max_heigh, ind):
                    vol += max_height - height[i]
                return calc_v(height[ind:], vol=vol)
            else:
                ind_max_heigh = ind
                max_height = val
    return vol
my_list=[0,1,0,2,1,0,1,3,2,1,2,1]
print(calc_v(my_list))
