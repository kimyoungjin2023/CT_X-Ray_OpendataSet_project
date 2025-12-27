import zipfile
import os
import shutil

ROOT_DIR = r"C:\Users\kyoun\Downloads\085.주요질환 이미지 합성데이터(X-ray)"
OUTPUT_DIR = ROOT_DIR + "_extracted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def safe_extract_zip(zip_path, extract_root):
    zip_name = os.path.splitext(os.path.basename(zip_path))[0]
    extract_path = os.path.join(extract_root, zip_name)
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            filename = os.path.basename(member.filename)
            if not filename:
                continue

            source = zip_ref.open(member)
            target_file = os.path.join(extract_path, filename)

            with open(target_file, "wb") as target:
                shutil.copyfileobj(source, target)

def walk_and_extract(base_dir, output_dir):
    for root, dirs, files in os.walk(base_dir):
        rel_path = os.path.relpath(root, base_dir)
        target_root = os.path.join(output_dir, rel_path)
        os.makedirs(target_root, exist_ok=True)

        for file in files:
            if file.lower().endswith(".zip"):
                zip_path = os.path.join(root, file)
                print(f"▶ 압축 해제: {zip_path}")
                safe_extract_zip(zip_path, target_root)

walk_and_extract(ROOT_DIR, OUTPUT_DIR)

print("✅ Training / Validation 전체 압축 해제 완료")
