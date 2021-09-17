import pandas as pd
import json
import geopandas as gpd

files = [
    "./data/dataPrep/Boston Elections - 1st Suffolk State Senate District Primary 2013.csv",
    "./data/dataPrep/Boston Elections - 2nd Suffolk State Senate District Primary 2008.csv",
    "./data/dataPrep/Boston Elections - 7th Congressional District Primary 2018.csv",
    "./data/dataPrep/Boston Elections - 11th Suffolk State House District Primary 2016.csv",
    "./data/dataPrep/Boston Elections - 11th Suffolk State House District Primary 2018.csv",
    "./data/dataPrep/Boston Elections - 12th Suffolk State House District Primary 2016.csv",
    "./data/dataPrep/Boston Elections - 12th Suffolk State House District Primary 2018.csv",
    "./data/dataPrep/Boston Elections - 14th Suffolk State House District Primary 2018.csv",
    "./data/dataPrep/Boston Elections - Mayor's Election 2017.csv"
]

df = pd.DataFrame(columns=["MATCH"])
for f in files:
    elect = pd.read_csv(f)
    df = pd.merge(elect,df, on="MATCH", how="outer")

cmap = {
    "MAY17_Jackson": "BOSMAY17G_TJackson",
    'MAY17_Walsh': "BOSMAY17G_MWalsh",
    'SH18_SIdowu': "SH18P_Suff14_SIdowu",
    'SH18_AScaccia': "SH18P_Suff14_AScaccia",
    'SH18_DCullinane': "SH18P_Suff12_DCullinane",
    'SH18_JLacet': "SH18P_Suff12_JLacet",
    'SH16_DCullinane': "SH16P_Suff12_DCullinane",
    'SH16_JLacet': "SH16P_Suff12_JLacet",
    'SH18_EMalia': "SH18P_Suff11_EMalia",
    'SH18_CClemonsMuhammad': "SH18P_Suff11_CClemons",
    'CONG18_APressley': "USH18P_7_APressley",
    'CONG18_MCapuano': "USH18P_7_MCapuano",
    'SS08_SChangDiaz': "SS08P_Suff2_SChangDiaz",
    'SS08DWilkerson': "SS08P_Suff2_DWilkerson",
    'SS13_LForry': "SS13P_Suff1_LForry",
    'SS13_NCollins': "SS13P_Suff1_NCollins",
    "MATCH": "NAMELSAD"
}

df = df.rename(cmap, axis=1)
df = df[list(cmap.values())]

def rename(name):
    if "Boston" in name:
        ward = name.split("Ward ")[-1].split(" Precinct")[0]
        precinct = name.split("Precinct ")[-1]
        return ward.zfill(2) + precinct.zfill(2)
    return name.replace("Randoplh", "Randolph")

df["NAMELSAD20"] = df["NAMELSAD"].apply(rename)

# ma_full = gpd.read_file("/Users/jnmatthews/MGGG/VRA-data-products/Massachusetts/shapes/MA_pcts.shp")

# ma_cvap = gpd.read_file("/Users/jnmatthews/MGGG/districtr-serverless/VRAEffectiveness/src/VRAEffectiveness/resources/massachusetts.csv")

# cvaps = ["CVAP{}".format(year) for year in [14,16,17,18]]
# bcvaps = ["BCVAP{}".format(year) for year in [14,16,17,18]]
df.to_csv("./massachusetts-something.csv", index=False)
#
"""
df = pd.read_csv("../localElectionDetails/resources/massachusetts.csv")

ma_full[["NAME", "TOTPOP", "VAP",]]

ma_pop = pd.merge(df, ma_full[["NAME", "TOTPOP"]], on="NAME", how="outer")


ma_pop = pd.merge(ma_full[["NAME", "TOTPOP"]], ma_cvap[["NAME"] + cvaps + bcvaps], on="NAME", how="outer")

pd.merge(df, ma_pop, on="NAME", how="outer").to_csv("../localElectionDetails/resources/massachusetts.csv", index=False)

ma_full[["NAME", "VAP", "BVAP"]].rename(columns={"VAP": "VAP10", "BVAP": "BVAP10"})

pd.merge(df, ma_full[["NAME", "VAP", "BVAP"]], on="NAME", how="outer").to_csv("../localElectionDetails/resources/massachusetts.csv", index=False)

df = pd.read_csv("../localElectionDetails/resources/massachusetts.csv")

df_old = pd.read_csv("../localElectionDetails/resources/massachusetts_old.csv")

# df_old[["NAME", "TOTPOP"]]

# pd.merge(df, df_old[["NAME", "TOTPOP"]], on="NAME").drop(columns=["Unnamed: 0"]).to_csv("../localElectionDetails/resources/massachusetts.csv", index=False)

cols = ["NAME", "TOTPOP","VAP10","HVAP10","WVAP10","BVAP10","AMINVAP10","ASIANVAP10","NHPIVAP10","OTHERVAP10","2MOREVAP10"]

df = df.drop(columns=[c for c in df.columns if "CVAP" in c])

df_cvap = df_old[["NAME"] + [c for c in df_old.columns if "CVAP" in c]]

pd.merge(df, df_cvap, on="NAME").to_csv("../localElectionDetails/resources/massachusetts.csv", index=False)



df = pd.read_csv("~/Downloads/WI25.csv", header=0)

df["assignment"] = df["assignment"].apply(lambda x: x+1)

df.to_csv("~/Downloads/WI25.csv", index=False)
"""