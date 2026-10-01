# Wyckoff / VSA — Đọc hành vi giá và khối lượng

Giáo trình được biên soạn từ khóa học trong dự án **Wickoff VSA**, theo trục:

> **Bối cảnh → giá → Spread → Volume → Effort/Result → Supply/Demand → phản ứng → xác nhận → kịch bản → hành động.**

## Tải sách

- **Kindle 3 / Kindle Keyboard — AZW3:**  
  https://raw.githubusercontent.com/hoangvanthiet86-sketch/Ph-n-t-ch-k-thu-t-theo-ph-ng-ph-p-Wyckoff-VSA-to-n-t-p/main/dist/Wyckoff_VSA_Kindle3.azw3
- **EPUB:**  
  https://raw.githubusercontent.com/hoangvanthiet86-sketch/Ph-n-t-ch-k-thu-t-theo-ph-ng-ph-p-Wyckoff-VSA-to-n-t-p/main/dist/Wyckoff_VSA_Kindle3.epub
- **Báo cáo build:**  
  https://github.com/hoangvanthiet86-sketch/Ph-n-t-ch-k-thu-t-theo-ph-ng-ph-p-Wyckoff-VSA-to-n-t-p/blob/main/dist/BUILD_REPORT.md

Bản AZW3 là bản ưu tiên để chép trực tiếp vào thư mục `documents` của Kindle 3.

## Nội dung

- 8 phần chính
- 40 chương
- 5 phụ lục
- 27 hình/sơ đồ (gồm bìa)
- bài tập và lời giải theo từng chương
- mục lục điện tử nhiều cấp

## Nguyên tắc hình ảnh

Biểu đồ dùng quy ước đen–trắng để đọc tốt trên e-ink:

- nến tăng: thân trắng/rỗng, viền đen;
- nến giảm: thân đen/xám đậm;
- Volume đặt dưới giá khi cần;
- không phụ thuộc màu để hiểu tín hiệu.

Các sơ đồ mô phỏng được ghi rõ là **mô phỏng sư phạm, không phải dữ liệu thị trường thực**.

## Nguồn chỉnh sửa

- `book/book.md` — bản thảo nguồn
- `book/generate_assets.py` — sinh biểu đồ đen–trắng
- `book/kindle.css` — CSS tối ưu ebook
- `.github/workflows/build-ebook.yml` — tự động tạo EPUB/AZW3

Khi chỉnh nội dung nguồn, GitHub Actions sẽ tự build lại sách và cập nhật tệp trong `dist/`.
