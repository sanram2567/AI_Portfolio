import os

def audit_project(root_dir="."):
    print(f"--- AI Portfolio Project Audit ---")
    print(f"Target Directory: {os.path.abspath(root_dir)}\n")

    file_counts = {}
    ignored_items = []
    tracked_items = []

    # Common folders/files to check for
    important_checkpoints = {
        '.git': 'Git Repository Initialized',
        '.gitignore': 'Git Ignore File Present',
        'ai_portfolio': 'Virtual Environment (Local)',
        'ingest.py': 'Data Ingestion Script'
    }

    print("Checking Checkpoints:")
    for item, description in important_checkpoints.items():
        exists = os.path.exists(os.path.join(root_dir, item))
        status = "✅ Found" if exists else "❌ Missing"
        print(f"{status}: {item} ({description})")

    print("\nFile Distribution:")
    for root, dirs, files in os.walk(root_dir):
        # Skip the virtual env folder to avoid thousands of lines of output
        if 'ai_portfolio' in dirs:
            dirs.remove('ai_portfolio')
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            ext = os.path.splitext(file)[1] or "No Extension"
            file_counts[ext] = file_counts.get(ext, 0) + 1
            
    for ext, count in file_counts.items():
        print(f"  {ext}: {count} files")

    print("\n--- Audit Complete ---")

if __name__ == "__main__":
    audit_project()