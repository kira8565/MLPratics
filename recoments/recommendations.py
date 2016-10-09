from math import sqrt

critics = {
    'Lisa Rose':
        {
            'Lady in the Water': 2.5,
            'Snakes on a Plane': 3.5,
            'Just My Luck': 3.0,
            'Superman Returns': 3.5,
            'You,Me and Dupree': 2.5,
            'The Night Listener': 3.0
        },
    'Gene Seymour':
        {
            'Lady in the Water': 3.0,
            'Snakes on a Plane': 3.5,
            'Just My Luck': 1.5,
            'Superman Returns': 5.0,
            'You,Me and Dupree': 3.0,
            'The Night Listener': 3.5
        },
    'Michael Phillips':
        {
            'Lady in the Water': 2.5,
            'Snakes on a Plane': 3.0,
            'Superman Returns': 3.5,
            'The Night Listener': 4.0
        },
    'Claudia Puig':
        {
            'Snakes on a Plane': 3.0,
            'Just My Luck': 3.0,
            'Superman Returns': 4.0,
            'You,Me and Dupree': 2.5,
            'The Night Listener': 4.5
        },
    'Mick Lasalle':
        {
            'Lady in the Water': 3.0,
            'Snakes on a Plane': 4.0,
            'Just My Luck': 2.0,
            'Superman Returns': 3.0,
            'You,Me and Dupree': 2.0,
            'The Night Listener': 3.0
        },
    'Jack Matthews':
        {
            'Lady in the Water': 3.0,
            'Snakes on a Plane': 4.0,
            'Just My Luck': 2.0,
            'Superman Returns': 3.0,
            'You,Me and Dupree': 2.0,
            'The Night Listener': 3.0
        },
    'Toby':
        {
            'Snakes on a Plane': 4.5,
            'Superman Returns': 4.0,
            'You,Me and Dupree': 4.0,
        }
}

#打分
# def topMatches(prefs,person,n=5,similarity=sim_distance()):


# 皮尔逊相关系数

def sim_pearson(prefs, person1, person2):
    si = {}

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])

    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

    num = pSum - (sum1 * sum2 / len(si))
    den = sqrt((sum1Sq - pow(sum1, 2) / len(si)) * (sum2Sq - pow(sum2, 2 / len(si))))

    if den == 0:
        return 0

    r = num / den

    return r


# 欧几里何距离
def sim_distance(prefs, person1, person2):
    si = {}

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sqrt(sum_of_squares))
