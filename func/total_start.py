import pandas as pd
from datetime import datetime
from func.total_data import total_data

def total_start():
    from func.total_helix import total_helix
    # from func.total_invitro import total_invitro
    # from func.total import total
    # from data.helix.total_helix import total_helix_data
    # from data.invitro.total_invitro import total_invitro_data

    invitro = pd.read_excel('./data/invitro/data/invitro.xlsx')
    alpha = pd.read_excel('./data/invitro/data/total_invitro.xlsx')
    invitro = total_data.find_data("invitro", invitro, alpha)

    helix_alpha = pd.read_excel('./data/helix/data/total_helix.xlsx')
    helix = pd.read_excel('./data/helix/data/helix.xlsx')
    helix = total_data.find_data("helix", helix, helix_alpha)

    eml_apha = pd.read_excel('./data/eml/data/total_eml.xlsx')
    eml = pd.read_excel('./data/eml/data/eml.xlsx')
    eml = total_data.find_data("eml", eml, eml_apha)
    
    shablon = pd.read_excel('./data/shablon.xlsx')
    total_helix = total_helix(helix, shablon)
    print(total_helix.columns.tolist())


    # invitro = pd.read_excel('./data/total invitro.xlsx')
    # helix = pd.read_excel('./data/helix/total helix.xlsx')
    # invitro = total_invitro_data(invitro, alpha_invitro)
    # helix = total_helix_data()
    # eml = pd.read_excel('./data/eml/total eml.xlsx')

    #
    #
    # total_invitro = total_invitro(invitro, total_helix)
    # # 'наименование', 'закупка helix','стоимость helix','цена alpha', 'закупка invitro', 'стоимость invitro','стоимость alpha','код helix', 'код invitro', 'код eml'
    # total = total(eml, total_invitro)
    #
    # print(total.columns.tolist())
    # current_date = datetime.now().date()
    # print(current_date)
    # print(total.head(20))
    # writer = pd.ExcelWriter(f"total_{current_date}.xlsx")
    # total.to_excel(writer)
    # writer.save()
