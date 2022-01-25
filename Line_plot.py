#jenis jenis dari sebuah visualisasi data pada metploit adalah line plot, countering plot, bar plot, histogram plot,bar chart, dan pie chart.

"""
line_plot merupakan sebuah representasi sebuah data yang menghubungkan nilai data dengan garis biasanya digunakan dalam visualisasi timeseries (data covid,data saham)


"""
import matplotlib.pyplot as plt

nama=[
    "Januari","Febuari","Maret",
    "April","Mei","Juni","Juli","Agustus",
    "September","Oktober","November",
    "Desember"
]

nilai=[1200,1219,1201,1216,1204,1220,1232,1220,1222,1245,1240,1259]

#membuat visualisasi
#1.)membuat kanvas kosong
fig,ax=plt.subplots()
#2.digunakan untuk plots garis nilai X terhadap garis nilai Y
ax.plot(nama,nilai)
#3.memberikan label pada sumbu garis
ax.set_xlabel("Bulan")
ax.set_ylabel("Dana Saham")
#4.menyertai judul
ax.set_title("Analisis Saham Gorengan")
#menampilkan sebuah gambar
plt.show()
