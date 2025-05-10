#point to be noted
#1. x axis will represent weight in kg
#2. y axis will represent height in cm
#3. title of the graph will be "average weight wrt average height"
#4. marker will be '*' and line color will be green
#5. line style will be 'dashed'
#6. line width will be 2




import matplotlib.pyplot as plt
import pandas as pd
height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
df=pd.DataFrame({"Height":height,"Weight":weight})
 
#seting x label for plot
plt.xlabel("weight in kg ")

#set y label for the plot
plt.ylabel("height in cm")

#setting chart title
plt.title("average weight wrt average height")

#plot using markr '*'and line color as green
plt.plot(df["Weight"],df["Height"],marker="*",markersize=10,linewidth=2,color="green",linestyle='dashdot')

plt.show()