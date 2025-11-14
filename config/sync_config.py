# Configuration des dossiers et fichiers à synchroniser/copier

# Dossier source principal
SOURCE_FOLDER = "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes"

# Liste des fichiers et dossiers à copier
SYNC_ITEMS = [
    {
        "type": "folder",
        "source": "plugins"
    },
    {
        "type": "folder",
        "source": "snippets"
    },
    {
        "type": "file",
        "source": "app.json"
    },
    {
        "type": "file",
        "source": "community-plugins.json"
    },
    {
        "type": "file",
        "source": "core-plugins.json"
    },
]

# Dossier de destination pour la synchronisation
DESTINATION_FOLDERS = [
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/COGEP",
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/devlog",
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/emploi",
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/formations",
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/karned",
    "/Users/killian/Library/Mobile Documents/iCloud~md~obsidian/Documents/references",
    ]

# Options de synchronisation
SYNC_OPTIONS = {
    "preserve_timestamps": True,
    "create_backup": True,
    "exclude_patterns": [
        "*.tmp",
        "*.log",
        ".DS_Store"
    ]
}

