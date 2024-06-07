# Analisis_Data_Instagram
Berikut adalah tiga contoh tabel data yang relevan untuk dianalisis:


Tabel 1: Penggunaan Hashtag dan Engagement

        Post_ID	Hashtags	Likes	Comments	Shares

        1	#travel #photo	120	15	5

        2	#food #yummy	200	30	10

        3	#fitness #gym	150	20	8

        4	#nature #beauty	180	25	12

        5	#art #creative	220	35	15


Tabel 2: Waktu Posting dan Engagement

        Post_ID	Time_Posted	Likes	Comments	Shares

        1	08:00	100	10	3

        2	12:00	220	28	11

        3	18:00	170	20	9

        4	21:00	200	25	13

        5	23:00	130	15	5


Tabel 3: Jenis Konten dan Engagement

        Post_ID	Content_Type	Likes	Comments	Shares

        1	Photo	180	20	6

        2	Video	250	35	15

        3	Story	150	18	7

        4	IGTV	200	25	10

        5	Reel	230	30	12


Langkah 2: Membuat Visualisasi
Mari kita mulai dengan membuat visualisasi untuk data di atas menggunakan Python. Kita akan membuat scatter plot, bar chart, pie chart, box plot, dan histogram.


Langkah 3: Analisis Statistik
Untuk analisis statistik keterkaitan antara data-data ini, kita dapat menggunakan berbagai teknik seperti korelasi Pearson, analisis regresi, dan uji hipotesis.


Langkah 4: Visualisasi Keterkaitan Data
Menggunakan heatmap, kita bisa melihat hubungan korelasi antara berbagai metrik.



![Screenshot (174)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/c46e4175-f9ea-4026-9163-09898a78c8ed)

![Screenshot (175)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/65db1ea9-4156-4b42-ad74-82048067c6e8)

![Screenshot (176)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/7d409eaa-d8f5-4135-aa8b-23472f959e70)

![Screenshot (177)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/098f08e8-c404-429d-835c-0bb544ba5a81)

![Screenshot (2)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/bca7a997-938f-48aa-8c25-5c9eb3c90ab8)

![Screenshot (3)](https://github.com/yosuaadich/Analisis_Data_Instagram/assets/152783601/d5a3903a-24e0-436f-92e9-1cf7eaeeac3d)

Berikut adalah interpretasi dari setiap analisis yang sudah dilakukan:

1. Scatter Plot: Hashtags vs Engagement
    Pada scatter plot pertama, kita memvisualisasikan hubungan antara Likes dengan Comments dan Likes dengan Shares.

    Likes vs Comments: Jika titik-titik cenderung membentuk pola linear, ini menunjukkan adanya hubungan antara jumlah Likes dan jumlah Comments.
    Likes vs Shares: Sama dengan Likes vs Comments, jika ada pola linear, ini menunjukkan hubungan antara jumlah Likes dan jumlah Shares.
    Interpretasi: Jika ada hubungan yang jelas (positif atau negatif) antara Likes dan Comments atau Likes dan Shares, ini bisa menunjukkan bahwa postingan dengan lebih banyak Likes cenderung mendapatkan lebih banyak Comments dan Shares.

2. Bar Chart: Waktu Posting dan Engagement
    Pada bar chart ini, kita memvisualisasikan engagement (Likes, Comments, Shares) berdasarkan waktu posting.

    Likes, Comments, Shares by Time Posted: Chart ini menunjukkan waktu tertentu ketika engagement tertinggi terjadi.
    Interpretasi: Jika engagement lebih tinggi pada waktu-waktu tertentu, ini bisa memberikan wawasan kapan waktu terbaik untuk memposting konten guna mendapatkan lebih banyak engagement.

3. Pie Chart: Jenis Konten dan Likes
    Pie chart ini menunjukkan distribusi Likes berdasarkan jenis konten.

    Likes by Content Type: Menunjukkan jenis konten yang paling banyak mendapatkan Likes.
    Interpretasi: Memahami jenis konten yang lebih disukai oleh audiens dapat membantu dalam strategi konten untuk meningkatkan engagement.

4. Box Plot: Distribusi Engagement
    Box plot ini menunjukkan distribusi dari Likes, Comments, dan Shares.

    Distribution of Engagement Metrics: Menunjukkan rentang, median, dan outlier dari masing-masing metrik.
    Interpretasi: Dapat membantu memahami variasi data dan mengidentifikasi outlier atau postingan yang memiliki engagement jauh lebih tinggi atau lebih rendah dibandingkan yang lain.

5. Histogram: Distribusi Likes
    Histogram ini menunjukkan distribusi frekuensi dari Likes.

    Likes Distribution: Menunjukkan seberapa sering jumlah Likes tertentu terjadi.
    Interpretasi: Membantu memahami distribusi dan kecenderungan data Likes. Jika distribusi tidak normal, ini bisa mempengaruhi analisis statistik lainnya.

6. Korelasi Pearson: Tabel 1, 2, 3
   Heatmap ini menunjukkan matriks korelasi antara Likes, Comments, dan Shares.
    
   Correlation Matrix: Nilai korelasi berkisar dari -1 hingga 1. Nilai mendekati 1 atau -1 menunjukkan hubungan linear kuat, sedangkan nilai mendekati 0 menunjukkan hubungan lemah atau tidak ada hubungan.
    Interpretasi:

    Korelasi positif tinggi antara Likes dan Comments menunjukkan bahwa postingan dengan banyak Likes cenderung juga mendapatkan banyak Comments.
    Korelasi positif tinggi antara Likes dan Shares menunjukkan bahwa postingan dengan banyak Likes cenderung juga dibagikan lebih sering.
    Korelasi antara Comments dan Shares menunjukkan hubungan serupa.
7. Analisis Skewness
    Histogram dengan kurva skewness menunjukkan distribusi data dan skewnessnya.

    Likes Skewness: Nilai skewness menunjukkan apakah distribusi Likes condong ke kanan (positif) atau ke kiri (negatif).
    Comments Skewness: Menunjukkan skewness dari distribusi Comments.
    Shares Skewness: Menunjukkan skewness dari distribusi Shares.
        Interpretasi:

        Skewness positif menunjukkan data condong ke kanan dengan lebih banyak nilai rendah dan beberapa nilai tinggi.
        Skewness negatif menunjukkan data condong ke kiri dengan lebih banyak nilai tinggi dan beberapa nilai rendah.
        Distribusi normal memiliki skewness mendekati 0.
