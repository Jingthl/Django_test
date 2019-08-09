import pandas as pd
from Django_test.wsgi import *
from admin_form.models import Staff, Client, Product, Contract, Resource
import random

df = pd.read_excel('CT.xls', sheet_name='CRM全量电路')
_ = df.fillna(0, inplace=True)
for i in df.index:
    if i < 5:
        Client.objects.create(cid=str(int(df.loc[i]['客户编码'])),
                              client_name=df.loc[i]['客户名称'],
                              user_name=df.loc[i]['使用客户'],
                              standard_address=df.loc[i]['标准地址'],
                              client_address=df.loc[i]['客户地址'])
        # Product.objects.create(sid=df.loc[i]['专线号'],
        #                        status=df.loc[i]['状态'],
        #                        MKT_CHNL_NAME=df.loc[i]['MKT_CHNL_NAME'],
        #                        MKT_GRID_NAME=df.loc[i]['MKT_GRID_NAME'],
        #                        receive_org=df.loc[i]['揽收组织'],
        #                        PRODUCT_NAME=df.loc[i]['PRODUCT_NAME'],
        #                        main_set=df.loc[i]['主套餐'],
        #                        add_set=df.loc[i]['加装包'],
        #                        CRM=df.loc[i]['CRM产品名称'],
        #                        product_quality=df.loc[i]['产品性质'],
        #                        client_id=str(int(df.loc[i]['客户编码'])),
        #                        )
    else:
        break
# def main():
#
#
# if __name__ == '__main__':
#     main()
