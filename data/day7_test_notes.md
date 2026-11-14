# Benchmark test Day 7

## Thiết kế trước khi chạy

Đây là bộ câu hỏi test mới cho 321 chunk strategy B thuộc
collection `thinkpython2_e8412522c5d43b8e`.

Bộ test gồm:
- 5 câu có đáp án trong tài liệu.
- 2 câu không đủ bằng chứng để trả lời.

Không sử dụng lại bộ test cũ của Day 6.

Các câu hỏi khác với bộ dev Day 7 nhưng dùng chung sách,
corpus và có thể trùng trang. Vì vậy, đây là phép chia theo
câu hỏi, không phải phép chia độc lập theo tài liệu hoặc chương.

Bộ test được AI hỗ trợ soạn sau khi chọn cấu hình trên dev
và trước khi chạy retrieval hoặc agent trên các câu này.

Năm đoạn evidence được đối chiếu trực tiếp với corpus.
Mỗi đoạn nằm trọn trong một chunk đúng nguồn và trang.
Không dùng thứ hạng retrieval hoặc câu trả lời của agent
trên test để lựa chọn evidence.

Tác giả cần kiểm tra câu hỏi và lý do thiếu bằng chứng
trước lần chạy đầu tiên.

## Các file đầu vào

- [Bộ test đầy đủ: 5 câu có đáp án và 2 câu thiếu bằng chứng](./day7_test_questions.json).
- [Bộ test chỉ gồm câu có đáp án để đánh giá retrieval](./day7_test_answerable_questions.json).
- [Corpus](./day6_chunks.json).

File đánh giá retrieval chứa đúng 5 câu có đáp án được lấy
từ bộ test đầy đủ.

Các chương trình đánh giá retrieval hiện tại yêu cầu gold
và không hỗ trợ câu thiếu bằng chứng. Không đưa các câu
thiếu bằng chứng vào mẫu số của chỉ số retrieval evidence.

Gold và đáp án chuẩn chỉ dùng để chấm điểm. Chương trình
agent chỉ gửi câu hỏi cho model và công cụ retrieval.

## Cấu hình và cách chấm

Giữ nguyên cấu hình đã chọn:

- Phương pháp: hybrid dense + TF-IDF.
- Hợp nhất thứ hạng bằng RRF.
- Candidate-k: 10 cho mỗi retriever.
- RRF-k: 60.
- Top-k: 3.
- Context budget: 1600 ký tự.
- Tối đa 4 lượt search.
- Tối đa 2 lượt sửa định dạng đầu ra.
- Agent model: `deepseek/deepseek-v4.1-flash-1017`.
- Embedding: model Day 6 đã cố định revision, vector 384 chiều.

Baseline đối chiếu là TF-IDF agent, dùng cùng agent model,
context budget và giới hạn lượt gọi.

Không tạo file khóa cấu hình riêng theo lựa chọn của người dùng.
Tài liệu này ghi lại quyết định trước khi chạy test,
không tự động ngăn code hoặc cấu hình bị thay đổi.

### Đánh giá retrieval

Với 5 câu có đáp án, báo cáo:

- Hit@1.
- Evidence Hit@3.
- Context Evidence Rate.

Đây là đánh giá retrieval một lượt bằng query gốc,
khác với agent có thể viết lại query và tìm nhiều lượt.

### Đánh giá agent

Đọc toàn bộ 5 câu có đáp án và 2 câu thiếu bằng chứng
cho cả baseline và cấu hình được chọn.

- Chấm câu trả lời theo thang 0/1/2.
- Chấm context theo thang 0/1/2.
- Kiểm tra từng citation với context cuối và khẳng định
  mà citation đó hỗ trợ.
- Chấm khả năng từ chối hai yêu cầu thiếu bằng chứng,
  không thêm khẳng định vô căn cứ.

Có thể chấp nhận evidence tương đương nếu ghi rõ
lý do nội dung đó hỗ trợ câu trả lời.

Giữ lại và báo lỗi riêng. Trạng thái `answered`
không đồng nghĩa với câu trả lời đúng.

## Phạm vi các câu thiếu bằng chứng

### test_u01 — Ngoài phạm vi tài liệu đã index

Câu hỏi yêu cầu thông số cấu hình HTTP của OpenRouter
được quy định trong chính tài liệu Think Python.

Kiểm tra toàn bộ corpus không thấy tên OpenRouter.
Kết quả tìm từ khóa chỉ là bằng chứng hỗ trợ,
không phải phép chứng minh tổng quát rằng không có
bằng chứng tương đương về mặt ngữ nghĩa.

Phạm vi sách và yêu cầu cấu hình riêng cho dịch vụ
cũng được đối chiếu khi xác định câu thiếu bằng chứng.

Không được lấy timeout trong code ứng dụng RAG
để làm bằng chứng cho nội dung sách.

### test_u02 — Thiếu phép đo của phiên chạy riêng

Câu hỏi yêu cầu thời gian thực thi cụ thể trên máy
cá nhân của người hỏi nhưng không cung cấp log hoặc phép đo.

Ví dụ và kiến thức về histogram trong sách không đủ
để xác định số mili giây thực đo của lần chạy đó.

## Quy tắc sau khi bắt đầu test

Sau khi đã chạy một trong hai phương pháp trên bộ test:

- Không điều chỉnh hệ thống theo kết quả test rồi báo
  kết quả đó như một đánh giá độc lập.
- Không sửa nhãn để tăng điểm.
- Không âm thầm thay thế câu hỏi.
- Giữ lại lỗi và ghi rõ mọi sửa chữa nhãn thực sự cần thiết.

Nếu kết quả test được dùng để thay đổi hệ thống,
cần bộ test mới cho lần đánh giá độc lập tiếp theo.