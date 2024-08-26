"""
	put backups here as a variable:
"""

# balanceSheet = {
#     'وجه نقد': 'cash', 'حساب دریافتنی': 'Net Receivables',
#     'سرمایه گذاری کوتاه مدت': 'Short Term Investments', 'موجودی کالا': 'Inventory',
#     'دارایی جاری': 'Total Current Assets', 'سرمایه گذاری بلند مدت': 'LongTermInvestments',
#     'دارایی ثابت': 'Property Plant And Equipment', 'دارایی نامشهود': 'intangible assets',
#     'دارایی': 'Total Assets', 'حساب پرداختنی': 'Accounts Payable',
#     'بدهی جاری': 'Total Current Liabilities', 'بدهی': 'Total Liabilities', 'سرمایه': 'capital',
#     'سود انباشته': 'Retained Earnings', 'حقوق صاحبان سهام': 'Equity', 'پیش  پرداخت': 'PrePayment',
# }
# income = {'فروش': 'Total income',
#           'سود ناخالص': 'GrossProfit',
#           'سود عملیاتی': 'OperatingIncomeOrLoss',
#           'هزینه مالی': 'InterestExpense',
#           'سود قبل مالیات': 'IncomeBeforeTax',
#           'سود خالص': 'NetIncome'}
# Ratio = {'جاری': 'Current Ratio', 'آنی': 'Quick Ratio', 'نقد': 'Cash Ratio', 'بدهی(درصد)': 'D/A',
#          'بدهی به ح ص س': 'D/E', 'گردش دارای(بار)': 'S/A',
#          'دوره گردش موجودی ': 'Inventory Turnover Ratio',
#          'دوره گردش حساب پرداختنی (روز)': 'Accounts  Payable Turnover Ratio', 'حاشیه سود خالص (درصد)': 'Profit Margin',
#          'حاشیه سود ناخالص (درصد)': 'Gross Profit Margin', 'سود عملیاتی به سود ناخالص(درصد)': 'EBIT/GrossProfit',
#          'هزینه بهره به سود عملیاتی (درصد)': 'r/EBIT', 'بازده دارایی (درصد)': 'ROA', 'بازده ح ص س (درصد)': 'ROE'}
#

