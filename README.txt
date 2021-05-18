Cách sử dụng chương trình:

Nếu bạn muốn sử dụng dữ liệu mới, xin tham khảo các bước sau. Nếu bạn muốn sử dụng dữ liệu có sẵn, xem tiếp dòng 51.

1/Mở File new-input.txt

2/Gõ dữ liệu mong muốn vào file với:

-Hàng đầu tiên ghi các thuộc tính (chú ý mỗi thuộc tính không được phép có dấu cách, nếu không sẽ bị tách thành 2 thuộc tính riêng biệt)

-Các hàng tiếp theo ghi các thông tin của từng đơn vị. Chú ý:

+Các thông tin là case-sensitive, vì vậy khác dù chỉ là chữ in hoa với chữ thường sẽ tạo ra các thông tin khác nhau (Red, red, RED là 3 thông tin hoàn toàn khác nhau)

+Các thông tin phải được ghi theo đúng chính xác thuộc tính tương ứng ở hàng đầu tiên, và số thông tin phải đúng bằng số thuộc tính

-Khi các đơn vị mẫu đã được nhập vào hết, xuống dòng, gõ một dấu "-" (không có ngoặc đôi) và xuống dòng lần nữa

3/Hàng tiếp theo ghi 1 hoặc 2 con số:

+Số đầu tiên là số nguyên, là kích thước mẫu (equivalent sample size)

+Nếu chọn một ước lượng tiền định (priori estimate) cho tất cả các biến cố có điều kiện thì ghi một số thực >=0 và <=1 vào cạnh kích thước mẫu (cách một hoặc nhiều dấu cách). Nếu ước lượng tiền định <0 thì sẽ trở thành 0, >1 thì sẽ trở thành 1. Hoặc dùng ước lượng tiền định riêng biệt cho mỗi biến cố thì bỏ trống, xuống hàng.

4/Các hàng còn lại ghi thông tin của các đơn vị cần được phân lớp, chú ý cách gõ ở mục (2). Tuy nhiên các thuộc tính cần được phân lớp sẽ được thay bằng "-"


Ví dụ: (Không bao gồm ##)


##
Color     Genre        Origin      Customer's_Gender
red       sport        domestic    male      
red       sport        domestic    female    
red       sport        domestic    male      
yellow    sport        domestic    female    
yellow    sport        imported    male      
yellow    traveling    imported    female    
yellow    traveling    imported    male      
yellow    traveling    domestic    female    
red       traveling    imported    female    
red       sport        imported    male
-
3 0.5
red traveling domestic -
yellow -  - female
- - - male
##


Kết quả chương trình và hướng dẫn thêm sẽ được in trong phần hiển thị (vì hạn chế kỹ thuật nên chương trình hiện không có GUI, team ARMY xin chân thành xin lỗi và sẽ xem xét nâng cấp trong tương lai).

##Cảm ơn bạn đã sử dụng sản phẩm của team ARMY##
