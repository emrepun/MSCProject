import sys

count = "1000"

if len(sys.argv) == 2:
    count = sys.argv[1]

document = open("neural_networks_results.doc", "a+")
document.write("\r\n" + "Results for " + count + " samples:" + "\r\n")
document.close()
