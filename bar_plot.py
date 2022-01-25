import matplotlib.pyplot as plt
#bentuk dari visualisasi data dengan menggunakan sebuah persegi panjang sebagai penunjuk nilai  yang dapa tdigambarkan baik secara horizontal ataupun vertical

Makanan=["Bakso","Mie","Batakor","Tipat","Ayam Goreng"]
Peminat=[10,20,30,40,50]
fig,ax=plt.subplots()
ax.bar(
    Makanan,Peminat,
    color=["red","blue","green","yellow","pink"]
)
ax.set_xlabel("MAKANAN DISUKAI")
ax.set_ylabel("Peminat di setiap makanan")
plt.show()

"""
Bagian #1 digunakan untuk membuat kanvas kosong.
Bagian #2 adalah Code dasar untuk membuat diagram batang dengan nilai x merupakan label dan y merupakan nilai atau kuantitas dari data.
Bagian #3 adalah Code untuk membuat label pada sumbu x.
Bagian #4 adalah Code untuk membuat label pada sumbu y.
Bagian #5 adalah Code untuk menampilkan atau memunculkan gambar.
"""