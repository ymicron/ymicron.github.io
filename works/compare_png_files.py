import os
import shutil

# Ange sökvägen till den andra mappen här
other_folder_path = "/home/bearbar/Dropbox/Projects/Refraction/Output"  # Byt ut denna med den faktiska sökvägen

# Få sökvägen till mappen där skriptet ligger
script_directory = os.path.dirname(os.path.abspath(__file__))

# Skapa "NotFound"-mappen om den inte finns
not_found_folder = os.path.join(script_directory, "NotFound")
if not os.path.exists(not_found_folder):
    os.makedirs(not_found_folder)

# Gå igenom alla PNG-filer i samma mapp som skriptet
for file_name in os.listdir(script_directory):
    if file_name.endswith(".png"):
        original_file_path = os.path.join(script_directory, file_name)
        
        # Kontrollera om filen finns i den andra mappen
        other_file_path = os.path.join(other_folder_path, file_name)
        
        if not os.path.exists(other_file_path):
            # Om filen inte finns i den andra mappen, kopiera den till "NotFound"-mappen
            shutil.copy(original_file_path, not_found_folder)
            print(f"Kopierade {file_name} till {not_found_folder}")

