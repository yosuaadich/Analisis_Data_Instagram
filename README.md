# Analisis_Data_Instagram
Berikut adalah tiga contoh tabel data yang relevan untuk dianalisis:


Tabel 1: Penggunaan Hashtag dan Engagement
Post_ID	Hashtags	Likes	Comments	Shares
1	#travel #photo	120	15	5
2	#food #yummy	200	30	10
3	#fitness #gym	150	20	8
4	#nature #beauty	180	25	12
5	#art #creative	220	35	15
6	#tech #innovation	170	22	9
7	#fashion #style	190	28	14
8	#music #concert	210	32	11
9	#health #wellness	160	18	7
10	#education #learn	140	16	6
11	#fun #friends	130	14	8
12	#work #office	240	40	20
13	#weekend #relax	250	45	18
14	#summer #beach	180	25	13
15	#love #romance	170	22	12
16	#family #home	200	30	15
17	#holiday #trip	190	28	14
18	#city #urban	220	32	17
19	#mountain #hiking	210	30	16
20	#pets #animals	180	25	12

Tabel 2: Waktu Posting dan Engagement
Post_IDTime_PostedLikes	CommentsShares
1	08:00	100	10	3
2	12:00	220	28	11
3	18:00	170	20	9
4	21:00	200	25	13
5	23:00	130	15	5
6	07:00	110	12	4
7	14:00	190	22	10
8	16:00	160	18	8
9	19:00	180	24	12
10	20:00	140	14	6
11	09:00	150	16	7
12	13:00	230	34	17
13	17:00	240	36	16
14	22:00	180	25	13
15	06:00	160	18	8
16	10:00	120	12	5
17	15:00	200	28	14
18	11:00	170	22	10
19	05:00	110	12	4
20	04:00	100	10	3

Tabel 3: Jenis Konten dan Engagement
Post_ID Content_Type Likes Comments Shares
1	Photo	180	20	6
2	Video	250	35	15
3	Story	150	18	7
4	IGTV	200	25	10
5	Reel	230	30	12
6	Live	170	22	8
7	Carousel	210	28	13
8	Highlight	190	24	9
9	Guide	160	20	6
10	Meme	140	15	5
11	Photo	150	18	8
12	Video	240	38	18
13	Story	250	42	17
14	IGTV	180	28	12
15	Reel	170	25	10
16	Live	200	30	14
17	Carousel	190	28	13
18	Highlight	220	32	15
19	Guide	210	30	14
20	Meme	180	25	12


Langkah 2: Membuat Visualisasi
Mari kita mulai dengan membuat visualisasi untuk data di atas menggunakan Python. Kita akan membuat scatter plot, bar chart, pie chart, box plot, dan histogram.


Langkah 3: Analisis Statistik
Untuk analisis statistik keterkaitan antara data-data ini, kita dapat menggunakan berbagai teknik seperti korelasi Pearson, analisis regresi, dan uji hipotesis.


Langkah 4: Visualisasi Keterkaitan Data
Menggunakan heatmap, kita bisa melihat hubungan korelasi antara berbagai metrik.

![Screenshot (4)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/c249e1dc-c312-4196-a419-d3f5f035df35)

![Screenshot (5)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/5735137d-dc50-42ac-9334-08f0231bca52)

![Screenshot (6)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/2bf93517-6dfe-477c-8e88-96cc42ed49b7)

![Screenshot (7)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/d4e12d9a-ee1d-4ea3-99a2-9272a7454956)

![Screenshot (9)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/fcc6c50c-60ac-4179-ad42-d9dd7fc80269)

![Screenshot (10)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/a522aa9d-d2d3-46c9-8f02-06fbde787403)

Berikut adalah interpretasi dari setiap analisis yang sudah dilakukan:

