# Điều chỉnh evidence của bộ dev Day 6 cho Day 7

15 câu hỏi dev được chuyển từ Day 6 sang Day 7.
Câu hỏi, đáp án chuẩn, source ID và số trang được giữ nguyên.
Không sử dụng nhãn test trong quá trình điều chỉnh.

Các nhãn gốc vẫn được lưu trong repository Day 6.

## Lý do điều chỉnh

Baseline Day 7 yêu cầu mỗi evidence thay thế phải nằm trọn
trong một chunk.

Ba đoạn trích được chuyển từ Day 6 bị cắt qua ranh giới
các chunk strategy B. Vì vậy, chúng được thay bằng các
đoạn trích nguyên văn tương đương đã đối chiếu với
[day6_chunks.json](./day6_chunks.json).

Việc lựa chọn đoạn thay thế được thực hiện trước lần
benchmark retrieval Day 7 chạy thành công đầu tiên,
không dựa vào thứ hạng kết quả retrieval.

## Các thay đổi

| Câu hỏi | Nội dung điều chỉnh | Chunk hỗ trợ |
|---|---|---|
| q08 | Giữ evidence trang 106. Thay evidence thay thế ở trang 107 bằng phần giải thích và cách cài đặt tương đương sử dụng uses_only trên cùng trang. | d5286a35b8295c70831a21d22ef13cd6 |
| q12 | Dùng ví dụ delimiter.join(t) và phần giải thích delimiter ở trang 117. | e9cb1a022110108f4b7b88897c3a17ab |
| q13 | Dùng phần phân biệt object equivalent và identical, cùng ví dụ về giá trị của list ở trang 118. | d47d0792b790af695fbd82c66b898760 |

## Phạm vi và giới hạn

Đây là các nhãn dev được điều chỉnh cho phiên bản corpus
đang sử dụng, không phải một bộ nhãn được chấm độc lập.

Tác giả cần kiểm tra lại nội dung các đoạn thay thế
để xác nhận chúng thực sự hỗ trợ đáp án.

Baseline sử dụng chỉ số evidence nằm trong một chunk.
Vì vậy, bằng chứng hợp lệ nhưng nằm rải qua nhiều chunk
có thể không được ghi nhận bởi chỉ số này.

Khi bổ sung cơ chế sử dụng nhiều chunk làm bằng chứng,
cần đánh giá riêng và mô tả rõ cách xác định đủ evidence.