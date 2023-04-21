import pandas as pd

def total_helix_data():
    print("total_helix_data")
    helix_alpha = pd.read_excel('./data/helix/data/total_helix.xlsx')
    helix = pd.read_excel('./data/helix/data/helix.xlsx')
    total = pd.DataFrame(columns=['код','название', 'цена закупки','цена хеликс','цена алфа'])
    y = 0
    for x, r in helix.iterrows():
        for i, row in helix_alpha.iterrows():
            if row['код'] == r['код']:
                total.loc[len(total.index)] = [r['код'], r['услуга'], row['цена helix'], row['цена alpha'], r['цена']]
                print(f'work {y}')
                y +=1
                break
            total.loc[len(total.index)] = [r['код'], r['услуга'],'1' ,'1' , r['цена']]
    return total
    # print(total.head())
    # total.to_excel('./total helix.xlsx')