class market:
    def __init__(self,market,symbols = []):

        def get_symbols(market):

            all_symbols = {

                        "ninja" : ["BTC-USD"],

                        "nasdaq" : [ "KFS","MPW","FCFS","ICLR","CVCY","WHLRP","BGB","HTGC","DPG","GWB","JMM","NX","EFSC","ERIC","A","ANET","BCS",
                                    "CM","CSL","DNB","EME","GOF","IDA","KBH","MQY","NVS","PGRE","PHG","IROQ","CSCO","CTSH","EWBC","IROQ","JOUT",
                                    "SEAC","CB","COF","CRH","DRI","GF","GLF","KNL","LII","NEP","NGG","PFN","RMD","RPT","SLF","SMG","BLDR","COST",
                                    "GRMN","LOPE","NVAX","AIZ","APO","ARCO","BDJ","DB","DHI","FMC","GRA","HD","PM","ROG","RPAI","RYN","SCCO","SEM",
                                    "CDZI","WINA","MTX","NCT","PHX" ],

                        "nyse" : [  "A","AA","AA$B","AAC","AAN","AAP","AAT","AAV","AB","ABB","ABBV","ABC","ABEV","ABG","ABM","ABR","ABR$A","ABR$B",
                                  "ABR$C","ABRN","ABT","ABX","ACC","ACCO","ACE","ACG","ACH","ACI","ACM","ACMP","ACN","ACP","ACRE","ACT","ACW","ADC",
                                  "ADM","ADPT","ADS","ADT","ADX","AEB","AEC","AED","AEE","AEG","AEH","AEK","AEL","AEM","AEO","AEP","AER","AES","AES$C",
                                  "AET","AF","AF$C","AFA","AFB","AFC","AFG","AFGE","AFL","AFM","AFQ","AFSD","AFSI$A","AFSI$B","AFSI$C","AFT","AFW","AG",
                                  "AGC","AGCO","AGD","AGI","AGM","AGM$A","AGM$B","AGM$C","AGM.A","AGN","AGO","AGO$B","AGO$E","AGO$F","AGRO","AGU","AGX",
                                  "AHC","AHH","AHL","AHL$A","AHL$B","AHL$C","AHP","AHS","AHT" ],

                       "world_indice" : [ "^GSPC","^DJI","^IXIC","^NYA","^XAX","^BUK100P","^RUT","^VIX","^FTSE","^GDAXI","^FCHI","^STOXX50E","^N100",
                                         "^BFX","IMOEX.ME","^N225","^HSI","000001.SS","399001.SZ","^STI","^AXJO","^AORD","^BSESN","^JKSE","^KLSE","^NZ50",
                                         "^KS11","^TWII","^GSPTSE","^BVSP","^MXX","^IPSA","^MERV","^TA125.TA","^CASE30","^JN0U.JO" ],

                       "forex" : [ "EURUSD=X","JPY=X","GBPUSD=X","AUDUSD=X","NZDUSD=X","EURJPY=X","GBPJPY=X","EURGBP=X","EURCAD=X",
                                  "EURSEK=X","EURCHF=X","EURHUF=X","EURJPY=X","CNY=X","HKD=X","SGD=X","INR=X","MXN=X","PHP=X","IDR=X","THB=X","MYR=X",
                                  "ZAR=X","RUB=X" ],

                        "crypto" : ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'USDT-USD', 'DOT1-USD', 'DOT2-USD', 'XRP-USD', 'LTC-USD', 'LINK-USD',
                                    'BCH-USD', 'USDC-USD', 'XLM-USD', 'LUNA1-USD', 'THETA-USD', 'DOGE-USD', 'VET-USD', 'ATOM1-USD', 'TRX-USD', 'AVAX-USD',
                                    'EOS-USD', 'XMR-USD', 'MIOTA-USD', 'CTC1-USD', 'BSV-USD', 'SOL1-USD', 'ATOM2-USD', 'SOL2-USD', 'XTZ-USD', 'XEM-USD',
                                    'ALGO-USD', 'KSM-USD', 'NEO-USD', 'HBAR-USD', 'LUNA2-USD', 'EGLD-USD', 'DASH-USD', 'DCR-USD', 'ZIL-USD', 'CTC2-USD',
                                    'CTC3-USD', 'ZEC-USD', 'RVN-USD', 'BAT-USD', 'TFUEL-USD', 'CCXX-USD', 'ETC-USD', 'BNT-USD', 'DFI-USD', 'STX1-USD',
                                    'XWC-USD', 'CEL-USD', 'ICX-USD', 'SC-USD', 'ZRX-USD', 'WAVES-USD', 'DGB-USD', 'ONE2-USD', 'VGX-USD', 'ONT-USD', 'IOST-USD',
                                    'OMG-USD', 'CELO-USD', 'STX2-USD', 'LRC-USD', 'AR-USD', 'NANO-USD', 'QTUM-USD', 'ZEN-USD', 'HNT1-USD', 'KNC-USD', 'BTG-USD',
                                    'XVG-USD', 'LSK-USD', 'EWT-USD', 'CKB-USD', 'GLM-USD', 'ETN-USD', 'IOTX-USD', 'XDC-USD', 'FUN-USD', 'SNT-USD', 'REP-USD',
                                    'WAXP-USD', 'MAID-USD', 'COTI-USD', 'CVC-USD', 'ANT-USD', 'ARDR-USD', 'HNT2-USD', 'META-USD', 'SRM-USD', 'ONE3-USD',
                                    'KIN-USD', 'MED-USD', 'ONE1-USD', 'BTS-USD', 'STORJ-USD', 'IRIS-USD', 'KMD-USD', 'GNO-USD', 'STEEM-USD', 'BCD-USD',
                                    'VLX-USD', 'WAN-USD', 'DNT-USD', 'STRAX-USD', 'ARK-USD', 'TOMO-USD', 'SYS-USD', 'RLC-USD', 'TT-USD', 'XHV-USD', 'HIVE-USD',
                                    'PAC-USD', 'BTM-USD', 'PHA-USD', 'MWC-USD', 'HNC-USD', 'PPT-USD', 'DIVI-USD', 'NYE-USD', 'WOZX-USD', 'SAPP-USD', 'ADX-USD',
                                    'ABBC-USD', 'RDD-USD', 'ATRI-USD', 'AION-USD', 'GRN-USD', 'ZNN-USD', 'LBC-USD', 'MLN-USD', 'MONA-USD', 'GAS-USD', 'HNS-USD',
                                    'MASS-USD', 'WTC-USD', 'NKN-USD', 'NRG-USD', 'XNC-USD', 'MTC3-USD', 'NXS-USD', 'MTL-USD', 'PCX-USD', 'BEAM-USD', 'NIM-USD',
                                    'FIRO-USD', 'JUL-USD', 'ELA-USD', 'LOKI-USD', 'REV-USD', 'BCN-USD', 'WICC-USD', 'NULS-USD', 'DAG-USD', 'PIVX-USD',
                                    'AXEL-USD', 'CNX-USD', 'GNT-USD', 'FSN-USD', 'BDX-USD', 'MTC1-USD', 'CTXC-USD', 'OBSR-USD', 'VITAE-USD', 'VSYS-USD',
                                    'MARO-USD', 'FIO-USD', 'VRA-USD', 'AE-USD', 'NAV-USD', 'EMC2-USD', 'CRU-USD', 'GO-USD', 'ARRR-USD', 'GRS-USD', 'ERG-USD',
                                    'KDA-USD', 'GXC-USD', 'XSN-USD', 'HC-USD', 'MCO-USD', 'NAS-USD', 'DMCH-USD', 'SKY-USD', 'VITE-USD', 'XZC-USD', 'NXT-USD',
                                    'CSC-USD', 'SBD-USD', 'NEBL-USD', 'XLT-USD', 'KRT-USD', 'APL-USD', 'BIP-USD', 'AMB-USD', 'SERO-USD', 'PAI-USD', 'STRAT-USD',
                                    'PAY-USD', 'GRIN-USD', 'VTC-USD', 'MHC-USD', 'DGD-USD', 'RBTC-USD', 'VERI-USD', 'ADK-USD', 'PI-USD', 'BLOCK-USD',
                                    'RINGX-USD', 'GAME-USD', 'QASH-USD', 'CUT-USD', 'DCN-USD', 'DERO-USD', 'POA-USD', 'GBYTE-USD', 'DYN-USD', 'DNA1-USD',
                                    'HPB-USD', 'LYNX-USD', 'CMT1-USD', 'SALT-USD', 'BHD-USD', 'QRL-USD', 'NMC-USD', 'FCT-USD', 'TRUE-USD', 'MAN-USD', 'NIX-USD',
                                    'BTC2-USD', 'XRC-USD', 'ETP-USD', 'VIA-USD', 'GLEEC-USD', 'XDN-USD', 'SFT-USD', 'UBQ-USD', 'DNA2-USD', 'YOYOW-USD',
                                    'NVT-USD', 'ZEL-USD', 'ACT-USD', 'CET-USD', 'PZM-USD', 'AYA-USD', 'SNGLS-USD', 'ZANO-USD', 'SNM-USD', 'ACH-USD', 'PPC-USD',
                                    'PHR-USD', 'BHP-USD', 'BPS-USD', 'PLC-USD', 'VAL1-USD', 'TERA-USD', 'FLO-USD', 'SMART-USD', 'CTC-USD', 'CHI-USD',
                                    'SCC1-USD', 'CMT2-USD', 'SCC5-USD', 'ZYN-USD', 'FO-USD', 'BURST-USD', 'PART-USD', 'SCC2-USD', 'SCC4-USD', 'AEON-USD',
                                    'VAL2-USD', 'FTC-USD', 'WINGS-USD', 'XMY-USD', 'SCP-USD', 'MBC-USD', 'HTDF-USD', 'NLG-USD', 'GHOST1-USD', 'IDNA-USD',
                                    'TAAS-USD', 'MOON-USD', 'HTML-USD', 'XST-USD', 'LCC-USD', 'VEX-USD', 'INSTAR-USD', 'ILC-USD', 'INT-USD', 'FAIR-USD',
                                    'NYZO-USD', 'OTO-USD', 'MIR-USD', 'DTEP-USD', 'GRC-USD', 'SUB-USD', 'CRW-USD', 'BLK-USD', 'BLK-USD', 'VIN-USD',
                                    'PMEER-USD', 'BPC-USD', 'OWC-USD', 'USNBT-USD', 'RADS-USD', 'DIME-USD', 'CURE-USD', 'IOC-USD', 'MGO-USD', 'GHOST-USD',
                                    'HYC-USD', 'ZVC-USD', 'SONO2-USD', 'GCC2-USD', 'XAS-USD', 'GHOST2-USD', 'GCC1-USD', 'QRK-USD', 'XBY-USD', 'SONO1-USD',
                                    'ERK-USD', 'CPS-USD', 'XMC-USD', 'BCA-USD', 'DDK-USD', 'EDG-USD', 'NPC-USD', 'OURO-USD', 'HSS-USD', 'DEV-USD', 'FRST-USD',
                                    'ATB-USD', 'COMP1-USD', 'COMP2-USD', 'EDC-USD', 'NLC2-USD', 'MOAC-USD', 'ECC-USD', 'BONO-USD', 'ECA-USD', 'UNO-USD',
                                    'COLX-USD', 'LKK-USD', 'CLAM-USD', 'ALIAS-USD', 'FLASH-USD', 'TUBE-USD', 'RBY-USD', 'SCC3-USD', 'AIB-USD', 'WGR-USD',
                                    'MINT-USD', 'XUC-USD', 'DUN-USD', 'MRX-USD', 'RSTR-USD', 'XNS2-USD', 'XNS1-USD', 'SHIFT-USD', 'JDC-USD', 'MTC2-USD',
                                    'CCA-USD', 'MIDAS-USD', 'SLS-USD', 'DCY-USD', 'XCP-USD', 'BTX-USD', 'LRG-USD', 'DMD-USD', 'BRC-USD', 'XLQ-USD',
                                    'YEP-USD', 'VBK-USD', 'BST-USD'],


                        "mutual_fund" : ['KMKNX', 'HSSIX', 'HSSAX', 'HSSCX', 'FFBFX', 'BFOCX', 'INPSX', 'INPIX', 'TEFQX', 'MINDX', 'MIDNX', 'FBIOX',
                                         'RYOIX', 'FCCGX', 'FCTGX', 'ENTIX', 'FCIGX', 'FIDGX', 'FCAGX', 'DHMCX', 'SCATX', 'WAAEX', 'FBTIX', 'PRLAX',
                                         'FBTAX', 'FBTTX', 'LGIIX', 'ASMOX', 'INDIX', 'BCSIX', 'BCSSX', 'FFGRX', 'NWSAX', 'LMIYX', 'FSRPX', 'AGOZX',
                                         'ILLLX', 'HSPGX', 'BIPSX', 'QISGX', 'BIPIX', 'HSPCX', 'QASGX', 'QCSGX', 'QLSGX', 'PRHSX', 'THISX', 'JSMVX',
                                         'FSELX', 'FBTAX', 'FBTTX', 'LGIIX', 'ASMOX', 'INDIX', 'BCSIX', 'BCSSX', 'FFGRX', 'NWSAX', 'LMIYX', 'FSRPX',
                                         'AGOZX', 'ILLLX', 'HSPGX', 'BIPSX', 'QISGX', 'BIPIX', 'HSPCX', 'QASGX', 'QCSGX', 'QLSGX', 'PRHSX', 'THISX',
                                         'JSMVX', 'FSELX', 'JSMTX', 'DCGTX', 'CYPIX', 'FJSCX'],

                        "comodities" : ['ES=F', 'YM=F', 'NQ=F', 'RTY=F', 'ZB=F', 'ZN=F', 'ZF=F', 'ZT=F', 'GC=F', 'MGC=F', 'SI=F', 'SIL=F', 'PL=F',
                                        'HG=F', 'PA=F', 'CL=F', 'HO=F', 'NG=F', 'RB=F', 'BZ=F', 'B0=F', 'ZC=F', 'ZO=F', 'KE=F', 'ZR=F', 'ZM=F', 'ZL=F',
                                        'ZS=F', 'GF=F', 'HE=F', 'LE=F', 'CC=F', 'KC=F', 'CT=F', 'LB=F', 'OJ=F', 'SB=F']

                    }

            return all_symbols[market]
        if symbols == [] :
            self.symbols = get_symbols(market)
        if symbols != [] :
            self.symbols = symbols



if __name__ == "__main__" :
    print(market('nasdaq').symbols)
