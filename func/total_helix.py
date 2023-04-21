import pandas as pd

def total_helix(helix,shablon):
    # helix = pd.read_excel('./data/helix/data/total_helix.xlsx')
    # shablon = pd.read_excel('./data/helix/data/shablon.xlsx')
    print("total_helix")
    total_helix = pd.DataFrame(columns=['наименование','цена закупки helix' , 'стоимость helix','стоимость alpha','код helix','код invitro', 'код eml'])
    print(helix.columns.tolist())
    # 'код','название', 'цена закупки','цена хеликс','цена алфа'
    for i, row in shablon.iterrows():
        for y, r in helix.iterrows():
                if str(row['код helix']) == str(r['код']):
                    total_helix.loc[len(total_helix.index)]= [row['тест'],r['цена закупки helix'], r['цена helix'],r['цена альфа'],row['код helix'],row['код invitro'], row['код eml']]
                    break
        else:
            total_helix.loc[len(total_helix.index)] = [row['тест'],'1', '1','1',row['код helix'], row['код invitro'], row['код eml']]

    print(total_helix.head())
    return total_helix

