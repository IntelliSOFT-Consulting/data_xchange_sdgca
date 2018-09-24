"""
Fetch org units from one dhis2 instance to another
July 7th, 2018
Python 3.6.5
"""
import argparse
import csv

import requests


USERNAME = 'fegati'
PASSWORD = 'Sdgca@2018'
FETCH_URL = 'https://test.sdgca.intellisoftkenya.com/nationalmrs/api/29/analytics.json?dimension=pe:2015&dimension=dx:LGR9NIOhJZN.HllvX50cXC0;' \
            'doGQYyiL5Xc.HllvX50cXC0;VGcl0oGA3gQ.HllvX50cXC0;wgG0LeHPhme.HllvX50cXC0;UYfKX2Zko4k.HllvX50cXC0;lAJhTUbm4uq.HllvX50cXC0;' \
            'H45l65Grp8h.HllvX50cXC0;LmtfIaGo0ze.HllvX50cXC0;KBuWLWOnaDX.HllvX50cXC0;fT9njJ08ONo.HllvX50cXC0;DYoyQl1eYOo.HllvX50cXC0;' \
            'ixPGl1NVAjc.HllvX50cXC0;M7BMX4KeItQ.HllvX50cXC0;QF7w41u2GJH.HllvX50cXC0;OI8W4V2UeCw.HllvX50cXC0;nhBNZvraNtR.HllvX50cXC0;' \
            'J6mhwkHXYRX.HllvX50cXC0;cgp29l4lidD.HllvX50cXC0;APPRHhMypTn.HllvX50cXC0;Et4Jnj4Y0bx.HllvX50cXC0;jcWXxKiW0i4.HllvX50cXC0;' \
            'DC82t4TqvSt.HllvX50cXC0;lWs0BXDInz8.HllvX50cXC0;lsR89zdhpE7.HllvX50cXC0;ynSFHBIYfAc.HllvX50cXC0;KI4KGmBjeK5.HllvX50cXC0;' \
            'zLZFU6m9B0O.HllvX50cXC0;fg10UJuPwYW.HllvX50cXC0;V9ahdUlT8ak.HllvX50cXC0;uM0hXE3jV3V.HllvX50cXC0;f3HhCfTEkZh.HllvX50cXC0;' \
            'cx5zefVyAZC.HllvX50cXC0;Yo5wu8Xtiss.HllvX50cXC0;h529oFxp0fz.HllvX50cXC0;XbyQiRu1Ut1.HllvX50cXC0;jvfrnV2dyE6.HllvX50cXC0;' \
            'huEkNaUiiZS.ssMY53iFjYm;huEkNaUiiZS.sLKRSW7xmwp;huEkNaUiiZS.sJUGNYho7Ey;huEkNaUiiZS.bJmK5mlfvQk;huEkNaUiiZS.RmWCNbUlKNT;' \
            'huEkNaUiiZS.iEgy3xKqVi5;huEkNaUiiZS.SiFHV5KVTgY;huEkNaUiiZS.SOw3NHN47G7;huEkNaUiiZS.r8hBd63qzn4;KaRLMIg67ut.ssMY53iFjYm;' \
            'KaRLMIg67ut.sLKRSW7xmwp;KaRLMIg67ut.sJUGNYho7Ey;KaRLMIg67ut.bJmK5mlfvQk;KaRLMIg67ut.RmWCNbUlKNT;KaRLMIg67ut.iEgy3xKqVi5;' \
            'KaRLMIg67ut.SiFHV5KVTgY;KaRLMIg67ut.SOw3NHN47G7;KaRLMIg67ut.r8hBd63qzn4;EsW7jXi2mNg.HllvX50cXC0;LXBAztHs8GC.HllvX50cXC0;' \
            'jtMK6hK3BnU.HllvX50cXC0;IGpQdzyB9JL.HllvX50cXC0;umJef6viQsI.HllvX50cXC0;NO17dTDKMMl.HllvX50cXC0;piR74Xk7nQY.HllvX50cXC0;' \
            'NtkFpqrWUUz.HllvX50cXC0;tFC6V5nnzan.HllvX50cXC0;lzvT5c6XGaS.HllvX50cXC0;fGrYKYgsz56.HllvX50cXC0;cIiBVaVnyqb.HllvX50cXC0;' \
            'bkSUYeNHvXG.HllvX50cXC0;OnvFPyD5WQ4.HllvX50cXC0;bKVIl5DFvYH.HllvX50cXC0;j4w8plpRTl9.HllvX50cXC0;b2JULRR29Vr.HllvX50cXC0;' \
            'OqkExkc8YQg.HllvX50cXC0;WNbwHJdi9fj.HllvX50cXC0;QIdqsSCdmSP.HllvX50cXC0;zrYzxKPMCUf.HllvX50cXC0;Uqj4TFaAjVJ.HllvX50cXC0;' \
            'NJiuosvvTqR.HllvX50cXC0;R2mSVduTEHb.HllvX50cXC0;IifjkFPTvF9.HllvX50cXC0;upip89aqbWr.HllvX50cXC0;L4YmBBm4RmP.HllvX50cXC0;' \
            'iXJmz0gayg2.HllvX50cXC0;wD1WS24kqQR.ssMY53iFjYm;wD1WS24kqQR.sLKRSW7xmwp;wD1WS24kqQR.sJUGNYho7Ey;wD1WS24kqQR.bJmK5mlfvQk;' \
            'wD1WS24kqQR.RmWCNbUlKNT;wD1WS24kqQR.iEgy3xKqVi5;wD1WS24kqQR.SiFHV5KVTgY;wD1WS24kqQR.SOw3NHN47G7;wD1WS24kqQR.r8hBd63qzn4;' \
            'TsZLukacJ6T.ssMY53iFjYm;TsZLukacJ6T.sLKRSW7xmwp;TsZLukacJ6T.sJUGNYho7Ey;TsZLukacJ6T.bJmK5mlfvQk;TsZLukacJ6T.RmWCNbUlKNT;' \
            'TsZLukacJ6T.iEgy3xKqVi5;TsZLukacJ6T.SiFHV5KVTgY;TsZLukacJ6T.SOw3NHN47G7;TsZLukacJ6T.r8hBd63qzn4;HNUVvzz5Mcb.ssMY53iFjYm;' \
            'HNUVvzz5Mcb.sLKRSW7xmwp;HNUVvzz5Mcb.sJUGNYho7Ey;HNUVvzz5Mcb.bJmK5mlfvQk;HNUVvzz5Mcb.RmWCNbUlKNT;HNUVvzz5Mcb.iEgy3xKqVi5;' \
            'HNUVvzz5Mcb.SiFHV5KVTgY;HNUVvzz5Mcb.SOw3NHN47G7;HNUVvzz5Mcb.r8hBd63qzn4;mEtKA2HMRkT.ssMY53iFjYm;mEtKA2HMRkT.sLKRSW7xmwp;' \
            'mEtKA2HMRkT.sJUGNYho7Ey;mEtKA2HMRkT.bJmK5mlfvQk;mEtKA2HMRkT.RmWCNbUlKNT;mEtKA2HMRkT.iEgy3xKqVi5;mEtKA2HMRkT.SiFHV5KVTgY;' \
            'mEtKA2HMRkT.SOw3NHN47G7;mEtKA2HMRkT.r8hBd63qzn4;pTOpNf6zkTv.ssMY53iFjYm;pTOpNf6zkTv.sLKRSW7xmwp;pTOpNf6zkTv.sJUGNYho7Ey;' \
            'pTOpNf6zkTv.bJmK5mlfvQk;pTOpNf6zkTv.RmWCNbUlKNT;pTOpNf6zkTv.iEgy3xKqVi5;pTOpNf6zkTv.SiFHV5KVTgY;pTOpNf6zkTv.SOw3NHN47G7;' \
            'pTOpNf6zkTv.r8hBd63qzn4;NCsJ0u0J5kO.ssMY53iFjYm;NCsJ0u0J5kO.sLKRSW7xmwp;NCsJ0u0J5kO.sJUGNYho7Ey;NCsJ0u0J5kO.bJmK5mlfvQk;' \
            'NCsJ0u0J5kO.RmWCNbUlKNT;NCsJ0u0J5kO.iEgy3xKqVi5;NCsJ0u0J5kO.SiFHV5KVTgY;NCsJ0u0J5kO.SOw3NHN47G7;NCsJ0u0J5kO.r8hBd63qzn4;' \
            'pBeH3AFPieZ.HllvX50cXC0;cBaVY4cTk1A.HllvX50cXC0;nsPgvbrDPwQ.HllvX50cXC0;jHGHRAQ0RcL.HllvX50cXC0;SdGVvEDBReG.HllvX50cXC0;' \
            'Hz6LcIaTWfY.HllvX50cXC0;CDWr02Kxj2X.HllvX50cXC0;tqDcS5WQm3T.HllvX50cXC0;JhZxmBFYmuL.HllvX50cXC0;dGsxottaM20.HllvX50cXC0;' \
            'pH4ByZuNaRi.HllvX50cXC0;SDnpTlaTfuA.HllvX50cXC0;Bt7EwzXnP1B.HllvX50cXC0;NXhSDQe6OXB.HllvX50cXC0;KnUVvNnHny2.HllvX50cXC0;' \
            'LgOeUwjhGva.HllvX50cXC0;OyAEqNG6RMg.HllvX50cXC0;Yk7ej3qZXDv.HllvX50cXC0;wZdc6Gvc3um.HllvX50cXC0;F2kfyiytNRy.HllvX50cXC0;' \
            'r1tLOkgBXcw.HllvX50cXC0;pADPo7G4Q8n.HllvX50cXC0;NS7zBWqKEXq.HllvX50cXC0;Cl2zeNxNNEM.HllvX50cXC0;SJCuhkbZCqN.HllvX50cXC0;' \
            'K35BjlZcXYV.HllvX50cXC0;mFeVazpypaZ.HllvX50cXC0;erR6FSvuScN.HllvX50cXC0;IcUjJW2C9Im.HllvX50cXC0;atbJtXLSbyf.HllvX50cXC0;' \
            'qj15XcoUCDI.HllvX50cXC0;b1IbuE6i9Tc.HllvX50cXC0;Vak8DH4WNiD.HllvX50cXC0;DtwIkKQchib.HllvX50cXC0;HW9SvVBHjfX.HllvX50cXC0;' \
            'Rd6xzemL4S5.HllvX50cXC0;iCihpG4jRzH.HllvX50cXC0;mH9XBhoW1Cf.HllvX50cXC0;pZWwlUZworn.HllvX50cXC0;con8QLEKvTB.HllvX50cXC0;' \
            'rR9ege9U0X3.HllvX50cXC0;fqqZhw9AMvn.HllvX50cXC0;C22hsuW2rE5.HllvX50cXC0;VM8F1Q8EVxB.HllvX50cXC0;s4SKEVPtp2m.HllvX50cXC0;' \
            'uR57Bcq3Rgq.HllvX50cXC0;KjU4p8nocJQ.HllvX50cXC0;aRe93xxQav7.HllvX50cXC0;RbhomZoQGDs.HllvX50cXC0;HzqYEXs8hoO.HllvX50cXC0;' \
            'UKUOkTXaoz6.HllvX50cXC0;SdxjNoHJO7z.HllvX50cXC0;LjiN9Kh17Bj.HllvX50cXC0;FOp1pCnNuBo.HllvX50cXC0;JFvlTEuknXq.HllvX50cXC0;' \
            'W0lTMtPnlip.HllvX50cXC0;o7TozpqU8FT.HllvX50cXC0;yj4fJbzFrfg.HllvX50cXC0;dlinqsDHurO.HllvX50cXC0;JCrwCxh05iE.HllvX50cXC0;' \
            'MemsRPHqriD.HllvX50cXC0;wjtsNUXEZmA.HllvX50cXC0;X3pqi7fAvgs.HllvX50cXC0;qO7NEsYVVXN.HllvX50cXC0;w8oLlRxIzST.HllvX50cXC0;' \
            'ETzoIk2kLNK.HllvX50cXC0;R5tq2LHUK6X.HllvX50cXC0;vFCUplW58Dq.HllvX50cXC0;x7dHhPJWJPe.HllvX50cXC0;K10M0TiP5Id.HllvX50cXC0;' \
            'vmzqxcCgqPd.HllvX50cXC0;aGhDRO2S4Lu.HllvX50cXC0;Ti6DZBxiGsG.HllvX50cXC0;Vid4sMI2rtf.HllvX50cXC0;TU2VGO7AnYK.HllvX50cXC0;' \
            'GYeuH3xRLlD.HllvX50cXC0;HcMZhdKHITQ.HllvX50cXC0;xwCjzKpZEMe.HllvX50cXC0;MPwkNd0OtI2.ssMY53iFjYm;MPwkNd0OtI2.sLKRSW7xmwp;' \
            'MPwkNd0OtI2.sJUGNYho7Ey;MPwkNd0OtI2.bJmK5mlfvQk;MPwkNd0OtI2.RmWCNbUlKNT;MPwkNd0OtI2.iEgy3xKqVi5;MPwkNd0OtI2.SiFHV5KVTgY;' \
            'MPwkNd0OtI2.SOw3NHN47G7;MPwkNd0OtI2.r8hBd63qzn4;AhMpu40ZhnW.ssMY53iFjYm;AhMpu40ZhnW.sLKRSW7xmwp;AhMpu40ZhnW.sJUGNYho7Ey;' \
            'AhMpu40ZhnW.bJmK5mlfvQk;AhMpu40ZhnW.RmWCNbUlKNT;AhMpu40ZhnW.iEgy3xKqVi5;AhMpu40ZhnW.SiFHV5KVTgY;AhMpu40ZhnW.SOw3NHN47G7;' \
            'AhMpu40ZhnW.r8hBd63qzn4;q8mm20cJoYs.ssMY53iFjYm;q8mm20cJoYs.sLKRSW7xmwp;q8mm20cJoYs.sJUGNYho7Ey;q8mm20cJoYs.bJmK5mlfvQk;' \
            'q8mm20cJoYs.RmWCNbUlKNT;q8mm20cJoYs.iEgy3xKqVi5;q8mm20cJoYs.SiFHV5KVTgY;q8mm20cJoYs.SOw3NHN47G7;q8mm20cJoYs.r8hBd63qzn4;' \
            'ES8fQnz9u4A.HllvX50cXC0;JdwU3qMoYxO.HllvX50cXC0;SBmI91hjx3T.ssMY53iFjYm;SBmI91hjx3T.sLKRSW7xmwp;SBmI91hjx3T.sJUGNYho7Ey;' \
            'SBmI91hjx3T.bJmK5mlfvQk;SBmI91hjx3T.RmWCNbUlKNT;SBmI91hjx3T.iEgy3xKqVi5;SBmI91hjx3T.SiFHV5KVTgY;SBmI91hjx3T.SOw3NHN47G7;' \
            'SBmI91hjx3T.r8hBd63qzn4;Ebrx1HB3nkN.HllvX50cXC0;kqnpnHrcTcg.ssMY53iFjYm;kqnpnHrcTcg.sLKRSW7xmwp;kqnpnHrcTcg.sJUGNYho7Ey;' \
            'kqnpnHrcTcg.bJmK5mlfvQk;kqnpnHrcTcg.RmWCNbUlKNT;kqnpnHrcTcg.iEgy3xKqVi5;kqnpnHrcTcg.SiFHV5KVTgY;kqnpnHrcTcg.SOw3NHN47G7;' \
            'kqnpnHrcTcg.r8hBd63qzn4;q534i5qtxG2.HllvX50cXC0;ofjriq3zC1Y.HllvX50cXC0;UTKJklNQim3.HllvX50cXC0;ygD0dPHpavK.HllvX50cXC0' \
            '&filter=ou:YIA7WLCOZd4&displayProperty=NAME'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
FILE_NAME = 'data.csv'




def fetch_data():
    url = FETCH_URL
    request = requests.get(
        url,
        auth=AUTH
    )
    return request.json()['rows']


def create_csv(filename):
    ''' create a new csv file'''
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['dataelement', 'period', 'orgunit', 'catoptcombo', 'attroptcombo' 'value','storedby']
        )


def create_array(data):
    storedby = 'fegati'
    orgunit = 'YIA7WLCOZd4'
    attroptcombo = ''
    for dataitems in data:
        dataelement_categoryoption = dataitems[0]
        element_cat = dataelement_categoryoption.split('.')
        dataelement = element_cat[0]
        catoptcombo = element_cat[1]
        period = dataitems[1]
        if (".0" in dataitems[2]):
            value = int(float(dataitems[2]))
        else:
            value = float(dataitems[2])

        add_to_csv([dataelement,period,orgunit,catoptcombo,attroptcombo,value,storedby])



def add_to_csv(details):
    ''' add organisation units to the csv file '''
    with open(FILE_NAME, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(details)


if __name__ == '__main__':
    create_csv(FILE_NAME)
    data_instance = fetch_data()
    list_data = create_array(data_instance)
