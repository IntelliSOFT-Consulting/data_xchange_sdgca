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
FETCH_URL = 'https://test.sdgca.intellisoftkenya.com/nationalmrs/api/29/analytics.json?dimension=pe:2015&dimension=' \
            'dx:NCsJ0u0J5kO;pTOpNf6zkTv;mEtKA2HMRkT;HNUVvzz5Mcb;TsZLukacJ6T;wD1WS24kqQR;pBeH3AFPieZ;cBaVY4cTk1A;nsPgvbrDPwQ;' \
            'jHGHRAQ0RcL;SdGVvEDBReG;Hz6LcIaTWfY;CDWr02Kxj2X;tqDcS5WQm3T;JhZxmBFYmuL;dGsxottaM20;pH4ByZuNaRi;SDnpTlaTfuA;Bt7EwzXnP1B;' \
            'NXhSDQe6OXB;KnUVvNnHny2;LgOeUwjhGva;OyAEqNG6RMg;Yk7ej3qZXDv;wZdc6Gvc3um;F2kfyiytNRy;r1tLOkgBXcw;pADPo7G4Q8n;NS7zBWqKEXq;' \
            'Cl2zeNxNNEM;SJCuhkbZCqN;K35BjlZcXYV;mFeVazpypaZ;erR6FSvuScN;IcUjJW2C9Im;atbJtXLSbyf;qj15XcoUCDI;b1IbuE6i9Tc;Vak8DH4WNiD;' \
            'DtwIkKQchib;HW9SvVBHjfX;Rd6xzemL4S5;iCihpG4jRzH;mH9XBhoW1Cf;pZWwlUZworn;con8QLEKvTB;rR9ege9U0X3;fqqZhw9AMvn;C22hsuW2rE5;' \
            'VM8F1Q8EVxB;s4SKEVPtp2m;uR57Bcq3Rgq;KjU4p8nocJQ;aRe93xxQav7;RbhomZoQGDs;HzqYEXs8hoO;UKUOkTXaoz6;SdxjNoHJO7z;LjiN9Kh17Bj;' \
            'FOp1pCnNuBo;JFvlTEuknXq;W0lTMtPnlip;o7TozpqU8FT;yj4fJbzFrfg;dlinqsDHurO;JCrwCxh05iE;MemsRPHqriD;wjtsNUXEZmA;X3pqi7fAvgs;' \
            'qO7NEsYVVXN;w8oLlRxIzST;ETzoIk2kLNK;R5tq2LHUK6X;vFCUplW58Dq;x7dHhPJWJPe;K10M0TiP5Id;vmzqxcCgqPd;aGhDRO2S4Lu;Ti6DZBxiGsG;' \
            'Vid4sMI2rtf;TU2VGO7AnYK;GYeuH3xRLlD;HcMZhdKHITQ;xwCjzKpZEMe;MPwkNd0OtI2;AhMpu40ZhnW;q8mm20cJoYs;ES8fQnz9u4A;JdwU3qMoYxO;' \
            'SBmI91hjx3T;Ebrx1HB3nkN;kqnpnHrcTcg;q534i5qtxG2;ofjriq3zC1Y;UTKJklNQim3;ygD0dPHpavK;rW9QXpbg4Xd;cZ1kDXBQ7C2;jCcnjrZJy12;' \
            'nMmhSIi5hLE;UkPFxKSr0wb;ukncn1Hlzdf;goDhooTdnpA;XgtR08R2tWT;aXgQjzyBOHY;N6fWQSZhzXS;QUGGAviJi4F;EvxREEMoa5E;OEpkeiWuqX0;' \
            'iIHXuIzCh9H;DGX5LV26AD1;EUVnujhYWcR;kCRn8WKklIR;zT3hIUDKfgl;C0ScMXqXY02;WQGDscmrGgi;oqhLWFqRC14;ReqlS094zxC;rZQRXUXUPaL;' \
            'NlcSFvZFfjA;ACLqta1bLlC;E8M2iiHaKLh;tl6Qlw1d0FB;j6NGNhKM1jz;MpwayQltPTy;Gtrz0rkNIH9;qVkMsM6gB9n;dX49L52V9WM;xYjKHmNPMKu;' \
            'KltV9viaHHG;bKFp3z7BOK7;ePlRlJHXijB;isVafLZvrzO;dAbyaqzPFQu;nQDrXyuARRa;R64mkjYs7B7;Djjg8FIvCKp;tvhODPVwvvV;U34Rhq28dIv;' \
            'sUHIdkbigKw;o8atQWjlEQ5;D1xcT46JCVw;NqFPQJkDE9I;oXdk88u7wtf;WCjZOCH6jPx;CXnbOm2RZE1;y39BBEAsVXl;HrnVSfYnHma;rrjMth4f11Z;' \
            'fcy9TKaPBS0;TQGrrzcVi9a;YKfRIUfnqaw;grluc6vgaSM;F8JgS20k6r7;LGR9NIOhJZN;doGQYyiL5Xc;VGcl0oGA3gQ;wgG0LeHPhme;UYfKX2Zko4k;' \
            'lAJhTUbm4uq;H45l65Grp8h;LmtfIaGo0ze;KBuWLWOnaDX;fT9njJ08ONo;DYoyQl1eYOo;ixPGl1NVAjc;M7BMX4KeItQ;QF7w41u2GJH;OI8W4V2UeCw;' \
            'nhBNZvraNtR;J6mhwkHXYRX;cgp29l4lidD;APPRHhMypTn;Et4Jnj4Y0bx;jcWXxKiW0i4;DC82t4TqvSt;lWs0BXDInz8;lsR89zdhpE7;ynSFHBIYfAc;' \
            'KI4KGmBjeK5;zLZFU6m9B0O;fg10UJuPwYW;V9ahdUlT8ak;uM0hXE3jV3V;f3HhCfTEkZh;cx5zefVyAZC;Yo5wu8Xtiss;h529oFxp0fz;XbyQiRu1Ut1;' \
            'jvfrnV2dyE6;huEkNaUiiZS;KaRLMIg67ut;EsW7jXi2mNg;LXBAztHs8GC;jtMK6hK3BnU;IGpQdzyB9JL;umJef6viQsI;NO17dTDKMMl;piR74Xk7nQY;' \
            'NtkFpqrWUUz;tFC6V5nnzan;lzvT5c6XGaS;fGrYKYgsz56;cIiBVaVnyqb;bkSUYeNHvXG;OnvFPyD5WQ4;bKVIl5DFvYH;j4w8plpRTl9;b2JULRR29Vr;' \
            'OqkExkc8YQg;WNbwHJdi9fj;QIdqsSCdmSP;zrYzxKPMCUf;Uqj4TFaAjVJ;NJiuosvvTqR;R2mSVduTEHb;IifjkFPTvF9;upip89aqbWr;L4YmBBm4RmP;' \
            'iXJmz0gayg2&filter=ou:YIA7WLCOZd4&displayProperty=NAME'
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
            ['dataelementid', 'period', 'value','storedby']
        )


def create_array(data):
    storedby = 'fegati'
    for dataitems in data:
        dataelement = dataitems[0];
        period = dataitems[1]
        value = dataitems[2]

        add_to_csv([dataelement,period,value,storedby])



def add_to_csv(details):
    ''' add organisation units to the csv file '''
    with open(FILE_NAME, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(details)


if __name__ == '__main__':
    create_csv(FILE_NAME)
    data_instance = fetch_data()
    list_data = create_array(data_instance)
