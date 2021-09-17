
import pandas as pd
import numpy as np

mass2020 = pd.read_csv("./data/massachusetts-2020.csv")
mass2010 = pd.read_csv("./data/massachusetts.csv")
mass2010 = mass2010.set_index("NAME")

elections = [
    ["USH18P_7_APressley","USH18P_7_MCapuano"],
    ["BOSMAY17G_TJackson","BOSMAY17G_MWalsh"],
    ["SS08P_Suff2_SChangDiaz","SS08P_Suff2_DWilkerson"],
    ["SS13P_Suff1_LForry","SS13P_Suff1_NCollins"],
    ["SH18P_Suff11_EMalia","SH18P_Suff11_CClemons"],
    ["SH18P_Suff12_DCullinane","SH18P_Suff12_JLacet"],
    ["SH18P_Suff14_AScaccia", "SH18P_Suff14_SIdowu"],
    ["SH16P_Suff11_EMalia","SH16P_Suff11_CClemons"],
    ["SH16P_Suff12_DCullinane","SH16P_Suff12_JLacet"]
]

for electionset in elections:
    zeros = list(mass2010[mass2010[electionset].isna()].index)
    print(zeros)
    mass2020[electionset] = mass2020[mass2020["NAMELSAD20"].isin(zeros)][electionset].replace(0, np.nan)

mass2020.to_csv("./data/massachusetts-2020-naned.csv", index=False)
