import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()
# c.execute('''
# create table data(msisdn,Mastermsisdn,accounteventid,serviceclassid,vouchergroupid,transactiondatetime,transactionAmount,balancemainbeforerefill,balancemainafterrefill,amountmain,actualtalktime,originoperatorid,nodeid,organizationid,currency,paymenttransactionid,externaldata1,externaldata2,externaldata3,externaldata4,servicefeeexpirydatebefore,servicefeeexpirydateafter,supervisionexpirydatebefore,supervisionexpirydateafter,activationdate,welcomeStatus,ServiceOfferingbefore,ServiceOfferingafter,CommunityId1Before,CommunityId2Before,CommunityId3Before,CommunityId1After,CommunityId2After,CommunityId3After,Locationnumber,Offeridbefore,OfferStartDateBefore,OfferExpiryDateBefore,Offeridafter,OfferStartDateafter,OfferExpiryDateafter,TDFValiditysupervision,TDFValidityservicefee,TDFSRCValidity,temporaryServiceClassBefore,temporaryServiceClassAfter,originHostName,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10)''')

c.execute('''.import 05_KOL_BH_PYMT_STATIC_20200819.txt data''')