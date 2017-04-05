# Import CSV File
import arcpy
from arcpy import env

env.overwriteOutput=True

env.workspace = r'C:\Users\jvilbig\Desktop\GIS 5090 Labs\Project 1'

output_gdb = r'C:\Users\jvilbig\Desktop\GIS 5090 Labs\Project 1\StlCrime.gdb'
dbf_file = output_gdb+"/"+ "crime_stats_table" #r'C:\Users\jvilbig\Desktop\GIS 5090 Labs\Project 1\StlCrimeStats.dbf'
infc = output_gdb + "/" + "Crime_Points"

arcpy.CopyRows_management("January2017.csv", dbf_file)

# Make XY Event Layer
arcpy.MakeXYEventLayer_management(dbf_file, "XCoord", "YCoord", "Crime_Locations")

# Convert Event Layer to Feature Class
arcpy.FeatureClassToFeatureClass_conversion("Crime_Locations", output_gdb, "Crime_Points")

# Define FC projection
sr = arcpy.SpatialReference('NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)')
arcpy.DefineProjection_management(infc, sr)

print "Analysis Complete"