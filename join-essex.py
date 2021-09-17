
import pandas as pd
import geopandas as gpd

# Note that I got the abbreviation wrong: the "sos" elections are for State Senate,
# *not* Secretary of State (which Rachel informed me is actually the Secretary
# of the Commonwealth, because Massachusetts isn't technically a state).

files = [
    "./data/essex-house-18-primary.csv",
    "./data/essex-sos-18-primary.csv",
    "./data/essex-sos-14-primary.csv",
    "./data/essex-house-17-general.csv"
]

colmapush18 = {
    "Lori Trahan": "USH18PTRAHAN",
    "Daniel Koh": "USH18PKOH",
    "Barbara L'Italien": "USH18PLITALIEN",
    "Juana Matias": "USH18PMATIAS",
    "Rufus Gifford": "USH18PGIFFORD",
    "Alexandra Chandler": "USH18PCHANDLER",
    "Beej Das": "USH18PDAS",
    "Jeffrey Ballinger": "USH18PBALLINGER",
    "Bopha Malone": "USH18PMALONE",
    "Leonard Golder": "USH18PGOLDER",
    # "All Others": "USH18POTHER",
    "Blanks": "USH18PBLANK",
    # "Total Votes Cast": "USH18PTOTVOTE"
}

colmapss18 = {
    "Barry Finegold": "SS18PFINEGOLD",
    "Mike Armano": "SS18PARMANO",
    "Pavel Payano": "SS18PPAYANO",
    # "All Others": "SS18POTHER",
    "Blanks": "SS18PBLANK",
    # "Total Votes Cast": "SS18PTOTVOTE"
}

colmapss14 = {
    "Barbara L'Italien": "SS14PLITALIEN",
    "Pavel Payano": "SS14PPAYANO",
    "Doris Rodriguez": "SS14PRODRIGUEZ",
    # "All Others": "SS14POTHER",
    "Blanks": "SS14PBLANK",
    # "Total Votes Cast": "SS14PTOTVOTE"
}

colmapsh17 = {
    "Andres Vargas": "SH17PVARGAS",
    "Shaun Toohey": "SH17PTOOHEY",
    # "All Others": "SH17POTHER",
    "Blanks": "SH17PBLANK",
    # "Total Votes Cast": "SH17PTOTVOTE"
}

columns = list(colmapush18.values()) + list(colmapss18.values()) + list(colmapss14.values())
print(columns)
print([0]*len(columns))
# print(list(colmapush18.values()) + list(colmapss18.values()) + list(colmapss14.values()))

essex = pd.read_csv(files[0]).rename(colmapush18, axis=1)

# For the remaining, join on "name."
for file, colmap in zip(files[1:], [colmapss18, colmapss14, colmapsh17]):
    mergeable = pd.read_csv(file).rename(colmap, axis=1)
    essex = essex.merge(mergeable, on="NAME", how="outer")

# Drop things and rename things.
dropped = [c for c in list(essex) if "_x" in c]
essex = essex.drop(dropped, axis=1)
essex = essex.rename({
    column: column.replace("_y", "")
    for column in list(essex)
}, axis=1)

# Combine two precincts which don't seem to have a match otherwise.
winchendon_indices = essex[essex["NAME"] == "Winchendon Town Precinct 1A"].index
dracut_indices = essex[essex["NAME"] == "Dracut Town Precinct 6A"].index
essex.loc[winchendon_indices, "NAME"] = "Winchendon Town Precinct 1"
essex.loc[dracut_indices, "NAME"] = "Dracut Town Precinct 6"

essex = essex.groupby(by="NAME").sum().reset_index()

# Load the precinct geojson to attach GEOIDs.
vtds = gpd.read_file("./data/geometries/MA_vtd20.geojson")
essex = essex.merge(vtds[["NAMELSAD20", "GEOID20"]], left_on="NAME", right_on="NAMELSAD20")
essex["GEOID20"] = essex["GEOID20"].astype(str)
essed = essex.drop("NAMELSAD20", axis=1)

essex.to_csv("./data/essex.csv", index=False)