# never delete all_ids:
all_ids = ['IRO1PARK0001', 'IRO7GHUP0001', 'IRO1FNAR0001', 'IRO7VIRP0001', 'IRO3BGHZ0001', 'IRO1PPAM0001',
           'IRO1LMIR0001', 'IRO1ALBZ0001', 'IRO7KTAP0001', 'IRO3KSPZ0001', 'IRO1NSPS0001', 'IRO1MKBT0001',
           'IRO1MADN0001', 'IRO7SFAP0001', 'IRO1GNJN0001', 'IRO1NALM0001', 'IRO3PKSH0001', 'IRO3PSKZ0001',
           'IRO3PGLZ0001', 'IRO1HJPT0001', 'IRO1RKSH0001', 'IRO3GFRZ0001', 'IRO1DKSR0001', 'IRO1BANK0001',
           'IRO1SKRN0001', 'IRO1TAYD0001', 'IRO1PSIR0001', 'IRO1PKLJ0001', 'IRO1PKER0001', 'IRO3JPRZ0001',
           'IRO7PESP0001', 'IRO3BLKZ0001', 'IRO1AMLH0001', 'IRO7FROP0001', 'IRO1NIKI0001', 'IRO1NSAZ0001',
           'IRO1FIBR0001', 'IRO1TRIR0001', 'IRO7MOZP0001', 'IRO1HTOK0001', 'IRO1DODE0001', 'IRO1TKIN0001',
           'IRO1RINM0001', 'IRO3ETLZ0001', 'IRO1GOLG0001', 'IRO1SFRS0001', 'IRO1HMRZ0001', 'IRO1DADE0001',
           'IRO1MOBN0001', 'IRO1FOLD0001', 'IRO1NASI0001', 'IRO3PMRZ0001', 'IRO1PKHA0001', 'IRO1CHAR0001',
           'IRO1KSIM0001', 'IRO1MNGZ0001', 'IRO1BRKT0001', 'IRO1DSBH0001', 'IRO1SBAH0001', 'IRO1DJBR0001',
           'IRO3MPRZ0001', 'IRO7SHQP0001', 'IRO1KAVR0001', 'IRO1NOSH0001', 'IRO1MRAM0001', 'IRO1TRNS0001',
           'IRO1SEPA0001', 'IRO1SHND0001', 'IRO1PFRB0001', 'IRO1IPTR0001', 'IRO1DDPK0001', 'IRO7BIRP0001',
           'IRO1MELT0001', 'IRO1GMEL0001', 'IRO1ALVN0001', 'IRO7ARSP0001', 'IRO1SAND0001', 'IRO3SHHZ0001',
           'IRO1IPAR0001', 'IRO1BHSM0001', 'IRO1IKHR0001', 'IRO1TOSA0001', 'IRO1BFJR0001', 'IRO1PKOD0001',
           'IRO1GCOZ0001', 'IRO1PIRN0001', 'IRO1DZAH0001', 'IRO1SHSI0001', 'IRO1PMSZ0001', 'IRO1PDRO0001',
           'IRO1GOST0001', 'IRO3CHRZ0001', 'IRO1BIME0001', 'IRO1BPAR0001', 'IRO3SYNZ0001', 'IRO3BHPZ0001',
           'IRO1CHIR0001', 'IRO1SSIN0001', 'IRO1PTAP0001', 'IRO1FKAS0001', 'IRO1IKCO0001', 'IRO1ATDM0001',
           'IRO1FAJR0001', 'IRO1KSAD0001', 'IRO1SIPA0001', 'IRO7AZRP0001', 'IRO1AMIN0001', 'IRO7TSAP0001',
           'IRO1NOVN0001', 'IRO1SNMA0001', 'IRO1SORB0001', 'IRO1SKER0001', 'IRO1THSH0001', 'IRO1SHAD0001',
           'IRO3KBCZ0001', 'IRO3PKDZ0001', 'IRO1KSKA0001', 'IRO1NSTH0001', 'IRO1FKHZ0001', 'IRO7RZIP0001',
           'IRO1GORJ0001', 'IRO1DMOR0001', 'IRO1CONT0001', 'IRO1BPAS0001', 'IRO1OFRS0001', 'IRO3PZGZ0001',
           'IRO3ZAGZ0001', 'IRO1PSHZ0001', 'IRO1SBOJ0001', 'IRO1BSTE0001', 'IRO1RSAP0001', 'IRO1ASIA0001',
           'IRO1AZIN0001', 'IRO7IRNP0001', 'IRO7KMSP0001', 'IRO1TAMI0001', 'IRO1SADB0001', 'IRO1LKGH0001',
           'IRO1KNRZ0001', 'IRO1TMKH0001', 'IRO3HORZ0001', 'IRO1OIMC0001', 'IRO1SDID0001', 'IRO1JAMD0001',
           'IRO1MESI0001', 'IRO1EPRS0001', 'IRO7DSHP0001', 'IRO1DALZ0001', 'IRO1RIIR0001', 'IRO3DBRZ0001',
           'IRO1ROZD0001', 'IRO1MSTI0001', 'IRO1GLOR0001', 'IRO7PAIP0001', 'IRO1GPSH0001', 'IRO3FOHZ0001',
           'IRO1GGAZ0001', 'IRO7SNOP0001', 'IRO1DSOB0001', 'IRO1DFRB0001', 'IRO7ITLP0001', 'IRO1DOSE0001',
           'IRO1BTEJ0001', 'IRO1OFST0001', 'IRO1SBHN0001', 'IRO7ALTP0001', 'IRO1SYSM0001', 'IRO7PYAP0001',
           'IRO1GDIR0001', 'IRO7ABGP0001', 'IRO1BMEL0001', 'IRO1ABAD0001', 'IRO1MHKM0001', 'IRO7KHDP0001',
           'IRO1BAHN0001', 'IRO7PRMP0001', 'IRO7SESP0001', 'IRO3BMDZ0001', 'IRO3GASZ0001', 'IRO7CTSP0001',
           'IRO1DAML0001', 'IRO1GHAT0001', 'IRO1SGRB0001', 'IRO1INDM0001', 'IRO1SSHR0001', 'IRO1BAFG0001',
           'IRO1GSKE0001', 'IRO3HPRZ0001', 'IRO1SAKH0001', 'IRO1SEFH0001', 'IRO7GPHP0001', 'IRO1KRIR0001',
           'IRO7SDRP0001', 'IRO1KALZ0001', 'IRO1PSER0001', 'IRO1MAGS0001', 'IRO1TSHE0001', 'IRO1KCHI0001',
           'IRO1PETR0001', 'IRO3KAHZ0001', 'IRO1BAMA0001', 'IRO1BALI0001', 'IRO1SPKH0001', 'IRO1SZPO0001',
           'IRO1TKNO0001', 'IRO7GAZP0001', 'IRO7TKDP0001', 'IRO3GOMZ0001', 'IRO3KZGZ0001', 'IRO1SROD0001',
           'IRO1KGND0001', 'IRO1TMEL0001', 'IRO3ARFZ0001', 'IRO3BHLZ0001', 'IRO7FVAP0001', 'IRO1KDPS0001',
           'IRO1MSMI0001', 'IRO3ZNDZ0001', 'IRO7PTOP0001', 'IRO1GESF0001', 'IRO7GTOP0001', 'IRO7KSNP0001',
           'IRO1DRKH0001', 'IRO1SHMD0001', 'IRO7RAHP0001', 'IRO3KRMZ0001', 'IRO1ALIR0001', 'IRO1SWIC0001',
           'IRO1DRZK0001', 'IRO3LIAZ0001', 'IRO1SINA0001', 'IRO3GHSZ0001', 'IRO1PRKT0001', 'IRO1RTIR0001',
           'IRO1SGOS0001', 'IRO3SBZZ0001', 'IRO1TKSM0001', 'IRO3SLVZ0001', 'IRO1BHMN0001', 'IRO7ARTP0001',
           'IRO1RADI0001', 'IRO1SAMA0001', 'IRO1CHCH0001', 'IRO1GNBO0001', 'IRO1FRVR0001', 'IRO7DHVP0001',
           'IRO1KSHJ0001', 'IRO1BSDR0001', 'IRO3SOBZ0001', 'IRR1KSIM0101', 'IRO1SGEN0001', 'IRO3BKSZ0001',
           'IRO1AZAB0001', 'IRO1NBEH0001', 'IRO1SAJN0001', 'IRO1DPAK0001', 'IRO1SHPZ0001', 'IRO1KFAN0001',
           'IRO1VLMT0001', 'IRO7DANP0001', 'IRO1IAGM0001', 'IRO7IRGP0001', 'IRO1PASN0001', 'IRO1DLGM0001',
           'IRO1SIMS0001', 'IRO1PNES0001', 'IRO1CIDC0001', 'IRO1GSBE0001', 'IRO3SARZ0001', 'IRO7KIVP0001',
           'IRO7ZNGP0001', 'IRO1GMRO0001', 'IRO7REFP0001', 'IRO1FRIS0001', 'IRO1DSIN0001', 'IRO1GHND0001',
           'IRO1SHZG0001', 'IRO1SSEP0001', 'IRO1TAZB0001', 'IRO7LKPP0001', 'IRO1EXIR0001', 'IRO1BARZ0001',
           'IRO1DTIP0001', 'IRO1KRTI0001', 'IRO1RENA0001', 'IRO1MSKN0001', 'IRO1PRDZ0001', 'IRO1PABD0001',
           'IRO1SURO0001', 'IRO1BMLT0001', 'IRO7VSHP0001', 'IRO7FNRP0001', 'IRO1NGFO0001', 'IRO1MARK0001',
           'IRO1SAHD0001', 'IRO1KHFZ0001', 'IRO1SPTA0001', 'IRO7KAFP0001', 'IRO1SPPE0001', 'IRO7GHMP0001',
           'IRO1SPAH0001', 'IRO1SEIL0001', 'IRO1CHML0001', 'IRO7SHEP0001', 'IRO1SEPP0001', 'IRO3CGRZ0001',
           'IRO7SHIP0001', 'IRO1LAMI0001', 'IRO1SHGN0001', 'IRO7AZMP0001', 'IRO3NPSZ0001', 'IRO3ETKZ0001',
           'IRO1TOKA0001', 'IRO7LSDP0001', 'IRO1GTSH0001', 'IRO3TUKZ0001', 'IRO7THSP0001', 'IRO1MRGN0001',
           'IRO1SSAP0001', 'IRO7BNDP0001', 'IRO1SDOR0001', 'IRO7CKHP0001', 'IRO3MNOZ0001', 'IRO7FAHP0001',
           'IRO1GSHI0001', 'IRO1INFO0001', 'IRO1MAPN0001', 'IRO1MNMH0001', 'IRO1DMVN0001', 'IRO1VSIN0001',
           'IRO1SSNR0001', 'IRO1SRMA0001', 'IRO3NOLZ0001', 'IRO1PLKK0001', 'IRO1PAKS0001', 'IRO1PLAK0001',
           'IRO1TSRZ0001', 'IRO7KMOP0001', 'IRO1KHOC0001', 'IRO1SHFS0001', 'IRO1SHKR0001', 'IRO7PLSP0001',
           'IRO1SMAZ0001', 'IRO1NKOL0001', 'IRO1LIRZ0001', 'IRO1SISH0001', 'IRO1TSBE0001', 'IRO3ASPZ0001',
           'IRO1GBEH0001', 'IRO1IDOC0001', 'IRO1KVRZ0001', 'IRO1SGAZ0001', 'IRO1ROOI0001', 'IRO3TORZ0001',
           'IRO3TKMZ0001', 'IRO1PNTB0001', 'IRO3TBSZ0001', 'IRO1JOSH0001', 'IRO7SFSP0001', 'IRO7HPKP0001',
           'IRO1ABDI0001', 'IRO1SKOR0001', 'IRO1SBEH0001', 'IRO1SPDZ0001', 'IRO1SFNO0001', 'IRO1KHSH0001',
           'IRO1SFKZ0001', 'IRO1MOTJ0001', 'IRO1BROJ0001', 'IRO1ATIR0001', 'IRO1GHEG0001', 'IRO7SOLP0001',
           'IRO1NPRS0001', 'IRO7FLTP0001', 'IRO3TPSZ0001', 'IRO1LAPS0001', 'IRO1SLMN0001', 'IRO1TAIR0001',
           'IRO1LPAK0001', 'IRO1PELC0001', 'IRO1NAFT0001', 'IRO3PGPZ0001', 'IRO3BMAZ0001', 'IRO1SDST0001',
           'IRO1MRIN0001', 'IRO3OSHZ0001', 'IRO3PMTZ0001', 'IRO3BDMZ0001', 'IRO1ASAL0001', 'IRO3DSNZ0001',
           'IRO1NIRO0001', 'IRO7SDIP0001', 'IRO1BVMA0001', 'IRO7MINP0001', 'IRO1BDAN0001', 'IRO1APPE0001',
           'IRO1PFAN0001', 'IRO1BOTA0001', 'IRO1BMPS0001', 'IRO1SDAB0001', 'IRO1ARDK0001', 'IRO1DABO0001',
           'IRO1KHAZ0001', 'IRO7PKBP0001', 'IRO1SSOF0001', 'IRO3IMFZ0001', 'IRO1CRBN0001', 'IRO1BALB0001',
           'IRO1KIMI0001', 'IRO1DARO0001', 'IRO1KPRS0001', 'IRO7NEOP0001', 'IRO1TBAS0001', 'IRO3KHMZ0001',
           'IRO1SKAZ0001', 'IRO1HFRS0001', 'IRO1AYEG0001', 'IRO1KRAF0001', 'IRO3DZLZ0001', 'IRO1LZIN0001',
           'IRO7TOPP0001', 'IRO1MINO0001', 'IRO1LSMD0001', 'IRO1IRDR0001', 'IRO3ZOBZ0001', 'IRO1PJMZ0001',
           'IRO1TMVD0001', 'IRO3GDSZ0001', 'IRO1SKHS0001', 'IRO1TGOS0001', 'IRO1FTIR0001', 'IRO7JSHP0001',
           'IRO1NMOH0001', 'IRO1MAVA0001', 'IRO1NILO0001', 'IRO7TPOP0001', 'IRO7BSAP0001', 'IRO1MNSR0001',
           'IRO1BENN0001', 'IRO1PIAZ0001', 'IRO1KLBR0001', 'IRO1STEH0001', 'IRO1SKBV0001', 'IRO1LEAB0001',
           'IRO3BIPZ0001']

