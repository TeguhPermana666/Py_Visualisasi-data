import matplotlib.pylab as plt
siswa=[10,20,30,40,50]
bahasa_favorit=["Java","C","C++","Python","Kotlin"]
#membuat kanvas kosong
fig,ax=plt.subplots()
#membuat diagram dengan lingkaran
ax.pie(
    siswa,labels= bahasa_favorit,
    autopct="%.2f%%"
    )
#melihatkan data
plt.show()

