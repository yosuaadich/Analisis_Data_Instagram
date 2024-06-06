import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data1 = {
    'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Hashtags': ['#travel #photo', '#food #yummy', '#fitness #gym', '#nature #beauty', '#art #creative', '#tech #innovation', '#fashion #style', '#music #concert', '#health #wellness', '#education #learn'],
    'Likes': [120, 200, 150, 180, 220, 170, 190, 210, 160, 140],
    'Comments': [15, 30, 20, 25, 35, 22, 28, 32, 18, 16],
    'Shares': [5, 10, 8, 12, 15, 9, 14, 11, 7, 6]
}

data2 = {
    'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Time_Posted': ['08:00', '12:00', '18:00', '21:00', '23:00', '07:00', '14:00', '16:00', '19:00', '20:00'],
    'Likes': [100, 220, 170, 200, 130, 110, 190, 160, 180, 140],
    'Comments': [10, 28, 20, 25, 15, 12, 22, 18, 24, 14],
    'Shares': [3, 11, 9, 13, 5, 4, 10, 8, 12, 6]
}

data3 = {
    'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Content_Type': ['Photo', 'Video', 'Story', 'IGTV', 'Reel', 'Live', 'Carousel', 'Highlight', 'Guide', 'Meme'],
    'Likes': [180, 250, 150, 200, 230, 170, 210, 190, 160, 140],
    'Comments': [20, 35, 18, 25, 30, 22, 28, 24, 20, 15],
    'Shares': [6, 15, 7, 10, 12, 8, 13, 9, 6, 5]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

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
