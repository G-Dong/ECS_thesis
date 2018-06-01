import numpy as np
import matplotlib.pyplot as plt
"""
Y = np.array([33.2033860683,
65.7338712215,
105.802303076,
127.147273064,
159.953093052,
207.119021893])
"""
Y= np.array([1.1146544470272097,
1.0697453341904632,
1.0586081362533221,
1.0480170826638715,
1.0376828251365121,
1.0275965858974029])

X = np.array([10,20,30,40,50,60])
plt.scatter(X,Y)
    #plt.plot(X,interprod)
plt.title("Scatter Plot of Pure GD on Real Data (smaller group with alpha = 1e-6)")
plt.xlabel("Number of iteration")
plt.ylabel("error (1e+18)")
   
plt.show()   