filters = [
    {
        "benchmark": [0, 18, 25, 50, 75, 100, 200, 300],
        "target": [
            {'ratio_roe': 'ROE'},
            {'ratio_roa': 'ROA'},
            {'ratio_gross_profit_margin': 'حاشيه سود ناخالص'},
            {'ratio_profit_margin': 'حاشيه سود خالص'}
        ]
    },
    {
        "benchmark": [20, 40, 50, 60, 80],
        'target': [
            {'ratio_da': 'D/A'}
        ]
    },

    {
        'benchmark': [0.25, 0.5, 1, 2, 4, ],
        'target': [
            {'ratio_de': 'D/E'}
        ]
    },

    {
        'benchmark': [0.1, 0, 5, 1, 1.25, 1.5, 1, 2],
        'target': [
            {'ratio_current_ratio': 'نسبت جاري'},
            {'ratio_quick_ratio': 'نسبت آني'}
        ]
    },

    {
        'benchmark': [0.1, 0, 25, 0.5, 0, 75, 0.9],
        'target': [
            {'ratio_cash_ratio': 'نسبت نقد'}
        ]
    },

    {
        'benchmark': [0.1, 0, 25, 0.5, 0, 75, 0.9],
        'target': [
            {'ratio_cash_ratio': 'نسبت نقد'}
        ]
    },

    {
        'benchmark': [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 20, 40, 80, 100],
        'target': [
            {'ratio_pe': 'P/E'}
        ]
    }
]

