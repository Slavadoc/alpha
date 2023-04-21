import pandas as pd
from data.total_data import total_data

class total_invitro_data(total_data):
    print("work total invitro data ")

total_invitro_data = total_invitro_data()

total_invitro_data.find_data("invitro", )

    # invitro = pd.read_excel('./data/invitro/data/invitro.xlsx')
    # alpha_invitro = pd.read_excel('./data/invitro/data/total_invitro.xlsx')
    # total = pd.DataFrame(columns=['код','услуга', 'цена закупки invitro','цена invitro','цена альфа'])
    #
    # for x, r in invitro.iterrows():
    #     for i, row in alpha_invitro.iterrows():
    #         kod = str(row['код']).replace('!', '')
    #         kod = kod.replace(' ()', '')
    #         if r['код'] == kod:
    #             total.loc[len(total.index)] = [kod, row['услуга'],row['цена инвитро'], r['цена'], row['цена альфа']]
    #             break
    #     else:
    #         total.loc[len(total.index)] = [str(row['код']).replace('!', '').replace(' ()', ''), row['услуга'], '1', '1' , row['цена альфа']]
    # return total

# print(total.head())
# total.to_excel('./total invitro.xlsx')
