"""
Scarreter adalah sebuah tipe yang menggambarkan titik titik yang merepresentasikan nilai x terhadap y sebuah data  yang digunakan dalam menghubungkan sebuah dua buah nilai 

"""

import numpy as np
np.random.seed(1)
import matplotlib.pylab as plt
x=np.linspace(0,100,100)
#proses generating dataset yang mengikuti pola y = 2x namun diberikan nilai pencilan (outlier)
y=2*x+np.random.randint(-10,10,100)

#membuat sebuah layer baru
fig,ax=plt.subplots()
#membuat scralleter plot
ax.scatter(x,y)
#menampilkan kanvas
plt.show()

