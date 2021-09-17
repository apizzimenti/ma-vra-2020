
import pandas as pd

files=[
    "./data/raw_summaries/USH18P_3_LTrahan-DKoh-BLitalien-JMatias-RGifford-AChandler_WVAP-HVAP.csv",
    "./data/raw_summaries/SS18P_EssMidd2_BFinegold-PPayano-MArmano_WVAP-HVAP.csv",
    "./data/raw_summaries/SS14P_EssMidd2_BLitalien-PPayano-DRodriguez_WVAP-HVAP.csv",
    "./data/raw_summaries/2018_US_HOU_P_01_pressley-capuano_BVAP-HVAP.csv",
    "./data/raw_summaries/2017_BOS_MAY_G_01_walsh-jackson_BVAP-HVAP.csv",
    "./data/raw_summaries/2008_MA_SEN_P_01_chang_diaz-wilkerson_BVAP-HVAP.csv",
    "./data/raw_summaries/2013_MA_SEN_P_01_forry-collins-dahill_BVAP-HVAP.csv",
    "./data/raw_summaries/2018_MA_HOU_P_03_malia-turnbull-clemons_BVAP-HVAP.csv",
    "./data/raw_summaries/2018_MA_HOU_P_01_cullinane-lacet_BVAP-HVAP.csv",
    "./data/raw_summaries/2016_MA_HOU_P_01_cullinane-lacet_BVAP-HVAP.csv"
]

merged = pd.read_csv(files[0])

for column in list(merged):
    if "race" not in column:
        merged[column] = merged[column].apply(lambda c: float(c.split(" ")[0]))

for c in files[1:]:
    counts = pd.read_csv(c)
    for column in list(counts):
        if "race" not in column:
            counts[column] = counts[column].apply(lambda c: float(c.split(" ")[0]))

    merged = merged.merge(counts, on="race", how="outer")

cmap = {
    "USH18P_3_LTrahan": "USH18PTRAHAN",
    "USH18P_3_DKoh": "USH18PKOH",
    "USH18P_3_BLitalien": "USH18PLITALIEN",
    "USH18P_3_JMatias": "USH18PMATIAS",
    "USH18P_3_RGifford": "USH18PGIFFORD",
    "USH18P_3_AChandler": "USH18PCHANDLER",
    "USH18P_3_None": "USH18PBLANK",
    "SS18P_EssMidd2_BFinegold": "SS18PFINEGOLD",
    "SS18P_EssMidd2_PPayano": "SS18PPAYANO",
    "SS18P_EssMidd2_MArmano": "SS18PARMANO",
    "SS18P_EssMidd2_None": "SS18PBLANK",
    "SS14P_EssMidd2_BLitalien": "SS14PLITALIEN",
    "SS14P_EssMidd2_PPayano": "SS14PPAYANO",
    "SS14P_EssMidd2_DRodriguez": "SS14PRODRIGUEZ",
    "SS14P_EssMidd2_None": "SS14PBLANK",
    "pressley": "USH18P_7_APressley",
    "capuano": "USH18P_7_MCapuano",
    "2018_US_HOU_P_None": "USH18P_7_None",
    "walsh": "BOSMAY17G_MWalsh",
    "jackson": "BOSMAY17G_TJackson",
    "2017_BOS_MAY_None": "BOSMAY17G_None",
    "chang_diaz": "SS08P_Suff2_SChangDiaz",
    "wilkerson": "SS08P_Suff2_DWilkerson",
    "forry": "SS13P_Suff1_LForry",
    "collins": "SS13P_Suff1_NCollins",
    "malia": "SH18P_Suff11_EMalia",
    "clemons": "SH18P_Suff11_CClemons",
    "scaccia": "SH18P_Suff14_AScaccia",
    "idowu": "SH18P_Suff14_SIdowu",
    "sh16malia": "SH16P_Suff11_EMalia",
    "sh16clemons": "SH16P_Suff11_CClemons",
    "cullinane": "SH18P_Suff12_DCullinane",
    "lacet": "SH18P_Suff12_JLacet",
    "sh16cullinane": "SH16P_Suff12_DCullinane",
    "sh16lacet": "SH16P_Suff12_JLacet"
}

merged = merged.rename(cmap, axis=1)
merged = merged[~(merged["race"] == "WVAP")]
merged = merged.fillna(0)
merged.to_csv("./data/essex-elections.csv", index=False)
