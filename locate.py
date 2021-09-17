
import geopandas as gpd

vtds = gpd.read_file("./data/geometries/MA_mggg_pcts/")
dracut = vtds[vtds["NAME20"].str.contains("Dracut")]
winchendon = vtds[vtds["NAME20"].str.contains("Winchendon")]
print(list(dracut["GEOID20"]))
print(list(winchendon["GEOID20"]))
