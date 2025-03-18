import os
import shutil
import subprocess

def process_images(image_directory, json_directory, program_directory, palette_directory, colormap_source_directory):
    # För att hålla reda på unika datum som vi har bearbetat
    processed_dates = set()

    # Hämta alla filer i den angivna bildmappen
    for filename in os.listdir(image_directory):
        if filename.startswith("image_") and filename.endswith(".png"):
            # Extrahera DATE och COLORMAP från filnamnet
            try:
                # Dela upp filnamnet i högst tre delar: "image", "DATE" och "COLORMAP"
                parts = filename.split("_", 2)  # Dela upp vid första två understreck
                date = parts[1]  # Exempel: 20250218084314802
                colormap = parts[2].replace(".png", "")  # Resten av strängen är COLORMAP (t.ex. pink_matrix)

                # Om vi inte har bearbetat detta datum tidigare
                if date not in processed_dates:
                    # Markera detta datum som bearbetat
                    processed_dates.add(date)

                    # Skapa inputfilen som ska användas för programmet
                    input_filename = f"image_{date}_input.json"
                    input_filepath = os.path.join(json_directory, input_filename)  # Fullständig sökväg för inputfilen

                    if os.path.exists(input_filepath):
                        # Bygg den fullständiga sökvägen till programmet
                        program_filepath = os.path.join(program_directory, "refraction")

                        # Kontrollera om programmet finns
                        if os.path.exists(program_filepath):
                            # Rensa palettmappen (ta bort alla filer)
                            print(f"Rensar palettmappen: {palette_directory}")
                            for file in os.listdir(palette_directory):
                                file_path = os.path.join(palette_directory, file)
                                if os.path.isfile(file_path):
                                    os.remove(file_path)
                                    print(f"Raderade filen: {file_path}")

                            # Hitta alla unika COLORMAPs för detta DATE
                            colormap_files_to_copy = set()
                            for f in os.listdir(image_directory):
                                if f.startswith(f"image_{date}_") and f.endswith(".png"):
                                    colormap_name = f.split("_", 2)[2].replace(".png", "")
                                    colormap_files_to_copy.add(colormap_name)

                            # Kopiera alla COLORMAP.rgb för detta DATE
                            for colormap in colormap_files_to_copy:
                                colormap_file = f"{colormap}.rgb"
                                colormap_source_filepath = os.path.join(colormap_source_directory, colormap_file)
                                
                                if os.path.exists(colormap_source_filepath):
                                    # Kopiera filen till palettmappen
                                    shutil.copy(colormap_source_filepath, palette_directory)
                                    print(f"Kopierade {colormap_file} till {palette_directory}")
                                else:
                                    print(f"COLORMAP-filen {colormap_file} finns inte i källmappen.")

                            # Kör programmet med inputfilen
                            print(f"Kör programmet {program_filepath} med inputfil: {input_filepath}")
                            try:
                                # Exempel på att köra programmet (byt ut med din faktiska kommandorad)
                                subprocess.run([program_filepath, input_filepath], check=True)
                                print(f"Behandlade filen {input_filename}")
                            except subprocess.CalledProcessError as e:
                                print(f"Fel vid körning av programmet för {input_filename}: {e}")
                        else:
                            print(f"Programfilen {program_filepath} finns inte.")
                    else:
                        print(f"Inputfilen {input_filepath} finns inte.")
            except IndexError:
                print(f"Felaktigt filnamn: {filename}")
        else:
            continue

# Exempel på hur man kör funktionen
image_directory_path = "/home/bearbar/Dropbox/Projects/ymicron/ymicron.github.io/works"  # Mapp med PNG-filer
json_directory_path = "/home/bearbar/Dropbox/Projects/Refraction/AllJson"    # Mapp med JSON-filer
program_directory_path = "/home/bearbar/Dropbox/Projects/Refraction"  # Mapp där ditt program (ditt_program.py) ligger
palette_directory_path = "/home/bearbar/Dropbox/Projects/Refraction/Colormaps"  # Mapp där paletterna ska vara
colormap_source_directory_path = "/home/bearbar/Dropbox/Projects/Refraction/ColormapsLib"  # Mapp där COLORMAP.rgb ligger

process_images(image_directory_path, json_directory_path, program_directory_path, palette_directory_path, colormap_source_directory_path)