Balance_sheet = {'سرمایه گذاری کوتاه مدت': 'short_term_investments', 'دارایی': 'total_assets',
                 'حقوق صاحبان سهام': 'equity', 'حساب دریافتنی': 'net_receivables',
                 'دارایی جاری': 'total_current_assets', 'وجه نقد': 'cash', 'سرمایه': 'capital',
                 'بدهی جاری': 'total_current_liabilities', 'سود انباشته': 'retained_earnings',
                 'سرمایه گذاری بلند مدت': 'long_term_investments', 'موجودی کالا': 'inventory',
                 'پیش  پرداخت': 'prepayment', 'دارایی نامشهود': 'intangible_assets',
                 'دارایی ثابت': 'property_plant_and_equipment', 'بدهی': 'total_liabilities',
                 'حساب پرداختنی': 'accounts_payable'}
income = {'سود ناخالص': 'gross_profit', 'سود عملیاتی': 'operating_income_or_loss', 'سود قبل مالیات': 'income_before_tax',
         'فروش': 'total_income', 'سود خالص': 'net_income', 'هزینه مالی': 'interest_expense'}
Ratio = {'بازده دارایی (درصد)': 'roa', 'دوره گردش حساب دریافتنی (روز)': 'accounts_receivable_turnover_ratio',
          'دوره گردش حساب پرداختنی (روز)': 'accounts_payable_turnover_ratio', 'نقد': 'cash_ratio',
          'جاری': 'current_ratio', 'بدهی(درصد)': 'da', 'بازده ح ص س (درصد)': 'roe',
          'حاشیه سود خالص (درصد)': 'profit_margin', 'هزینه بهره به سود عملیاتی (درصد)': 'r_ebit',
          'دوره گردش موجودی کالا(روز)': 'inventory_turnover_ratio',
          'سود عملیاتی به سود ناخالص(درصد)': 'ebit_gross_profit', 'گردش دارای(بار)': 'sa', 'آنی': 'quick_ratio',
          'حاشیه سود ناخالص (درصد)': 'gross_profit_margin', 'بدهی به ح ص س': 'de'}

