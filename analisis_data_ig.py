import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data yang diperluas
data1 = {
    'Post_ID': list(range(1, 21)),
    'Hashtags': [
        '#travel #photo', '#food #yummy', '#fitness #gym', '#nature #beauty', '#art #creative',
        '#tech #innovation', '#fashion #style', '#music #concert', '#health #wellness', '#education #learn',
        '#fun #friends', '#work #office', '#weekend #relax', '#summer #beach', '#love #romance',
        '#family #home', '#holiday #trip', '#city #urban', '#mountain #hiking', '#pets #animals'
    ],
    'Likes': [120, 200, 150, 180, 220, 170, 190, 210, 160, 140, 130, 240, 250, 180, 170, 200, 190, 220, 210, 180],
    'Comments': [15, 30, 20, 25, 35, 22, 28, 32, 18, 16, 14, 40, 45, 25, 22, 30, 28, 32, 30, 25],
    'Shares': [5, 10, 8, 12, 15, 9, 14, 11, 7, 6, 8, 20, 18, 13, 12, 15, 14, 17, 16, 12]
}

data2 = {
    'Post_ID': list(range(1, 21)),
    'Time_Posted': [
        '08:00', '12:00', '18:00', '21:00', '23:00', '07:00', '14:00', '16:00', '19:00', '20:00',
        '09:00', '13:00', '17:00', '22:00', '06:00', '10:00', '15:00', '11:00', '05:00', '04:00'
    ],
    'Likes': [100, 220, 170, 200, 130, 110, 190, 160, 180, 140, 150, 230, 240, 180, 160, 120, 200, 170, 110, 100],
    'Comments': [10, 28, 20, 25, 15, 12, 22, 18, 24, 14, 16, 34, 36, 25, 18, 12, 28, 22, 12, 10],
    'Shares': [3, 11, 9, 13, 5, 4, 10, 8, 12, 6, 7, 17, 16, 13, 8, 5, 14, 10, 4, 3]
}

