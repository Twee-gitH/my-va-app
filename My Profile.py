import json
import os

FILENAME = "profiles_db.json"

def load_all_profiles():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return []

def save_all_profiles(profiles_list):
    with open(FILENAME, "w") as file:
        json.dump(profiles_list, file, indent=4)
    print(f"\n[Success] Database updated!")

def main():
    print("--- Virtual Assistant Profile Manager ---")
    all_profiles = load_all_profiles()
    
    # Check if your profile is already in there
    if not any(p['Name'] == "Twee Shin" for p in all_profiles):
        print("Adding your professional resume info to the database...")
        my_info = {
            "Name": "Twee Shin",
            "Age": "20s/30s",  # You can edit this number in the code
            "Role": "Virtual Assistant (Medical/Legal)",
            "Skills": "Medical Terminology, MS Office, Bilingual Translation, PSA Data Entry",
            "Experience": "Tagum Doctors Hospital, PSA, Freelance Translator"
        }
        all_profiles.append(my_info)
        save_all_profiles(all_profiles)
    else:
        print("Your profile is already loaded.")

    # Option to add MORE profiles
    add_more = input("\nAdd another profile? (y/n): ").lower()
    if add_more == 'y':
        new_profile = {
            "Name": input("Name: ").strip(),
            "Age": input("Age: ").strip(),
            "Role": input("Role: ").strip(),
            "Skills": input("Skills: ").strip()
        }
        all_profiles.append(new_profile)
        save_all_profiles(all_profiles)

    # Show the database
    print("\n--- Current Profiles ---")
    for i, p in enumerate(all_profiles, 1):
        print(f"{i}. {p['Name']} - {p['Role']}")

if __name__ == "__main__": 
    main()