1. Scatter Plot: Hashtags vs Engagement
   Pada scatter plot pertama, kita memvisualisasikan hubungan antara Likes dengan Comments dan Likes dengan Shares.

   Likes vs Comments: Jika titik-titik cenderung membentuk pola linear, ini menunjukkan adanya hubungan antara jumlah Likes dan jumlah Comments.

   Likes vs Shares: Sama dengan Likes vs Comments, jika ada pola linear, ini menunjukkan hubungan antara jumlah Likes dan jumlah Shares.

   Interpretasi: Jika ada hubungan yang jelas (positif atau negatif) antara Likes dan Comments atau Likes dan Shares, ini bisa menunjukkan bahwa postingan dengan lebih banyak Likes cenderung mendapatkan lebih banyak Comments dan Shares.

3. Bar Chart: Waktu Posting dan Engagement
    Pada bar chart ini, kita memvisualisasikan engagement (Likes, Comments, Shares) berdasarkan waktu posting.

    Likes, Comments, Shares by Time Posted: Chart ini menunjukkan waktu tertentu ketika engagement tertinggi terjadi.

    Interpretasi: Jika engagement lebih tinggi pada waktu-waktu tertentu, ini bisa memberikan wawasan kapan waktu terbaik untuk memposting konten guna mendapatkan lebih banyak engagement.

5. Pie Chart: Jenis Konten dan Likes
    Pie chart ini menunjukkan distribusi Likes berdasarkan jenis konten.

    Likes by Content Type: Menunjukkan jenis konten yang paling banyak mendapatkan Likes.

    Interpretasi: Memahami jenis konten yang lebih disukai oleh audiens dapat membantu dalam strategi konten untuk meningkatkan engagement.

7. Box Plot: Distribusi Engagement
    Box plot ini menunjukkan distribusi dari Likes, Comments, dan Shares.

    Distribution of Engagement Metrics: Menunjukkan rentang, median, dan outlier dari masing-masing metrik.

    Interpretasi: Dapat membantu memahami variasi data dan mengidentifikasi outlier atau postingan yang memiliki engagement jauh lebih tinggi atau lebih rendah dibandingkan yang lain.

9. Histogram: Distribusi Likes
    Histogram ini menunjukkan distribusi frekuensi dari Likes.

    Likes Distribution: Menunjukkan seberapa sering jumlah Likes tertentu terjadi.

    Interpretasi: Membantu memahami distribusi dan kecenderungan data Likes. Jika distribusi tidak normal, ini bisa mempengaruhi analisis statistik lainnya.

11. Korelasi Pearson: Tabel 1, 2, 3
    Heatmap ini menunjukkan matriks korelasi antara Likes, Comments, dan Shares.
    
    Correlation Matrix: Nilai korelasi berkisar dari -1 hingga 1. Nilai mendekati 1 atau -1 menunjukkan hubungan linear kuat, sedangkan nilai mendekati 0 menunjukkan hubungan lemah atau tidak ada hubungan.
    Interpretasi:
     Korelasi positif tinggi antara Likes dan Comments menunjukkan bahwa postingan dengan banyak Likes cenderung juga mendapatkan banyak Comments.

     Korelasi positif tinggi antara Likes dan Shares menunjukkan bahwa postingan dengan banyak Likes cenderung juga dibagikan lebih sering.

     Korelasi antara Comments dan Shares menunjukkan hubungan serupa.
    
11. Analisis Skewness
    Histogram dengan kurva skewness menunjukkan distribusi data dan skewnessnya.

    Likes Skewness: Nilai skewness menunjukkan apakah distribusi Likes condong ke kanan (positif) atau ke kiri (negatif).

    Comments Skewness: Menunjukkan skewness dari distribusi Comments.

    Shares Skewness: Menunjukkan skewness dari distribusi Shares.

    Interpretasi:
          Skewness positif menunjukkan data condong ke kanan dengan lebih banyak nilai rendah dan beberapa nilai tinggi.

          Skewness negatif menunjukkan data condong ke kiri dengan lebih banyak nilai tinggi dan beberapa nilai rendah.

          Distribusi normal memiliki skewness mendekati 0.
