import os
import shutil

BASE_DIR = "/home/cleavers/Dokumen/coolify_new"
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    template = f.read()

# Update undangan_launching.html as well
with open(os.path.join(BASE_DIR, "undangan_launching.html"), "w", encoding="utf-8") as f:
    f.write(template)

subfolders = {
    "rudi": "rudi",
    "yumei": "yumei",
    "adit": "adit",
    "roni": "roni",
    "bung-jeng": "bungjeng"
}

for folder, preset_key in subfolders.items():
    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Pre-select preset in onload
    custom_content = template.replace(
        "window.onload = checkUrlParams;",
        f"window.onload = function() {{ applyPreset('{preset_key}', false); }};"
    )
    
    target_file = os.path.join(folder_path, "index.html")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(custom_content)
    print(f"Created: {target_file}")

print("All 5 dedicated preset folders created successfully!")
