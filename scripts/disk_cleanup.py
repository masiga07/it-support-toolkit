import os
import shutil

print("=== DISK CLEANUP TOOL ===")

# Temp directories (Windows)
temp_paths = [
    os.environ.get('TEMP'),
    os.environ.get('TMP')
]

def clean_temp_folder(path):
    if path and os.path.exists(path):
        print(f"\nCleaning: {path}")
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

for path in temp_paths:
    clean_temp_folder(path)

print("\nCleanup complete.")
