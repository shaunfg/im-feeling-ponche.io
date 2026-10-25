import requests
import json
import csv
from io import StringIO

# Google Sheets configuration
SHEET_ID = '16KsSO3aFWe80XplMn7k4pXi5tag0tUaQbjYFhsjGNO8'

def fetch_sheet_data(sheet_id, filename):
    try:
        # Fetch CSV data from Google Sheets
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        response = requests.get(csv_url)
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch {filename}: {response.status_code}")
            return None
        
        # Google serves UTF-8 without a charset header, so requests would guess latin-1
        response.encoding = 'utf-8'

        # Parse CSV data
        csv_text = response.text
        csv_reader = csv.DictReader(StringIO(csv_text))
        data = list(csv_reader)
        
        # Save to JSON file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Successfully saved {len(data)} rows to {filename}")
        return data
        
    except Exception as e:
        print(f"❌ Error fetching {filename}: {str(e)}")
        return None

def main():
    print("🔄 Fetching data from Google Sheets...")
    
    # Fetch ponche data
    fetch_sheet_data(SHEET_ID, 'ponche_data.json')
    
    print("✅ Done! Check ponche_data.json")

if __name__ == "__main__":
    main()
