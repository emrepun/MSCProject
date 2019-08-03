import sys

count = "10"

if len(sys.argv) == 2:
    count = sys.argv[1]

#document = open("random_forest_results.doc", "a+")
document = open("normal_distribution_random_forest_results.doc", "a+")
document.write("\r\n" + "Results for " + count + " samples:" + "\r\n")
document.close()