data3 = {
    'Post_ID': list(range(1, 21)),
    'Content_Type': [
        'Photo', 'Video', 'Story', 'IGTV', 'Reel', 'Live', 'Carousel', 'Highlight', 'Guide', 'Meme',
        'Photo', 'Video', 'Story', 'IGTV', 'Reel', 'Live', 'Carousel', 'Highlight', 'Guide', 'Meme'
    ],
    'Likes': [180, 250, 150, 200, 230, 170, 210, 190, 160, 140, 150, 240, 250, 180, 170, 200, 190, 220, 210, 180],
    'Comments': [20, 35, 18, 25, 30, 22, 28, 24, 20, 15, 18, 38, 42, 28, 25, 30, 28, 32, 30, 25],
    'Shares': [6, 15, 7, 10, 12, 8, 13, 9, 6, 5, 8, 18, 17, 12, 10, 14, 13, 15, 14, 12]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Fungsi untuk menghitung skewness
def calculate_skewness(series):
    return series.skew()

# Fungsi untuk menghitung regresi linear
def linear_regression(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    return slope, intercept

# Visualisasi Data

# Jendela 1
plt.figure(figsize=(12, 6))

# Scatter Plot: Hashtags vs Engagement
plt.subplot(1, 2, 1)
plt.scatter(df1['Likes'], df1['Comments'], c='blue', label='Likes vs Comments')
plt.scatter(df1['Likes'], df1['Shares'], c='red', label='Likes vs Shares')
plt.title('Engagement Based on Hashtags')
plt.xlabel('Likes')
plt.ylabel('Comments / Shares')
plt.legend()
plt.grid(True)

# Bar Chart: Waktu Posting dan Engagement
plt.subplot(1, 2, 2)
df2.set_index('Time_Posted')[['Likes', 'Comments', 'Shares']].plot(kind='bar', ax=plt.gca())
plt.title('Engagement by Time Posted')
plt.xlabel('Time Posted')
plt.ylabel('Engagement')
plt.grid(axis='y')

plt.tight_layout()
plt.show()

# Jendela 2
plt.figure(figsize=(12, 6))

# Pie Chart: Jenis Konten dan Likes
plt.subplot(1, 2, 1)
plt.pie(df3['Likes'], labels=df3['Content_Type'], autopct='%1.1f%%', startangle=140)
plt.title('Likes Distribution by Content Type')

# Box Plot: Distribusi Engagement
plt.subplot(1, 2, 2)
df1[['Likes', 'Comments', 'Shares']].plot(kind='box', ax=plt.gca())
plt.title('Distribution of Engagement Metrics')
plt.grid(True)

plt.tight_layout()
plt.show()

# Analisis Statistik

# Jendela 3
plt.figure(figsize=(12, 6))

# Histogram: Distribusi Likes
plt.subplot(1, 2, 1)
plt.hist(df1['Likes'], bins=5, color='skyblue', edgecolor='black')
plt.title('Likes Distribution')
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.grid(True)

# Korelasi Pearson Tabel 1
plt.subplot(1, 2, 2)
correlation_matrix1 = df1[['Likes', 'Comments', 'Shares']].corr()
sns.heatmap(correlation_matrix1, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Engagement Metrics (Hashtags)')

plt.tight_layout()
plt.show()

# Jendela 4
plt.figure(figsize=(12, 6))

# Korelasi Pearson Tabel 2
plt.subplot(1, 2, 1)
correlation_matrix2 = df2[['Likes', 'Comments', 'Shares']].corr()
sns.heatmap(correlation_matrix2, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Engagement Metrics (Time Posted)')

# Korelasi Pearson Tabel 3
plt.subplot(1, 2, 2)
correlation_matrix3 = df3[['Likes', 'Comments', 'Shares']].corr()
sns.heatmap(correlation_matrix3, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Engagement Metrics (Content Type)')

plt.tight_layout()
plt.show()

# Analisis Skewness

# Jendela 5
plt.figure(figsize=(12, 6))

# Skewness Likes
plt.subplot(1, 2, 1)
sns.histplot(df1['Likes'], kde=True, color='skyblue', edgecolor='black')
likes_skewness = calculate_skewness(df1['Likes'])
plt.title(f'Likes Distribution (Skewness: {likes_skewness:.2f})')
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.grid(True)

# Skewness Comments
plt.subplot(1, 2, 2)
sns.histplot(df1['Comments'], kde=True, color='lightgreen', edgecolor='black')
comments_skewness = calculate_skewness(df1['Comments'])
plt.title(f'Comments Distribution (Skewness: {comments_skewness:.2f})')
plt.xlabel('Comments')
plt.ylabel('Frequency')
plt.grid(True)

plt.tight_layout()
plt.show()

# Jendela 6
plt.figure(figsize=(12, 6))

# Skewness Shares
plt.subplot(1, 2, 1)
sns.histplot(df1['Shares'], kde=True, color='lightcoral', edgecolor='black')
shares_skewness = calculate_skewness(df1['Shares'])
plt.title(f'Shares Distribution (Skewness: {shares_skewness:.2f})')
plt.xlabel('Shares')
plt.ylabel('Frequency')
plt.grid(True)

plt.tight_layout()
plt.show()

# Analisis Regresi Linear

# Jendela 7
plt.figure(figsize=(12, 6))

# Linear Regression Likes vs Comments
plt.subplot(1, 2, 1)
slope_likes_comments, intercept_likes_comments = np.polyfit(df1['Likes'], df1['Comments'], 1)
plt.scatter(df1['Likes'], df1['Comments'], c='blue')
plt.plot(df1['Likes'], slope_likes_comments * df1['Likes'] + intercept_likes_comments, color='red')
plt.title('Linear Regression: Likes vs Comments')
plt.xlabel('Likes')
plt.ylabel('Comments')
plt.grid(True)

# Linear Regression Likes vs Shares
plt.subplot(1, 2, 2)
slope_likes_shares, intercept_likes_shares = np.polyfit(df1['Likes'], df1['Shares'], 1)
plt.scatter(df1['Likes'], df1['Shares'], c='blue')
plt.plot(df1['Likes'], slope_likes_shares * df1['Likes'] + intercept_likes_shares, color='red')
plt.title('Linear Regression: Likes vs Shares')
plt.xlabel('Likes')
plt.ylabel('Shares')
plt.grid(True)

plt.tight_layout()
plt.show()
