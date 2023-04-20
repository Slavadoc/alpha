import pandas as pd

class total_data:
    def find_data(self, lab_name,alpha):
        print(f"work {self}")
        total = pd.DataFrame(columns=['код','услуга', f'цена закупки {self}',f'цена {self}','цена альфа'])
        for x, r in lab_name.iterrows():
            for i, row in alpha.iterrows():
                kod = str(row['код']).replace('!', '')
                kod = kod.replace(' ()', '')
                if r['код'] == kod:
                    total.loc[len(total.index)] = [kod, row['услуга'],row[f'цена {self}'], r['цена'], row['цена alpha']]
                    # print(f"work {kod}")
                    break
            else:
                total.loc[len(total.index)] = [str(r['код']).replace('!', '').replace(' ()', ''), row['услуга'], '1', '1' , row['цена alpha']]
        return total
        print(total.head())
        # total.to_excel('./total {name}.xlsx')