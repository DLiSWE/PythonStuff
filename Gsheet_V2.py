import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import datetime
import tkinter as tk
from tkinter import simpledialog
from tkinter import *

class MyDialog(simpledialog.Dialog):

    def body(self, master):

        Label(master, text = "Google Sheets Project Name").grid(row=0)
        Label(master, text = "Spreadsheet ID #").grid(row=1)
        Label(master, text = "UF Target ROAS").grid(row=2)
        Label(master, text = "MF Target ROAS").grid(row=3)
        Label(master, text = "BF Target ROAS").grid(row=4)
        Label(master, text = "Allocated Monthly Budget").grid(row=5)
        Label(master, text = "Days left in the month").grid(row=6)
        Label(master, text="Total days this month").grid(row=7)


        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e4 = Entry(master)
        self.e5 = Entry(master)
        self.e6 = Entry(master)
        self.e7 = Entry(master)
        self.e8 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)

        return self.e1

    def apply(self):

        GSHEET = self.e1.get()
        SSIDV = self.e2.get()
        UFTROAS = self.e3.get()
        MFTROAS = self.e4.get()
        BFTROAS = self.e5.get()
        AMB = self.e6.get()
        DLIM = self.e7.get()
        DIM =self.e8.get()

        self.tag = (GSHEET, SSIDV, UFTROAS, MFTROAS, BFTROAS, AMB, DLIM, DIM)
        self.tag1 = (GSHEET)
        self.tag2 = (SSIDV)
        self.tag3 = (UFTROAS)
        self.tag4 = (MFTROAS)
        self.tag5 = (BFTROAS)
        self.tag6 = (AMB)
        self.tag7 = (DLIM)
        self.tag8 = (DIM)

def gshtda():
    root = tk.Tk()
    root.withdraw()
    d = MyDialog(root)    

    GSHEETVAR = str(d.tag1)
    TSSIDV = str(d.tag2)
    TUFTROAS = int(d.tag3)
    TMFTROAS = int(d.tag4)
    TBFTROAS = int(d.tag5)
    AMB = int(d.tag6)
    TDLIM = int(d.tag7)
    TDIM = int(d.tag8)

