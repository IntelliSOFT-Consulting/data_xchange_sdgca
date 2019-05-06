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
indicators_a = 'NCsJ0u0J5kO;pTOpNf6zkTv;mEtKA2HMRkT;HNUVvzz5Mcb;TsZLukacJ6T;wD1WS24kqQR;pBeH3AFPieZ;cBaVY4cTk1A;nsPgvbrDPwQ;jHGHRAQ0RcL;SdGVvEDBReG;Hz6LcIaTWfY;CDWr02Kxj2X;tqDcS5WQm3T;JhZxmBFYmuL;dGsxottaM20;pH4ByZuNaRi;SDnpTlaTfuA;Bt7EwzXnP1B;NXhSDQe6OXB;KnUVvNnHny2;LgOeUwjhGva;OyAEqNG6RMg;Yk7ej3qZXDv;wZdc6Gvc3um;F2kfyiytNRy;r1tLOkgBXcw;pADPo7G4Q8n;NS7zBWqKEXq;Cl2zeNxNNEM;SJCuhkbZCqN;K35BjlZcXYV;mFeVazpypaZ;erR6FSvuScN;IcUjJW2C9Im;atbJtXLSbyf;qj15XcoUCDI;b1IbuE6i9Tc;Vak8DH4WNiD;DtwIkKQchib;HW9SvVBHjfX;Rd6xzemL4S5;iCihpG4jRzH;mH9XBhoW1Cf;pZWwlUZworn;con8QLEKvTB;rR9ege9U0X3;fqqZhw9AMvn;C22hsuW2rE5;VM8F1Q8EVxB;s4SKEVPtp2m;uR57Bcq3Rgq;KjU4p8nocJQ;aRe93xxQav7;RbhomZoQGDs;HzqYEXs8hoO;UKUOkTXaoz6;SdxjNoHJO7z;LjiN9Kh17Bj;FOp1pCnNuBo;JFvlTEuknXq;W0lTMtPnlip;o7TozpqU8FT;yj4fJbzFrfg;dlinqsDHurO;JCrwCxh05iE;MemsRPHqriD;wjtsNUXEZmA;X3pqi7fAvgs;qO7NEsYVVXN;w8oLlRxIzST;ETzoIk2kLNK;R5tq2LHUK6X;vFCUplW58Dq;x7dHhPJWJPe;K10M0TiP5Id;vmzqxcCgqPd;aGhDRO2S4Lu;Ti6DZBxiGsG;Vid4sMI2rtf;TU2VGO7AnYK;GYeuH3xRLlD;HcMZhdKHITQ;xwCjzKpZEMe;MPwkNd0OtI2;AhMpu40ZhnW;q8mm20cJoYs;ES8fQnz9u4A;JdwU3qMoYxO;SBmI91hjx3T;Ebrx1HB3nkN;kqnpnHrcTcg;q534i5qtxG2;ofjriq3zC1Y;UTKJklNQim3;ygD0dPHpavK;rW9QXpbg4Xd;cZ1kDXBQ7C2;jCcnjrZJy12;nMmhSIi5hLE;UkPFxKSr0wb;ukncn1Hlzdf;goDhooTdnpA;XgtR08R2tWT;aXgQjzyBOHY;N6fWQSZhzXS;QUGGAviJi4F;EvxREEMoa5E;OEpkeiWuqX0;iIHXuIzCh9H;DGX5LV26AD1;EUVnujhYWcR;kCRn8WKklIR;zT3hIUDKfgl;C0ScMXqXY02;WQGDscmrGgi;oqhLWFqRC14;ReqlS094zxC;rZQRXUXUPaL;NlcSFvZFfjA;ACLqta1bLlC;E8M2iiHaKLh;tl6Qlw1d0FB;j6NGNhKM1jz;MpwayQltPTy;Gtrz0rkNIH9;qVkMsM6gB9n;dX49L52V9WM;xYjKHmNPMKu;KltV9viaHHG;bKFp3z7BOK7;ePlRlJHXijB;isVafLZvrzO;dAbyaqzPFQu;nQDrXyuARRa;R64mkjYs7B7;Djjg8FIvCKp;tvhODPVwvvV;U34Rhq28dIv;sUHIdkbigKw;o8atQWjlEQ5;D1xcT46JCVw;NqFPQJkDE9I;oXdk88u7wtf;WCjZOCH6jPx;CXnbOm2RZE1;y39BBEAsVXl;HrnVSfYnHma;rrjMth4f11Z;fcy9TKaPBS0;TQGrrzcVi9a;YKfRIUfnqaw;grluc6vgaSM;F8JgS20k6r7;LGR9NIOhJZN;doGQYyiL5Xc;VGcl0oGA3gQ;wgG0LeHPhme;UYfKX2Zko4k;lAJhTUbm4uq;H45l65Grp8h;LmtfIaGo0ze;KBuWLWOnaDX;fT9njJ08ONo;DYoyQl1eYOo;ixPGl1NVAjc;M7BMX4KeItQ;QF7w41u2GJH;OI8W4V2UeCw;nhBNZvraNtR;J6mhwkHXYRX;cgp29l4lidD;APPRHhMypTn;Et4Jnj4Y0bx;jcWXxKiW0i4;DC82t4TqvSt;lWs0BXDInz8;lsR89zdhpE7;ynSFHBIYfAc;KI4KGmBjeK5;zLZFU6m9B0O;fg10UJuPwYW;V9ahdUlT8ak;uM0hXE3jV3V;f3HhCfTEkZh;cx5zefVyAZC;Yo5wu8Xtiss;h529oFxp0fz;XbyQiRu1Ut1;jvfrnV2dyE6;huEkNaUiiZS;KaRLMIg67ut;EsW7jXi2mNg;LXBAztHs8GC;jtMK6hK3BnU;IGpQdzyB9JL;umJef6viQsI;NO17dTDKMMl;piR74Xk7nQY;NtkFpqrWUUz;tFC6V5nnzan;lzvT5c6XGaS;fGrYKYgsz56;cIiBVaVnyqb;bkSUYeNHvXG;OnvFPyD5WQ4;bKVIl5DFvYH;j4w8plpRTl9;b2JULRR29Vr;OqkExkc8YQg;WNbwHJdi9fj;QIdqsSCdmSP;zrYzxKPMCUf;Uqj4TFaAjVJ;NJiuosvvTqR;R2mSVduTEHb;IifjkFPTvF9;upip89aqbWr;L4YmBBm4RmP;iXJmz0gayg2;lAJhTUbm4uq.HllvX50cXC0;H45l65Grp8h.HllvX50cXC0;LmtfIaGo0ze.HllvX50cXC0;KBuWLWOnaDX.HllvX50cXC0;fT9njJ08ONo.HllvX50cXC0;DYoyQl1eYOo.HllvX50cXC0;ixPGl1NVAjc.HllvX50cXC0;M7BMX4KeItQ.HllvX50cXC0;QF7w41u2GJH.HllvX50cXC0;DC82t4TqvSt.HllvX50cXC0;lsR89zdhpE7.HllvX50cXC0;Yo5wu8Xtiss.HllvX50cXC0;r1De8ZJQ8lV.HllvX50cXC0;XpY3cvVILxQ.HllvX50cXC0;tFC6V5nnzan.HllvX50cXC0;fGrYKYgsz56.HllvX50cXC0;cIiBVaVnyqb.HllvX50cXC0;SdGVvEDBReG.HllvX50cXC0;KnUVvNnHny2.HllvX50cXC0;MKn1soEZT8q.HllvX50cXC0;atbJtXLSbyf.HllvX50cXC0;qj15XcoUCDI.HllvX50cXC0;b1IbuE6i9Tc.HllvX50cXC0;HW9SvVBHjfX.HllvX50cXC0;fqqZhw9AMvn.HllvX50cXC0;RbhomZoQGDs.HllvX50cXC0;dlinqsDHurO.HllvX50cXC0;vFCUplW58Dq.HllvX50cXC0;K10M0TiP5Id.HllvX50cXC0;Ebrx1HB3nkN.HllvX50cXC0;kqnpnHrcTcg.ssMY53iFjYm;kqnpnHrcTcg.sLKRSW7xmwp;kqnpnHrcTcg.sJUGNYho7Ey;kqnpnHrcTcg.bJmK5mlfvQk;kqnpnHrcTcg.RmWCNbUlKNT;kqnpnHrcTcg.iEgy3xKqVi5;kqnpnHrcTcg.SiFHV5KVTgY;kqnpnHrcTcg.SOw3NHN47G7;kqnpnHrcTcg.r8hBd63qzn4;nMmhSIi5hLE.HllvX50cXC0;RL5Cd2V59j9.ssMY53iFjYm;RL5Cd2V59j9.sLKRSW7xmwp;RL5Cd2V59j9.sJUGNYho7Ey;RL5Cd2V59j9.bJmK5mlfvQk;RL5Cd2V59j9.RmWCNbUlKNT;RL5Cd2V59j9.iEgy3xKqVi5;RL5Cd2V59j9.SiFHV5KVTgY;RL5Cd2V59j9.SOw3NHN47G7;RL5Cd2V59j9.r8hBd63qzn4;OEpkeiWuqX0.HllvX50cXC0;EUVnujhYWcR.HllvX50cXC0;WQGDscmrGgi.HllvX50cXC0;E8M2iiHaKLh.HllvX50cXC0;U34Rhq28dIv.HllvX50cXC0;y39BBEAsVXl.HllvX50cXC0;grluc6vgaSM.HllvX50cXC0;F8JgS20k6r7.HllvX50cXC0;q2e5Wwjb7Ut.ssMY53iFjYm;q2e5Wwjb7Ut.sLKRSW7xmwp;q2e5Wwjb7Ut.sJUGNYho7Ey;q2e5Wwjb7Ut.bJmK5mlfvQk;q2e5Wwjb7Ut.RmWCNbUlKNT;q2e5Wwjb7Ut.iEgy3xKqVi5;q2e5Wwjb7Ut.SiFHV5KVTgY;q2e5Wwjb7Ut.SOw3NHN47G7;q2e5Wwjb7Ut.r8hBd63qzn4;ZaavkLrmpIh.HllvX50cXC0;VuxFvcDYY9Z.HllvX50cXC0;NAvcDWqehR0.ssMY53iFjYm;NAvcDWqehR0.sLKRSW7xmwp;NAvcDWqehR0.sJUGNYho7Ey;NAvcDWqehR0.bJmK5mlfvQk;NAvcDWqehR0.RmWCNbUlKNT;NAvcDWqehR0.iEgy3xKqVi5;NAvcDWqehR0.SiFHV5KVTgY;NAvcDWqehR0.SOw3NHN47G7;NAvcDWqehR0.r8hBd63qzn4;t0srib18QsM.HllvX50cXC0;cvl4sv37KRj.HllvX50cXC0;ZTHSXqAvoRh.HllvX50cXC0;oLXCIJJx7vv.HllvX50cXC0;UfvUkjWzWHS.HllvX50cXC0;TmujztOG0EK.ssMY53iFjYm;TmujztOG0EK.sLKRSW7xmwp;TmujztOG0EK.sJUGNYho7Ey;TmujztOG0EK.bJmK5mlfvQk;TmujztOG0EK.RmWCNbUlKNT;TmujztOG0EK.iEgy3xKqVi5;TmujztOG0EK.SiFHV5KVTgY;TmujztOG0EK.SOw3NHN47G7;TmujztOG0EK.r8hBd63qzn4'
indicators_b = 'HsNWdBITNHt.ssMY53iFjYm;HsNWdBITNHt.sLKRSW7xmwp;HsNWdBITNHt.sJUGNYho7Ey;HsNWdBITNHt.bJmK5mlfvQk;HsNWdBITNHt.r8hBd63qzn4;BgbLInmNwUu.HllvX50cXC0;yAEMY0V2OHY.ssMY53iFjYm;yAEMY0V2OHY.sLKRSW7xmwp;yAEMY0V2OHY.sJUGNYho7Ey;yAEMY0V2OHY.bJmK5mlfvQk;yAEMY0V2OHY.RmWCNbUlKNT;yAEMY0V2OHY.iEgy3xKqVi5;yAEMY0V2OHY.SiFHV5KVTgY;yAEMY0V2OHY.SOw3NHN47G7;yAEMY0V2OHY.r8hBd63qzn4;sSGLC3rkVGs.HllvX50cXC0'
indicators_list = [indicators_a, indicators_b]
FETCH_URL = 'https://test.sdgca.intellisoftkenya.com/nationalmrs/api/29/analytics.json?dimension=pe:'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
FILE_NAME = 'data.csv'
period = "2015"


def fetch_data():
    for indicators in indicators_list:
        url = FETCH_URL+period+"&dimension=dx:"+indicators+"&filter=ou:YIA7WLCOZd4&displayProperty=NAME"
        request = requests.get(
            url,
            auth=AUTH
        )
        create_array(request.json()['rows'])
    return 1


def create_csv(filename):
    """ create a new csv file"""
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['dataelement', 'period', 'orgunit', 'catoptcombo', 'attroptcombo', 'value', 'storedby']
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
        if ".0" in dataitems[2]:
            value = int(float(dataitems[2]))
        else:
            value = float(dataitems[2])

        add_to_csv([dataelement, period, orgunit, catoptcombo, attroptcombo, value, storedby])

    return 1


def add_to_csv(details):
    """ add organisation units to the csv file """
    with open(FILE_NAME, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(details)


if __name__ == '__main__':
    create_csv(FILE_NAME)
    data_instance = fetch_data()
    print(data_instance)
    # list_data = create_array(data_instance)
