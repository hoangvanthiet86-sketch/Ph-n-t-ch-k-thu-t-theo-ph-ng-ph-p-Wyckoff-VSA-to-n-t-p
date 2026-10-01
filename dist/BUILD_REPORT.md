# BUILD REPORT — WYCKOFF / VSA KINDLE 3

- Trạng thái build: **PASS**
- Thiết bị mục tiêu: **Kindle 3 / Kindle Keyboard**
- Số phần chính: **8**
- Số chương: **40**
- Số phụ lục: **5**
- Số bài tập/chương có phần thực hành: **40**
- Số ảnh/sơ đồ được sinh: **27** (gồm bìa)
- Biểu đồ tổng quan chính: **3** (Accumulation phases, Distribution phases, chu kỳ hoàn chỉnh)
- Các hình còn lại: biểu đồ phóng to/so sánh/sơ đồ sư phạm/bài tập
- Mục lục điện tử: **Có**, nhiều cấp do Pandoc tạo
- Liên kết nội bộ: **Có** qua mục lục EPUB/AZW3
- EPUB ZIP validation: **PASS**
- AZW3 metadata read: **PASS**
- AZW3 format: **Mobipocket/KF8 version 8, UTF-8**
- Chương được đánh dấu giới hạn nguồn: **Chương 21** và một phần **Chương 40**
- Biểu đồ cuối: dùng quy ước đen–trắng, nến tăng rỗng/trắng, nến giảm đen; không phụ thuộc màu
- Các hình mô phỏng đều ghi rõ: **không phải dữ liệu thị trường thực**

## Tệp xuất bản

- `dist/Wyckoff_VSA_Kindle3.azw3` — bản ưu tiên để chép trực tiếp vào Kindle 3
- `dist/Wyckoff_VSA_Kindle3.epub` — bản nguồn/đọc trên phần mềm hỗ trợ EPUB
- `book/book.md` — bản thảo nguồn để sửa theo góp ý từng chương

## Kiểm tra bố cục

- Không phát hiện lỗi đóng gói EPUB.
- Ảnh được đặt độc lập trong luồng nội dung và co theo chiều rộng màn hình.
- Các hình nhiều panel (đặc biệt phần Volume/Absorption) nên được kiểm tra thực tế thêm trên Kindle 3; nếu người đọc thấy chữ nhỏ, phiên bản sau sẽ tách thành nhiều hình phóng to.