#domain of grab (dont touch)
    scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']

    #service_account from Google API.
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
             "service_account.json", scope) # Your json file here

    #Get authorization token (dont touch)
    gc = gspread.authorize(credentials)

    #Choose Project up top's name
    wks = gc.open(GSHEETVAR).sheet1
    data = wks.get_all_values()
    headers = data.pop(0)
    ssid = TSSIDV
    wks_name = 'Transform'
    wks_name1 = 'Campaign UF'
    wks_name2 = 'Campaign MF'
    wks_name3 = 'Campaign BF'
    wks_name4 = 'Summary'

    #the cell you want the data to start with
    cell_of_start_df = 'B2'

    #Delete if you dont wanna see all the way down (dont touch)
    pd.set_option('display.max_rows', 300)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    #Create dataframe value
    df = pd.DataFrame(data, columns=headers)

    #change dtype for specific column (dont touch until explained)
    df['Campaign daily budget'] = pd.to_numeric(df['Campaign daily budget'], downcast='float')
    df['Cost'] = pd.to_numeric(df['Cost'], downcast='float')
    df['Return on ad spend (ROAS)'] = pd.to_numeric(df['Return on ad spend (ROAS)'], downcast='float')
    df['Website conversions'] = pd.to_numeric(df['Website conversions'], downcast='float')
    df['Impressions'] = pd.to_numeric(df['Impressions'], downcast='float')
    df['Unique outbound clicks'] = pd.to_numeric(df['Unique outbound clicks'], downcast='float')

    #add column for function (pretty basic)
    df['Campaign monthly budget'] = df['Campaign daily budget'] * TDIM
    df['Media Pacing'] = df['Cost'] / df['Campaign monthly budget']

    df['CPA'] = df['Cost'] / df['Website conversions']
    df['CPM (1000)'] = (df['Cost'] / df['Impressions']) * 1000
    df['CPC (all)'] = df['Cost'] / df['Unique outbound clicks']
    df['CTR'] = df['Unique outbound clicks'] / df['Impressions']

    UFROASP = TUFTROAS / df['Return on ad spend (ROAS)']
    MFROASP = TMFTROAS / df['Return on ad spend (ROAS)']
    BFROASP = TBFTROAS / df['Return on ad spend (ROAS)']

    df['ROAS Pacing'] = 0
    df.loc[(df['Campaign name'].str.startswith('UF'), 'ROAS Pacing')] = UFROASP.astype(float)
    df.loc[(df['Campaign name'].str.startswith('MF'), 'ROAS Pacing')] = MFROASP.astype(float)
    df.loc[(df['Campaign name'].str.startswith('BF'), 'ROAS Pacing')] = BFROASP.astype(float)

    #change dtype for new columns (dont touch until explained)
    df['Campaign monthly budget'] = pd.to_numeric(df['Campaign monthly budget'], downcast='float')
    df['CPA'] = pd.to_numeric(df['CPA'], downcast='float')
    df['CPM (1000)'] = pd.to_numeric(df['CPM (1000)'], downcast='float')
    df['CPC (all)'] = pd.to_numeric(df['CPC (all)'], downcast='float')
    df['CTR'] = pd.to_numeric(df['CTR'], downcast='float')

    #replace INF values with NaN (don't touch until explained)
    df = df.replace([np.inf], np.nan)

    #Sort Columns
    conditions = [df['Campaign name'].str.startswith('UF')]

    #groupby UF/MF/BF
    df2 = df[df['Campaign name'].str.startswith('UF')].copy(deep=True)
    df3 = df[df['Campaign name'].str.startswith('MF')].copy(deep=True)
    df4 = df[df['Campaign name'].str.startswith('BF')].copy(deep=True)

    #replace INF values with NaN (don't touch until explained)
    df2 = df2.replace([np.inf], np.nan)
    df3 = df3.replace([np.inf], np.nan)
    df4 = df4.replace([np.inf], np.nan)

    UF_Total = df2['Campaign daily budget'].sum()
    MF_Total = df3['Campaign daily budget'].sum()
    BF_Total = df4['Campaign daily budget'].sum()

    UF_MTotal = df2['Campaign monthly budget'].sum()
    MF_MTotal = df3['Campaign monthly budget'].sum()
    BF_MTotal = df4['Campaign monthly budget'].sum()

    UF_Spent = df2['Cost'].sum()
    MF_Spent = df3['Cost'].sum()
    BF_Spent = df4['Cost'].sum()

    UF_conversions = df2['Website conversions'].sum()
    MF_conversions = df3['Website conversions'].sum()
    BF_conversions = df4['Website conversions'].sum()

    UF_ROAS = df2['Return on ad spend (ROAS)'].mean()
    MF_ROAS = df3['Return on ad spend (ROAS)'].mean()
    BF_ROAS = df4['Return on ad spend (ROAS)'].mean()

    #date of script run
    rnow = datetime.datetime.now()

    prediction = ((UF_Total * TDLIM) + UF_Spent)
    prediction2 = ((MF_Total * TDLIM) + MF_Spent)
    prediction3 = ((BF_Total * TDLIM) + BF_Spent)

    RBUD = AMB - UF_Spent
    RBUD1 = RBUD - MF_Spent
    RBUD2 = RBUD1 - BF_Spent

    UFNDB = RBUD / TDLIM
    MFNDB = RBUD1 / TDLIM
    BFNDB = RBUD2 / TDLIM

    UFMP = df2['Cost'].sum() / AMB
    MFMP = df3['Cost'].sum() / AMB
    BFMP = df4['Cost'].sum() / AMB

    #create new page & insert variables listed above
    summary_sheet = {'Campaign daily total': [UF_Total, MF_Total, BF_Total],
    				'Campaign monthly total': [UF_MTotal, MF_MTotal, BF_MTotal],
    				'Spent': [UF_Spent, MF_Spent, BF_Spent],
    				'Website conversions': [UF_conversions, MF_conversions, BF_conversions],
    				'Estimated Spend for month': [prediction, prediction2, prediction3],
                    'Remaining Budget': [RBUD, RBUD1, RBUD2],
                    'New daily budget': [UFNDB, MFNDB, BFNDB],
    				'ROAS': [UF_ROAS, MF_ROAS, BF_ROAS],
                    'ROAS Pacing': [(df2['ROAS Pacing'].mean()), (df3['ROAS Pacing'].mean()), (df4['ROAS Pacing'].mean())],
                    'Adjusted Media Pacing': [UFMP , MFMP, BFMP],
    				'Date Run': [rnow, rnow, rnow]
    				}

    df5 = pd.DataFrame(summary_sheet, columns=['Campaign daily total','Campaign monthly total', 'Spent', 
    											'Website conversions', 'Estimated Spend for month', 'Remaining Budget',
                                                'New daily budget', 'ROAS', 'ROAS Pacing', 'Adjusted Media Pacing', 'Date Run'], 
    											index=['UF Totals', 'MF Totals', 'BF Totals'])

    #Create total columns for summary sheet
    df5.loc['Total', 'Campaign daily total'] = df5['Campaign daily total'].sum()
    df5.loc['Total', 'Campaign monthly total'] = df5['Campaign monthly total'].sum()
    df5.loc['Total', 'Spent'] = df5['Spent'].sum()
    df5.loc['Total', 'Website conversions'] = df5['Website conversions'].sum()
    df5.loc['Total', 'Estimated Spend for month'] = df5['Estimated Spend for month'].sum()
    df5.loc['Total', 'ROAS'] = df5['ROAS'].mean()
    df5.loc['Total', 'Remaining Budget'] = RBUD2
    df5.loc['Total', 'New daily budget'] = df5['New daily budget'].sum()
    df5.loc['Total', 'Adjusted Media Pacing'] = df5['Adjusted Media Pacing'].mean()
    df5.loc['Total', 'ROAS Pacing'] = df5['ROAS Pacing'].mean()
    df5['Date Run'] = df5['Date Run'].astype(object)

    #create total row in Transform, UF,MF,BF
    df.loc['Total', 'Campaign daily budget'] = df['Campaign daily budget'].sum()
    df.loc['Total', 'Cost'] = df['Cost'].sum()
    df.loc['Total', 'Campaign monthly budget'] = df['Campaign monthly budget'].sum()
    df.loc['Total', 'Website conversions'] = df['Website conversions'].sum()
    df.loc['Total', 'Impressions'] = df['Impressions'].sum()
    df.loc['Total', 'Return on ad spend (ROAS)'] = df['Return on ad spend (ROAS)'].mean()
    df.loc['Total', 'CPC (all)'] = df['Cost'].sum() / df['Unique outbound clicks'].sum()
    df.loc['Total', 'CPM (1000)'] = (df['Cost'].sum() / df['Impressions'].sum()) * 1000
    df.loc['Total', 'CTR'] = df['Unique outbound clicks'].sum() / df['Impressions'].sum()
    df.loc['Total', 'CPA'] = df['Cost'].sum() / df['Website conversions'].sum()
    df.loc['Total', 'Media Pacing'] = df['Media Pacing'].mean()
    df.loc['Total', 'ROAS Pacing'] = df['ROAS Pacing'].mean()
    df.loc['Total', 'Unique outbound clicks'] = df['Unique outbound clicks'].sum()

    df2.loc['Total', 'Campaign daily budget'] = df2['Campaign daily budget'].sum()
    df2.loc['Total', 'Cost'] = df2['Cost'].sum()
    df2.loc['Total', 'Campaign monthly budget'] = df2['Campaign monthly budget'].sum()
    df2.loc['Total', 'Website conversions'] = df2['Website conversions'].sum()
    df2.loc['Total', 'Impressions'] = df2['Impressions'].sum()
    df2.loc['Total', 'Return on ad spend (ROAS)'] = df2['Return on ad spend (ROAS)'].mean()
    df2.loc['Total', 'CPC (all)'] = df2['Cost'].sum() / df2['Unique outbound clicks'].sum()
    df2.loc['Total', 'CPM (1000)'] = (df2['Cost'].sum() / df2['Impressions'].sum()) * 1000
    df2.loc['Total', 'CTR'] = df2['Unique outbound clicks'].sum() / df2['Impressions'].sum()
    df2.loc['Total', 'CPA'] = df2['Cost'].sum() / df2['Website conversions'].sum()
    df2.loc['Total', 'Media Pacing'] = df2['Media Pacing'].mean()
    df2.loc['Total', 'ROAS Pacing'] = df2['ROAS Pacing'].mean()
    df2.loc['Total', 'Unique outbound clicks'] = df2['Unique outbound clicks'].sum()

    df3.loc['Total', 'Campaign daily budget'] = df3['Campaign daily budget'].sum()
    df3.loc['Total', 'Cost'] = df3['Cost'].sum()
    df3.loc['Total', 'Campaign monthly budget'] = df3['Campaign monthly budget'].sum()
    df3.loc['Total', 'Website conversions'] = df3['Website conversions'].sum()
    df3.loc['Total', 'Impressions'] = df3['Impressions'].sum()
    df3.loc['Total', 'Return on ad spend (ROAS)'] = df3['Return on ad spend (ROAS)'].mean()
    df3.loc['Total', 'CPC (all)'] = df3['Cost'].sum() / df3['Unique outbound clicks'].sum()
    df3.loc['Total', 'CPM (1000)'] = (df3['Cost'].sum() / df3['Impressions'].sum()) * 1000
    df3.loc['Total', 'CTR'] = df3['Unique outbound clicks'].sum() / df3['Impressions'].sum()
    df3.loc['Total', 'CPA'] = df3['Cost'].sum() / df3['Website conversions'].sum()
    df3.loc['Total', 'Media Pacing'] = df3['Media Pacing'].mean()
    df3.loc['Total', 'ROAS Pacing'] = df3['ROAS Pacing'].mean()
    df3.loc['Total', 'Unique outbound clicks'] = df3['Unique outbound clicks'].sum()

    df4.loc['Total', 'Campaign daily budget'] = df4['Campaign daily budget'].sum()
    df4.loc['Total', 'Cost'] = df4['Cost'].sum()
    df4.loc['Total', 'Campaign monthly budget'] = df4['Campaign monthly budget'].sum()
    df4.loc['Total', 'Website conversions'] = df4['Website conversions'].sum()
    df4.loc['Total', 'Impressions'] = df4['Impressions'].sum()
    df4.loc['Total', 'Return on ad spend (ROAS)'] = df4['Return on ad spend (ROAS)'].mean()
    df4.loc['Total', 'CPC (all)'] = df4['Cost'].sum() / df4['Unique outbound clicks'].sum()
    df4.loc['Total', 'CPM (1000)'] = (df4['Cost'].sum() / df4['Impressions'].sum()) * 1000
    df4.loc['Total', 'CTR'] = df['Unique outbound clicks'].sum() / df4['Impressions'].sum()
    df4.loc['Total', 'CPA'] = df4['Cost'].sum() / df4['Website conversions'].sum()
    df4.loc['Total', 'Media Pacing'] = df4['Media Pacing'].mean()
    df4.loc['Total', 'ROAS Pacing'] = df4['ROAS Pacing'].mean()
    df4.loc['Total', 'Unique outbound clicks'] = df4['Unique outbound clicks'].sum()

    #sort
    df = df[['Ad set start time', 'Campaign name', 'Campaign monthly budget', 'Campaign daily budget', 'Cost', 'Website conversions',
    'Return on ad spend (ROAS)', 'Impressions', 'CPM (1000)', 'Unique outbound clicks', 'CPC (all)', 'CTR', 'CPA', 'Media Pacing', 'ROAS Pacing']]

    df2 = df2[['Ad set start time', 'Campaign name', 'Campaign monthly budget', 'Campaign daily budget', 'Cost', 'Website conversions',
    'Return on ad spend (ROAS)', 'Impressions', 'CPM (1000)', 'Unique outbound clicks', 'CPC (all)', 'CTR', 'CPA', 'Media Pacing', 'ROAS Pacing']]

    df3 = df3[['Ad set start time', 'Campaign name', 'Campaign monthly budget', 'Campaign daily budget', 'Cost', 'Website conversions',
    'Return on ad spend (ROAS)', 'Impressions', 'CPM (1000)', 'Unique outbound clicks', 'CPC (all)', 'CTR', 'CPA', 'Media Pacing', 'ROAS Pacing']]

    df4 = df4[['Ad set start time', 'Campaign name', 'Campaign monthly budget', 'Campaign daily budget', 'Cost', 'Website conversions',
    'Return on ad spend (ROAS)', 'Impressions', 'CPM (1000)', 'Unique outbound clicks', 'CPC (all)', 'CTR', 'CPA', 'Media Pacing', 'ROAS Pacing']]

    d2g.upload(df,
        ssid,
        wks_name,
        credentials = credentials,
        col_names = True,
        row_names = True,
        start_cell = cell_of_start_df,
        clean = True)

    d2g.upload(df2,
        ssid,
        wks_name1,
        credentials = credentials,
        col_names = True,
        row_names = True,
        start_cell = cell_of_start_df,
        clean = True)

    d2g.upload(df3,
        ssid,
        wks_name2,
        credentials = credentials,
        col_names = True,
        row_names = True,
        start_cell = cell_of_start_df,
        clean = True)

    d2g.upload(df4,
        ssid,
        wks_name3,
        credentials = credentials,
        col_names = True,
        row_names = True,
        start_cell = cell_of_start_df,
        clean = True)

    d2g.upload(df5,
        ssid,
        wks_name4,
        credentials = credentials,
        col_names = True,
        row_names = True,
        start_cell = cell_of_start_df,
        clean = True)

#print dataframe (this is for development stage ^^^ up there sends the info to google sheets )






