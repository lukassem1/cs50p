# Start coding here... 
import pandas as pd
import numpy as np
#best_math_schools #80%
#top_10_schools #best avarege results
#largest_std_dev #larg std deviation

schools = pd.read_csv('schools.csv')
#print(schools.columns)
best_math_schools = schools[["school_name","average_math"]]
best_math_schools = best_math_schools.sort_values("average_math", ascending = False)
best_math_schools = best_math_schools[best_math_schools["average_math"] > 640]
print(best_math_schools)

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
sub_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT",ascending = False).head(10)
top_10_schools= sub_schools.head(10)
print(top_10_schools)

boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()].reset_index()
largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"}, inplace=True)
