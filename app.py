import streamlit as st
from config.sync_config import SYNC_ITEMS, SOURCE_FOLDER, DESTINATION_FOLDERS

st.title("🔄 Obsidian Sync Config")

st.subheader("📋 Fichiers à copier")
for item in SYNC_ITEMS:
    st.text(f"- {item['source']}")

st.subheader("📁 Dossiers")

with st.form("sync_form"):
    source = st.text_input("Source", value=SOURCE_FOLDER)
    destinations = st.text_area("Destinations", value="\n".join(DESTINATION_FOLDERS))

    submitted = st.form_submit_button("Copier")

if submitted:
    import subprocess
    import os

    st.subheader("🚀 Exécution des copies")

    source_folder = source
    dest_list = destinations.strip().split("\n")

    for dest in dest_list:
        dest = dest.strip()
        if dest:
            st.write(f"**Destination: {dest}**")

            # Créer le dossier de destination s'il n'existe pas
            dest_base = os.path.expanduser(f"{dest}/.obsidian")
            os.makedirs(dest_base, exist_ok=True)

            for item in SYNC_ITEMS:
                source_path = os.path.expanduser(f"{source_folder}/.obsidian/{item['source']}")
                dest_path = os.path.expanduser(f"{dest}/.obsidian/{item['source']}")

                try:
                    if item['type'] == 'folder':
                        # Créer le dossier parent de destination
                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                        cmd = ["rsync", "-av", f"{source_path}/", f"{dest_path}/"]
                        result = subprocess.run(cmd, capture_output=True, text=True)

                        if result.returncode == 0:
                            st.success(f"✅ {item['source']} (dossier)")
                        else:
                            st.error(f"❌ {item['source']}: {result.stderr}")
                    else:
                        # Créer le dossier parent de destination
                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                        cmd = ["cp", source_path, dest_path]
                        result = subprocess.run(cmd, capture_output=True, text=True)

                        if result.returncode == 0:
                            st.success(f"✅ {item['source']} (fichier)")
                        else:
                            st.error(f"❌ {item['source']}: {result.stderr}")

                except Exception as e:
                    st.error(f"❌ {item['source']}: {str(e)}")

            st.divider()
