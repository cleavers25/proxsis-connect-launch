import os

BASE_DIR = "/home/cleavers/Dokumen/coolify_new"
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    template = f.read()

# Update undangan_launching.html
with open(os.path.join(BASE_DIR, "undangan_launching.html"), "w", encoding="utf-8") as f:
    f.write(template)

subfolders = {
    "rudi": {
        "key": "rudi",
        "name": "Yth. Pak Rudi",
        "title": "Komisaris Proxsis Group",
        "short": "Pak Rudi"
    },
    "yumei": {
        "key": "yumei",
        "name": "Yth. Pak Yumei",
        "title": "Komisaris Proxsis Group",
        "short": "Pak Yumei"
    },
    "adit": {
        "key": "adit",
        "name": "Yth. Pak Adit",
        "title": "Presiden Direktur Proxsis Group",
        "short": "Pak Adit"
    },
    "roni": {
        "key": "roni",
        "name": "Yth. Pak Roni",
        "title": "Komisaris Proxsis Group",
        "short": "Pak Roni"
    },
    "bung-jeng": {
        "key": "bungjeng",
        "name": "Yth. Bung & Jeng serta Rekan Partner Proxsis",
        "title": "Seluruh Insan Proxsis Group & Strategic Partners",
        "short": "Bung & Jeng"
    }
}

for folder, data in subfolders.items():
    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Pre-select preset in onload and static HTML
    custom_content = template.replace(
        '<div class="recipient-name" id="displayGuestName">Yth. Bung & Jeng serta Rekan Partner Proxsis</div>',
        f'<div class="recipient-name" id="displayGuestName">{data["name"]}</div>'
    ).replace(
        '<div class="recipient-title" id="displayGuestTitle">Seluruh Insan Proxsis Group & Strategic Partners</div>',
        f'<div class="recipient-title" id="displayGuestTitle">{data["title"]}</div>'
    ).replace(
        '<input type="text" id="rsvpName" class="form-input" required placeholder="Nama Anda (Bung / Jeng / Rekan Partner)">',
        f'<input type="text" id="rsvpName" class="form-input" required value="{data["short"]}">'
    ).replace(
        '<input type="text" id="rsvpRole" class="form-input" required placeholder="cth: Developer / Consultant / PM / Partner">',
        f'<input type="text" id="rsvpRole" class="form-input" required value="{data["title"]}">'
    ).replace(
        "window.onload = checkUrlParams;",
        f"window.onload = function() {{ applyPreset('{data['key']}', false); }};"
    )
    
    target_file = os.path.join(folder_path, "index.html")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(custom_content)
    print(f"Created: {target_file} -> {data['name']} ({data['title']})")

print("All dedicated preset folders updated successfully!")
