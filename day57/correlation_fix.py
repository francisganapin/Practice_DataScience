# CORRELATION FIX
# Copy this cell into your notebook where you calculate correlations

# Select ONLY numeric columns for correlation (excludes categorical like 'Old', 'New', etc.)
numeric_df = df.select_dtypes(include=[np.number])

# Now calculate correlation on numeric columns only
corr_matrix = numeric_df.corr()

# Create heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='RdBu_r',
            center=0,
            square=True,
            linewidths=0.5,
            ax=ax)

ax.set_title('Correlation Between All Features\n(Closer to 1 = Strong Positive, Closer to -1 = Strong Negative)', 
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()
