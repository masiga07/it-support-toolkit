import os
import shutil

print("=== DISK CLEANUP TOOL ===")

# Remove duplicates using set()
temp_paths = list(set([
    os.environ.get('TEMP'),
    os.environ.get('TMP')
]))

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
                print(f"Could not delete {file_path}: {e}")

for path in temp_paths:
    clean_temp_folder(path)

print("\nCleanup complete.")