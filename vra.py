
import pandas as pd
import geopandas as gpd

vtds = pd.read_csv("./data/mass.csv")
essex = pd.read_csv("./data/essex.csv")

keep = [
    "GEOID20", "NAMELSAD20", "SEN13GEMARKEY", "SEN13GGGOMEZ", "SEN13PEMARKEY", "SEN13PSLYNCH",
    "GOV14PMCOAKLEY", "GOV14PSGROSSMAN", "GOV14PDBERWICK", "GOV14GCBAKER",
    "GOV14GMCOAKLEY", "LTGOV14PSKERRIGAN", "LTGOV14PLCHEUNG", "LTGOV14PMLAKE",
    "GOV14GCBAKER","GOV14GMCOAKLEY", "AG14PMHEALEY", "AG14PWTOLMAN",
    "AG14GMHEALEY","AG14GJMILLER", "TRE14PDGOLDBERG", "TRE14PBFINEGOLD", "TRE14PCONROY",
    "TRE14GDGOLDBERG","TRE14GMHEFFERNAN", "PRES16PHCLINTON","PRES16PBSANDERS",
    "PRES16GHCLINTON","PRES16GDTRUMP","GOV18PJGONZALEZ", "GOV18PBMASSIE",
    "GOV18GCBAKER", "GOV18GJGONZALEZ","LTGOV18PQPALFREY", "LTGOV18PJTINGLE",
    "GOV18GCBAKER", "GOV18GJGONZALEZ",
    "SOC18PWGALVIN","SOC18PJZAKIM", "SOC18GWGALVIN","SOC18GAAMORE",
    "PRES20PJBIDEN","PRES20PBSANDERS",
    "PRES20PEWARREN","PRES20PMBLOOMBERG","PRES20GJBIDEN","PRES20GDTRUMP",
    "SEN20PEMARKEY","SEN20PJKENNEDY","SEN20GEMARKEY","SEN20GKOCONNOR"
]

keep += [c for c in list(vtds) if "CVAP" in c]
keep += [c for c in list(vtds) if "VAP" in c and "CVAP" not in c]
keep += [c for c in list(vtds) if "POP" in c]

# Format the ID column and grab the right stuff.
vtds["GEOID20"] = vtds["GEOID20"].astype(str)
essex["GEOID20"] = essex["GEOID20"].astype(str)
vtds = vtds[keep]

# Merge Essex County data.
merged = vtds.merge(essex, on="GEOID20", how="outer")

# Read in Boston elections.
boston = pd.read_csv("./data/dataPrep/massachusetts-something.csv")
merged = merged.merge(boston, left_on="NAMELSAD20_x", right_on="NAMELSAD20", how="outer")
assert len(merged) == len(vtds)

merged.to_csv("./data/massachusetts-2020.csv", index=False)
