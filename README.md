# Customer Segmentation Analysis

## 📊 Project Overview

This project performs **customer segmentation** using K-Means clustering to identify distinct customer groups based on age and income. The analysis helps derive actionable marketing strategies for each segment.

### Key Objectives:
✅ Load and explore customer dataset  
✅ Clean and scale features (Age, Income)  
✅ Determine optimal number of clusters using Elbow Method  
✅ Apply K-Means clustering algorithm  
✅ Visualize and profile customer segments  
✅ Generate actionable marketing recommendations  

---

## 📁 Project Structure

```
week3/
├── customerSegmentation.ipynb       # Main Jupyter notebook with analysis
├── generate_report.py               # Python script to generate segment reports
├── customers.csv                    # Input dataset (26 sample customers)
├── customers_with_clusters.csv      # Output: customers with cluster assignments
├── customer_segmentation_report.txt # Human-readable segment report
├── customer_segmentation_report.json # Structured JSON report
└── README.md                        # This file
```

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Step 1: Run the Jupyter Notebook
```bash
jupyter notebook customerSegmentation.ipynb
```

Run all cells sequentially. The notebook will:
- Load customer data
- Scale features
- Apply elbow method to find optimal k
- Perform K-Means clustering
- Visualize clusters
- Save cluster assignments to CSV
- Generate reports

### Step 2: View Reports
After the notebook completes, reports are automatically generated:
- **Text Report:** `customer_segmentation_report.txt`
- **JSON Report:** `customer_segmentation_report.json`

---

## 📊 Dataset: `customers.csv`

**Columns:**
- `Name`: Customer name
- `Age`: Customer age (years)
- `Income`: Annual income ($)
- `SpendingScore`: Spending behavior score (0-100)

**Sample Data:**
```
Name,Age,Income,SpendingScore
Alice,25,30000,70
Bob,31,45000,65
Charlie,28,35000,55
...
```

---

## 🔍 Methodology

### 1. **Data Exploration**
- Load CSV and display summary statistics
- Check for missing values
- Analyze feature distributions

### 2. **Feature Scaling**
- Extract Age and Income columns
- Apply `StandardScaler` to normalize features
- Ensures equal contribution to clustering

### 3. **Elbow Method**
- Calculate inertia for k=1 to k=10
- Plot elbow curve to identify optimal k
- **Selected k=3** (shows clear elbow)

### 4. **K-Means Clustering**
- Fit K-Means model with k=3
- Assign cluster labels to each customer
- Extract cluster centroids

### 5. **Visualization**
- Scatter plot: Age vs Income
- Color-coded by cluster
- Centroids marked with yellow 'X'

### 6. **Segment Profiling**
- Calculate cluster statistics:
  - Average age, income, spending score
  - Customer count and percentage
  - Income and age ranges
- Derive marketing insights per segment

---

## 📈 Results: Customer Segments

### **Segment 0: Budget Conscious** (42.3% of customers)
- **Profile:** Young, lower income, moderate spenders
- **Avg Age:** 27 years | **Avg Income:** $35,091
- **Spending Score:** 56.5/100
- **Marketing Actions:**
  - Offer discounts and promotional deals
  - Bundle products for value pricing
  - Loyalty program with cashback rewards
  - Email campaigns for clearance sales

### **Segment 1: Moderate Spenders** (26.9% of customers)
- **Profile:** Older, high income, high spenders
- **Avg Age:** 42 years | **Avg Income:** $62,143
- **Spending Score:** 80.1/100
- **Marketing Actions:**
  - Cross-sell complementary products
  - Seasonal offers and exclusive collections
  - VIP member benefits
  - Personalized product recommendations

### **Segment 2: Premium Customers** (30.8% of customers)
- **Profile:** Mid-age, moderate income, high spenders
- **Avg Age:** 34.5 years | **Avg Income:** $50,000
- **Spending Score:** 70.5/100
- **Marketing Actions:**
  - Premium/luxury product lines
  - Exclusive early access to new collections
  - Concierge/priority customer service
  - Invite-only events and special experiences

