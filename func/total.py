import pandas as pd

def total(eml, total_invitro):
    print(" work total")
    print(eml.columns.tolist())
    total = pd.DataFrame(columns=['наименование', 'закупка helix' , 'стоимость helix', 'цена alpha', '' ,'закупка invitro','стоимость invitro','стоимость alpha', '', 'закупка EML','стоимость EML', 'стоимость EML',  '' ,  'код helix', 'код invitro', 'код eml'])
    for i, row in total_invitro.iterrows():
        for y, r in eml.iterrows():
            if str(row['код eml']) == str(r['код']):
                total.loc[len(total.index)] = [row['наименование'], row['закупка helix'] , row['стоимость helix'], row['цена alpha'],'' ,row['закупка invitro'], row['стоимость invitro'] , row['стоимость alpha'], '', r['цена закупки eml'],r['цена eml'], r['цена альфа'],'', row['код helix'],row['код invitro'],row['код eml']]
                break
        else:
            total.loc[len(total.index)] = [row['наименование'], row['закупка helix'] , row['стоимость helix'], row['цена alpha'],'',row['закупка invitro'], row['стоимость invitro'],row['стоимость alpha'], '', '1', '1', '1', '' ,row['код helix'],row['код invitro'],row['код eml']]

    return total


