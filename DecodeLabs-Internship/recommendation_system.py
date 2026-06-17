import pandas as pd

def read_dataset():
    try:
        data = pd.read_excel('Online-Store-Orders.xlsx')
        data.columns = [str(col).strip().lower() for col in data.columns]
        return data
    except:
        try:
            data = pd.read_excel('Online-Store-Orders')
            data.columns = [str(col).strip().lower() for col in data.columns]
            return data
        except:
            print("File 'Online-Store-Orders.xlsx' not found!")
            return None

def get_recommendations(data, user_choice):
    user_search = user_choice.strip().lower()
    
    data['clean_product'] = data['product'].str.strip().str.lower()
    
    filtered_df = data[data['clean_product'].str.contains(user_search, na=False)]
    
    if filtered_df.empty:
        print("\n No exact matches found. Showing our overall top store products instead!")
        filtered_df = data
        
    top_products = filtered_df.groupby('product')['quantity'].sum().reset_index()
    top_products = top_products.sort_values(by='quantity', ascending=False)
    
    return top_products.head(3)

def main():
    print("--- Store Recommendation System ---")
    
    df = read_dataset()
    if df is None:
        return
        
    sample_products = df['product'].dropna().unique()[:5]
    print("\nSome available products in store:")
    for prod in sample_products:
        print(f"- {prod}")
        
    user_input = input("\nWhat product or keyword are you looking for? ")
    print(f"\nSearching for: {user_input}...")
    
    results = get_recommendations(df, user_input)
    
    print("\nOur Top Recommendations:")
    if results is not None and not results.empty:
        for i, row in results.iterrows():
            print(f"Product: {row['product']} (Total Sold: {row['quantity']})")
    else:
        print("No recommendations available.")

if __name__ == "__main__":
    main()