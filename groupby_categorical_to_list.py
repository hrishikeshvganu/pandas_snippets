player_group_loc=match_stats[['pid','loc']].groupby('pid')

from collections import Counter
def counts_values(list1):
    c = Counter(list1)
    return list(c.items())
    
players_tmp=player_group_loc['loc'].apply(list).map(counts_values)    
players_grouped['home']=(
    list(players_tmp
.map(lambda x: x[0][1] if len(x)>0 else 0)
     )
    )
players_grouped['away']=(
    list(players_tmp
.map(lambda x: x[1][1] if len(x)>1 else 0)
     )
    )
players_grouped.head() 
