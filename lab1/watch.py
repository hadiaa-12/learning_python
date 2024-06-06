seconds = int(input("how many seconds? "))
hours = int(seconds/3600)
minutes = int((seconds%3600)/60)
second = (seconds%3600)%60
print(hours, minutes , second)