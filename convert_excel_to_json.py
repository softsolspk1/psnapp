import pandas as pd
import json
import os

def convert_excel_to_json():
    # Create data directory if it doesn't exist
    os.makedirs('assets/data', exist_ok=True)
    
    try:
        # Read Excel file
        df = pd.read_excel('PSN Members List.xlsx')
        
        # Convert DataFrame to list of dictionaries
        members = []
        for index, row in df.iterrows():
            member = {
                'id': int(index + 1),
                'name': str(row['Member Name']) if pd.notna(row['Member Name']) else None,
                'gender': str(row['gender']) if pd.notna(row['gender']) else None,
                'designation': str(row['designation']) if pd.notna(row['designation']) else None,
                'institution': str(row['instName']) if pd.notna(row['instName']) else None,
                'institution_address': str(row['instAdress']) if pd.notna(row['instAdress']) else None,
                'city': str(row['city']) if pd.notna(row['city']) else None,
                'province': str(row['province']) if pd.notna(row['province']) else None,
                'country': str(row['country']) if pd.notna(row['country']) else None,
                'email': str(row['email']) if pd.notna(row['email']) else None,
                'phone': str(row['phone']) if pd.notna(row['phone']) else None,
                'photo_url': str(row['profilePic']) if pd.notna(row['profilePic']) else None
            }
            
            # Remove None values and 'nan' strings
            member = {k: v for k, v in member.items() if v is not None and str(v).lower() != 'nan'}
            
            # Only add member if they have a name
            if 'name' in member:
                members.append(member)
        
        # Save to JSON file
        with open('assets/data/members.json', 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully converted Excel data to JSON. Total members: {len(members)}")
        
    except Exception as e:
        print(f"Error converting Excel to JSON: {str(e)}")

if __name__ == "__main__":
    convert_excel_to_json() 