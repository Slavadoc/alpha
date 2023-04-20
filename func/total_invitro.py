import pandas as pd


def total_invitro(invitro,total_helix):
    print("total_invitro")
    total_invitro = pd.DataFrame(columns=['наименование', 'закупка helix','стоимость helix','цена alpha', 'закупка invitro', 'стоимость invitro','стоимость alpha','код helix', 'код invitro', 'код eml'])
    # 'код','услуга', 'цена закупки invitro','цена invitro','цена альфа'
    #  # 'наименование','цена закупки helix' , 'стоимость helix','стоимость alpha','код helix','код invitro', 'код eml'
    for i,row in total_helix.iterrows():
        for y,r in invitro.iterrows():
            if str(row['код invitro']) == str(r['код']):
                total_invitro.loc[len(total_invitro.index)] = [row['наименование'], row['цена закупки helix'], row['стоимость helix'],row['стоимость alpha'], r['цена закупки invitro'],r['цена invitro'],r['цена альфа'],row['код helix'],row['код invitro'],row['код eml']]
                break
        else:
            total_invitro.loc[len(total_invitro.index)] = [row['наименование'],  row['цена закупки helix'], row['стоимость helix'],row['стоимость alpha'], '1', '1', '1',  row['код helix'],row['код invitro'],row['код eml']]

    # for i,row in total_helix.iterrows():
    #     for y,r in invitro.iterrows():
    #         if str(row['Код Invitro']) == str(r['код']):
    #             total_invitro.loc[len(total_invitro.index)] = [row['Наименование'],row['Стоимость Helix'],row['Стоимость Alpha'],r['цена интвитро'],r['цена альфа'],row['код eml']]
    #             break
    #     else:
    #         total_invitro.loc[len(total_invitro.index)] = [row['Наименование'], row['Стоимость Helix'], row['Стоимость Alpha'], '1', '1', row['код eml']]

    print(total_invitro.head())
    return total_invitro
