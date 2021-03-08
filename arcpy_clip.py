#drmriazkhan
#https://github.com/drmriaz
# Import arcpy module
import arcpy

# Script arguments
feature_to_be_clipped = arcpy.GetParameterAsText(0)
if feature_to_be_clipped == '#' or not feature_to_be_clipped:
    feature_to_be_clipped = "Pakistan_Districts" # provide a default value if unspecified

boudary = arcpy.GetParameterAsText(1)
if boudary == '#' or not boudary:
    boudary = "KPK_Boundary" # provide a default value if unspecified

clipped = arcpy.GetParameterAsText(2)
if clipped == '#' or not clipped:
    clipped = "Clipped" # provide a default value if unspecified

# Local variables:

# Process: Clip
arcpy.Clip_analysis(feature_to_be_clipped, boudary, clipped, "")

