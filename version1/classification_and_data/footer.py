from datetime import datetime

current_time = datetime.now()

document = open("random_forest_results.doc", "a+")
document.write("\r\n" + "A TRAINING CYCLE WITH MULTIPLE SAMPLE AMOUNTS HAS BEEN COMPLETED ON: " + str(current_time) + "\r\n")
document.close()