filters_data = [
    {
        'kind': 'fundamental',
        'filters':[
            {
                'benchmark': [0.1, 0, 25, 0.5, 0, 75, 0.9],
                'target': [
                    {'ratio__cash_ratio': 'نسبت نقد'}
                ]
            },
            ################################
            {
                "benchmark": [0, 18, 25, 50, 75, 100, 200, 300],
                "target": [
                    {'ratio__roe': 'ROE'}
                ]
            },
            ################################
            {
                "benchmark": [20, 40, 50, 60, 80],
                'target': [
                    {'ratio__da': 'D/A'}
                ]
            },
            ################################
            {
                "benchmark": [0, 18, 25, 50, 75, 90],
                "target": [
                    {'ratio__profit_margin': 'حاشيه سود خالص'}
                ]
            },
            ################################
            {
                'benchmark': [0.1, 0, 5, 1, 1.25, 1.5, 1, 2],
                'target': [
                    {'ratio__quick_ratio': 'نسبت آني'}
                ]
            },

            ################################
            {
                "benchmark": [0, 18, 25, 50, 75, 100, 200, 300],
                "target": [
                    {'ratio__roa': 'ROA'}
                ]
            },

            ################################
            {
                'benchmark': [0.25, 0.5, 1, 2, 4,],
                'target': [
                    {'ratio__de': 'D/E'}
                ]
            },
            ################################
            {
                "benchmark": [0, 18, 25, 50, 75, 90],
                "target": [
                    {'ratio__gross_profit_margin': 'حاشيه سود ناخالص'}
                ]
            },
            ################################
            {
                'benchmark': [0.1, 0, 5, 1, 1.25, 1.5, 1, 2],
                'target': [
                    {'ratio__current_ratio': 'نسبت جاري'}
                ]
            },
            ################################
            {
                'benchmark': [10, 30, 50, 70, 90],
                'target': [
                    {'ratio__ebit_gross_profit': 'سود عملیاتی به سود ناخالص'}
                ]
            },
            ################################
            {
                'benchmark': [10, 30, 50, 70, 90],
                'target': [
                    {'ratio__r_ebit': 'هزینه بهره به سود عملیاتی'}
                ]
            },
            ################################
            {
                'benchmark': [10*1000000, 30*1000000, 50*1000000, 100*1000000, 200*1000000],
                'target': [
                    {'balanceSheet__total_current_liabilities': '<span>بدهی جاری<br>(میلیون ریال)</span>'}
                ]
            },
        ]
    },
    {
        'kind': 'stockwatch',
        'filters': [
            {
                ################################
                'benchmark': [25, 50, 75],
                'target': [

                    {'stockWatch__BuyIndividualVolumePercentage': 'درصد حجم خرید حقیقی'}

                ]
            },
            ################################
            {
                'benchmark': [25, 50, 75],
                'target': [

                    {'stockWatch__SellIndividualVolumePercentage': 'درصد حجم فروش حقیقی'}
                ]
            },
            ################################
            {
                'benchmark': [1000000, 5000000, 10000000],
                'target': [
                    {'stockWatch__TotalNumberOfSharesTraded': 'حجم معاملات'}
                ]
            },
            ################################

            {
                'benchmark': [10, 100000, 500000, 1000000, 5000000],
                'target': [
                    {'stockWatch__BaseQuantity': 'حجم مبنا'},
                ]
            },
            ################################
            {
                'benchmark': [25, 50, 75],
                'target': [
                    {'stockWatch__BuyFirmVolumePercentage': 'درصد حجم خرید حقوقی'}
                ]
            },
            ################################
            {
                'benchmark': [25, 50, 75],
                'target': [
                    {'stockWatch__SellFirmVolumePercentage': 'درصد حجم فروش حقوقی'}
                ]
            },
            ################################
            {
                'benchmark': [-2000, -1000, 0, 200, 500, 1000, 2000],
                'target': [
                    {'stockWatch__Eps': 'EPS'}
                ]
            },
            ################################
            {
                'benchmark': [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 20, 40, 80, 100],
                'target': [
                    {'stockWatch__PricePerEarning': 'P/E'}
                ]
            },

            ################################
            {
                'benchmark': [-4, -3, -2, -1, 0, 1, 2, 3, 4],
                'target': [
                    {'stockWatch__ClosingPriceVariationPercent': 'درصد تغییر قیمت پایانی'}
                ]
            },

            ################################
            {
                'benchmark': [-4, -3, -2, -1, 0, 1, 2, 3, 4],
                'target': [
                    {'stockWatch__ReferencePriceVariationPercent': 'درصد تغییر آخرین معامله'}
                ]
            },
            ################################
            {
                'benchmark': [0, 100, 200, 500, 1000, 2000],
                'target': [
                    {'stockWatch__TotalNumberOfTrades': 'تعداد معاملات'}
                ]
            },
            ################################
            {
                'benchmark': [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 20, 40, 80, 100],
                'target': [
                    {'stockWatch__PricePerEarningGroup': 'P/E گروه'}
                ]
            },
        ]
    },
]
