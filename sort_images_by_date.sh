#!/bin/bash

# 創建目標分類資料夾
TARGET_DIR=~/Downloads/SortedImagesByDate
mkdir -p "$TARGET_DIR"

# 定義圖片文件的擴展名
IMAGE_EXTENSIONS=("jpg" "jpeg" "png" "gif" "bmp" "tiff")

# 循環遍歷下載資料夾中的所有圖片文件
for ext in "${IMAGE_EXTENSIONS[@]}"; do
    echo "Processing *.$ext files..."
    for file in *.$ext; do
        # 檢查文件是否存在（處理通配符擴展問題）
        if [ -e "$file" ]; then
            echo "Found file: $file"

            # 獲取文件的修改日期
            file_date=$(date -r "$file" "+%Y-%m-%d")

            # 創建對應日期的資料夾
            dest_dir="$TARGET_DIR/$file_date"
            mkdir -p "$dest_dir"
            echo "Created directory: $dest_dir"

            # 移動文件到對應的資料夾
            mv "$file" "$dest_dir"
            echo "Moved $file to $dest_dir"
        else
            echo "No files found for extension: $ext"
        fi
    done
done

