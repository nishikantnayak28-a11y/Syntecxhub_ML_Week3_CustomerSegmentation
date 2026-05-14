"""
Customer Segmentation Report Generator
Generates segment profiles and marketing recommendations
"""

import pandas as pd
import json
from datetime import datetime

def generate_report():
    """Generate segment reports based on cluster analysis"""
    
    # Load the clustered data
    try:
        df = pd.read_csv('customers_with_clusters.csv')
    except FileNotFoundError:
        print("Error: customers_with_clusters.csv not found!")
        return
    
    # Define segment names and marketing actions
    segment_names = {
        0: "Budget Conscious",
        1: "Moderate Spenders", 
        2: "Premium Customers"
    }
    
    marketing_actions = {
        0: [
            "Offer discounts and promotional deals",
            "Bundle products for value pricing",
            "Loyalty program with cashback rewards",
            "Email campaigns for clearance sales"
        ],
        1: [
            "Cross-sell complementary products",
            "Seasonal offers and exclusive collections",
            "VIP member benefits",
            "Personalized product recommendations"
        ],
        2: [
            "Premium/luxury product lines",
            "Exclusive early access to new collections",
            "Concierge/priority customer service",
            "Invite-only events and special experiences"
        ]
    }
    
    # Generate report
    print("\n" + "="*70)
    print("CUSTOMER SEGMENTATION REPORT")
    print("="*70)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Report for each segment
    for cluster_id in sorted(df['Cluster'].unique()):
        cluster_data = df[df['Cluster'] == cluster_id]
        segment_name = segment_names.get(cluster_id, f"Segment {cluster_id}")
        
        print(f"\n{'─'*70}")
        print(f"SEGMENT {cluster_id}: {segment_name}")
        print(f"{'─'*70}")
        
        # Statistics
        print(f"\nCustomer Base:")
        print(f"  • Total Customers: {len(cluster_data)}")
        print(f"  • Percentage: {(len(cluster_data)/len(df)*100):.1f}%")
        
        print(f"\nDemographics:")
        print(f"  • Average Age: {cluster_data['Age'].mean():.1f} years")
        print(f"  • Age Range: {cluster_data['Age'].min()}-{cluster_data['Age'].max()} years")
        print(f"  • Average Income: ${cluster_data['Income'].mean():.0f}")
        print(f"  • Income Range: ${cluster_data['Income'].min()}-${cluster_data['Income'].max()}")
        
        print(f"\nBehavior:")
        print(f"  • Average Spending Score: {cluster_data['SpendingScore'].mean():.1f}/100")
        print(f"  • Spending Range: {cluster_data['SpendingScore'].min()}-{cluster_data['SpendingScore'].max()}")
        
        # Marketing actions
        print(f"\nRecommended Marketing Actions:")
        for i, action in enumerate(marketing_actions.get(cluster_id, []), 1):
            print(f"  {i}. {action}")
        
        # Sample customers
        print(f"\nSample Customers:")
        sample = cluster_data[['Name', 'Age', 'Income', 'SpendingScore']].head(3)
        for idx, row in sample.iterrows():
            print(f"  • {row['Name']}: Age {int(row['Age'])}, "
                  f"Income ${int(row['Income'])}, Spending Score {int(row['SpendingScore'])}")
    
    print(f"\n{'='*70}")
    print("END OF REPORT")
    print("="*70 + "\n")
    
    # Save report to text file
    save_text_report(df, segment_names, marketing_actions)
    
    # Save as JSON
    save_json_report(df, segment_names, marketing_actions)

def save_text_report(df, segment_names, marketing_actions):
    """Save report as text file"""
    
    filename = 'customer_segmentation_report.txt'
    
    with open(filename, 'w') as f:
        f.write("="*70 + "\n")
        f.write("CUSTOMER SEGMENTATION REPORT\n")
        f.write("="*70 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for cluster_id in sorted(df['Cluster'].unique()):
            cluster_data = df[df['Cluster'] == cluster_id]
            segment_name = segment_names.get(cluster_id, f"Segment {cluster_id}")
            
            f.write(f"\n{'-'*70}\n")
            f.write(f"SEGMENT {cluster_id}: {segment_name}\n")
            f.write(f"{'-'*70}\n")
            
            f.write(f"\nCustomer Base:\n")
            f.write(f"  • Total Customers: {len(cluster_data)}\n")
            f.write(f"  • Percentage: {(len(cluster_data)/len(df)*100):.1f}%\n")
            
            f.write(f"\nDemographics:\n")
            f.write(f"  • Average Age: {cluster_data['Age'].mean():.1f} years\n")
            f.write(f"  • Age Range: {cluster_data['Age'].min()}-{cluster_data['Age'].max()} years\n")
            f.write(f"  • Average Income: ${cluster_data['Income'].mean():.0f}\n")
            f.write(f"  • Income Range: ${cluster_data['Income'].min()}-${cluster_data['Income'].max()}\n")
            
            f.write(f"\nBehavior:\n")
            f.write(f"  • Average Spending Score: {cluster_data['SpendingScore'].mean():.1f}/100\n")
            f.write(f"  • Spending Range: {cluster_data['SpendingScore'].min()}-{cluster_data['SpendingScore'].max()}\n")
            
            f.write(f"\nRecommended Marketing Actions:\n")
            for i, action in enumerate(marketing_actions.get(cluster_id, []), 1):
                f.write(f"  {i}. {action}\n")
    
    print(f"✓ Text report saved: {filename}")

def save_json_report(df, segment_names, marketing_actions):
    """Save report as JSON file"""
    
    filename = 'customer_segmentation_report.json'
    
    report_data = {
        "generated_at": datetime.now().isoformat(),
        "total_customers": len(df),
        "total_segments": df['Cluster'].nunique(),
        "segments": []
    }
    
    for cluster_id in sorted(df['Cluster'].unique()):
        cluster_data = df[df['Cluster'] == cluster_id]
        segment_name = segment_names.get(cluster_id, f"Segment {cluster_id}")
        
        segment_info = {
            "segment_id": int(cluster_id),
            "segment_name": segment_name,
            "customer_count": int(len(cluster_data)),
            "percentage": round((len(cluster_data)/len(df)*100), 1),
            "demographics": {
                "avg_age": round(cluster_data['Age'].mean(), 1),
                "age_range": [int(cluster_data['Age'].min()), int(cluster_data['Age'].max())],
                "avg_income": round(cluster_data['Income'].mean(), 0),
                "income_range": [int(cluster_data['Income'].min()), int(cluster_data['Income'].max())]
            },
            "behavior": {
                "avg_spending_score": round(cluster_data['SpendingScore'].mean(), 1),
                "spending_range": [int(cluster_data['SpendingScore'].min()), int(cluster_data['SpendingScore'].max())]
            },
            "marketing_actions": marketing_actions.get(cluster_id, [])
        }
        
        report_data["segments"].append(segment_info)
    
    with open(filename, 'w') as f:
        json.dump(report_data, f, indent=2)
    
    print(f"✓ JSON report saved: {filename}")

if __name__ == "__main__":
    generate_report()