---

## 📄 Output Files

### 1. `customers_with_clusters.csv`
Customer data with assigned cluster labels:
```
Name,Age,Income,SpendingScore,Cluster
Alice,25,30000,70,0
Bob,31,45000,65,2
...
```

### 2. `customer_segmentation_report.txt`
Human-readable report with:
- Segment summaries
- Customer demographics
- Spending behavior
- Marketing recommendations
- Sample customers per segment

### 3. `customer_segmentation_report.json`
Structured JSON with:
```json
{
  "generated_at": "2026-05-14T12:39:47.xxx",
  "total_customers": 26,
  "total_segments": 3,
  "segments": [
    {
      "segment_id": 0,
      "segment_name": "Budget Conscious",
      "customer_count": 11,
      "percentage": 42.3,
      "demographics": {...},
      "marketing_actions": [...]
    },
    ...
  ]
}
```

---

## 🛠️ Customization

### Change Number of Clusters
Edit `customerSegmentation.ipynb`, Section 5:
```python
optimal_k = 4  # Change from 3 to desired value
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
```

### Update Dataset
Replace `customers.csv` with your own data. Required columns:
- `Name` (string)
- `Age` (numeric)
- `Income` (numeric)
- `SpendingScore` (numeric, 0-100)

### Modify Marketing Actions
Edit `generate_report.py`, section with `marketing_actions` dictionary:
```python
marketing_actions = {
    0: ["Your custom action 1", "Your custom action 2", ...],
    1: [...],
    2: [...]
}
```

---

## 📊 Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `matplotlib` | Plotting and visualization |
| `seaborn` | Statistical data visualization |
| `scikit-learn` | Machine learning (KMeans, StandardScaler) |

---

## 🔄 Workflow

```
1. customerSegmentation.ipynb
   ├── Load customers.csv
   ├── Scale features
   ├── Elbow method analysis
   ├── K-Means clustering
   ├── Visualize clusters
   ├── Profile segments
   └── Save customers_with_clusters.csv

2. generate_report.py
   ├── Read customers_with_clusters.csv
   ├── Generate segment profiles
   ├── Create marketing recommendations
   ├── Save as TXT report
   └── Save as JSON report
```

---

## 📝 Usage Example

```bash
# Navigate to project directory
cd /Users/nishi/Desktop/internship/week3

# Run the report script (after notebook execution)
python3 generate_report.py

# View the text report
cat customer_segmentation_report.txt

# View the JSON report
cat customer_segmentation_report.json
```

---

## 🎯 Key Insights

1. **Budget Conscious Segment** is the largest (42%), indicating opportunity for volume-based strategies
2. **Moderate Spenders** have highest income and spending scores, suitable for premium offerings
3. **Premium Customers** balance income and spending habits, ideal for loyalty programs
4. Age correlates with income in this dataset
5. Spending scores vary significantly within income groups, suggesting behavior-based targeting

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `customers_with_clusters.csv not found` | Run notebook first to generate the file |
| Import errors | Install required packages: `pip install -r requirements.txt` |
| Notebook kernel crashes | Restart kernel and run cells sequentially |
| Report not generated | Ensure notebook executed Section 8 completely |

---

## 📚 Related Files

- **Main Notebook:** `customerSegmentation.ipynb`
- **Report Script:** `generate_report.py`
- **Input Data:** `customers.csv`
- **Outputs:** `.csv`, `.txt`, `.json` files

---

## 👨‍💼 Project Info

- **Organization:** Syntecxhub
- **Week:** Week 3
- **Project Type:** Machine Learning - Customer Segmentation
- **Algorithm:** K-Means Clustering
- **Date Generated:** 14 May 2026

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review notebook comments and documentation
3. Verify input data format matches requirements
4. Check generated report files for insights

---

**Happy Analyzing! 🎉**
