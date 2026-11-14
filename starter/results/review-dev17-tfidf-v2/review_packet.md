# Phiếu đối chiếu câu trả lời

Đọc context cuối, không chỉ kiểm tra ID citation.
Gold là nhãn tham chiếu, không thay thế việc đọc evidence.

## q01

**Câu hỏi:** Chỉ số âm trong chuỗi đếm từ phía nào?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Chỉ số âm trong chuỗi đếm ngược từ **cuối chuỗi**. Chẳng hạn, `fruit[-1]` là ký tự cuối cùng, `fruit[-2]` là ký tự áp chót, v.v. [b1ab56c6426c8ed5ec9282c015f74d93]

**Đáp án tham chiếu:**
Chỉ số âm đếm ngược từ cuối chuỗi.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 94,
    "evidence": "Or you can use negative indices, which count backward from the end of the string."
  }
]

**Citations theo thứ tự cần chấm:**
["b1ab56c6426c8ed5ec9282c015f74d93"]

**Context cuối thực sự gửi cho model:**
[334b2d4da22931849c908c9c39400704 | starter\data\raw\thinkpython2.pdf | page 112]
indices:

[cc73c22ea95cf096bf81436e92e9e46d | starter\data\raw\thinkpython2.pdf | page 132]
Here’s an example that tries to update a global variable:
count = 0
def example3():
count = count + 1 # WRONG
If you run it you get:

[b1ab56c6426c8ed5ec9282c015f74d93 | starter\data\raw\thinkpython2.pdf | page 94]
you have to subtract 1 fromlength:
>>> last = fruit[length-1]
>>> last
'a'
Or you can use negative indices, which count backward from the end of the string. The
expressionfruit[-1]yields the last letter,fruit[-2]yields the second to last, and so on.

**Các query đã tìm:**
[
  "negative indices string count from which side Python"
]

## q02

**Câu hỏi:** Điều gì xảy ra khi dùng số thực làm chỉ số để truy cập một ký tự trong chuỗi?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi dùng số thực làm chỉ số để truy cập một ký tự trong chuỗi, chương trình sẽ báo lỗi `TypeError: string indices must be integers`, vì chỉ số phải là số nguyên. Ví dụ: `fruit[1.5]` gây ra lỗi này [8ee3c32328f6b12af88d43507d83ef0b].

**Đáp án tham chiếu:**
Python báo TypeError vì chỉ số chuỗi phải là số nguyên.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 94,
    "evidence": "But the value of the index has to be an integer. Otherwise you get:\n>>> letter = fruit[1.5]\nTypeError: string indices must be integers"
  }
]

**Citations theo thứ tự cần chấm:**
["8ee3c32328f6b12af88d43507d83ef0b"]

**Context cuối thực sự gửi cho model:**
[8ee3c32328f6b12af88d43507d83ef0b | starter\data\raw\thinkpython2.pdf | page 94]
72 Chapter 8. Strings
But the value of the index has to be an integer. Otherwise you get:
>>> letter = fruit[1.5]
TypeError: string indices must be integers

[334b2d4da22931849c908c9c39400704 | starter\data\raw\thinkpython2.pdf | page 112]
indices:

[20514956c53e7e2324eed17fc381b325 | starter\data\raw\thinkpython2.pdf | page 96]
8.6 Searching
What does the following function do?
def find(word, letter):
index = 0
while index < len(word):
if word[index] == letter:
return index
index = index + 1
return -1

[04084172735c5d947369bbf5b000e7c5 | starter\data\raw\thinkpython2.pdf | page 93]
8.1 A string is a sequence
A string is a sequence of characters. You can access the characters one at a time with the
bracket operator:
>>> fruit ='banana'
>>> letter = fruit[1]
The second statement selects character number 1 fromfruitand assigns it toletter.
The expression in brackets is called anindex. The index indicates which character in the
sequence you want (hence the name).
But you might not get what you expect:
>>> letter
'a'

[81ccf3e8fe35b6643957666b728e4f5f | starter\data\raw\thinkpython2.pdf | page 102]
a string).

**Các query đã tìm:**
[
  "what happens when you use a float as an index to access a character in a string TypeError",
  "string indices must be integers float index TypeError Think Python"
]

## q03

**Câu hỏi:** Vì sao không thể thay một ký tự của chuỗi bằng cách gán vào vị trí của ký tự đó?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không thể gán vào một vị trí ký tự của chuỗi vì chuỗi trong Python là **bất biến** (*immutable*): không thể thay đổi một chuỗi đã tồn tại. Cách tốt nhất là tạo một chuỗi mới dựa trên chuỗi ban đầu, chẳng hạn bằng cách nối một ký tự mới với một lát cắt của chuỗi cũ. Việc này không làm thay đổi chuỗi gốc [4875fc67f0e705fb95180f1679231936].

**Đáp án tham chiếu:**
Chuỗi là immutable nên không thể thay đổi một chuỗi đã tồn tại; cần tạo chuỗi mới.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 96,
    "evidence": "The reason for the error is that strings areimmutable, which means you can’t change an\nexisting string. The best you can do is create a new string that is a variation on the original:"
  }
]

**Citations theo thứ tự cần chấm:**
["4875fc67f0e705fb95180f1679231936"]

**Context cuối thực sự gửi cho model:**
[4875fc67f0e705fb95180f1679231936 | starter\data\raw\thinkpython2.pdf | page 96]
The reason for the error is that strings areimmutable, which means you can’t change an
existing string. The best you can do is create a new string that is a variation on the original:
>>> greeting ='Hello, world!'
>>> new_greeting ='J'+ greeting[1:]
>>> new_greeting
'Jello, world!'
This example concatenates a new first letter onto a slice ofgreeting. It has no effect on the
original string.

[81ccf3e8fe35b6643957666b728e4f5f | starter\data\raw\thinkpython2.pdf | page 102]
a string).

[bff571429fa1b7f66b52d2374846e72c | starter\data\raw\thinkpython2.pdf | page 143]
To start with the obvious, strings are more limited than other sequences because the ele-
ments have to be characters. They are also immutable. If you need the ability to change the
characters in a string (as opposed to creating a new string), you might want to use a list of
characters instead.
Lists are more common than tuples, mostly because they are mutable. But there are a few
cases where you might prefer tuples:

[f73ef73a0e8d3e115bc34eca0c673127 | starter\data\raw\thinkpython2.pdf | page 132]
ofbeen_calleddoesn’t change. The problem

[5e048c8083c695feb778ef2034652d2a | starter\data\raw\thinkpython2.pdf | page 144]
12.9 Glossary
tuple:An immutable sequence of elements.
tuple assignment:An assignment with a sequence on the right side and a tuple of vari-
ables on the left. The right side is evaluated and then its elements are assigned to the
variables on the left.

**Các query đã tìm:**
[
  "strings immutable cannot change character assignment item assignment string",
  "\"Strings are immutable\" \"create a new string\" variation original"
]

## q04

**Câu hỏi:** Trong chương 8, vị trí kết thúc truyền cho phương thức find có được tính vào phạm vi tìm kiếm không?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không. Vị trí kết thúc (chỉ số thứ hai) truyền cho `find` **không** được tính vào phạm vi tìm kiếm: phương thức tìm "đến nhưng không bao gồm" chỉ số thứ hai, nhờ đó `find` nhất quán với toán tử slice. Ví dụ `name.find('b', 1, 2)` trả về `-1` vì `'b'` không xuất hiện trong khoảng chỉ số từ 1 đến 2, không tính 2 [8244e78c77b3fdf58c0397a2f7b4d1ba].

**Đáp án tham chiếu:**
Không. Phạm vi tìm kiếm không bao gồm vị trí kết thúc.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 98,
    "evidence": "This search fails becausebdoes not appear in the index range from1to2, not including2.\nSearching up to, but not including, the second index makesfindconsistent with the slice\noperator."
  }
]

**Citations theo thứ tự cần chấm:**
["8244e78c77b3fdf58c0397a2f7b4d1ba"]

**Context cuối thực sự gửi cho model:**
[9c5406cb13323226c0e7813d7babfca3 | starter\data\raw\thinkpython2.pdf | page 98]
76 Chapter 8. Strings
This form of dot notation specifies the name of the method,upper, and the name of the
string to apply the method to,word. The empty parentheses indicate that this method
takes no arguments.
A method call is called aninvocation; in this case, we would say that we are invoking
upperonword.
As it turns out, there is a string method namedfindthat is remarkably similar to the
function we wrote:
>>> word ='banana'
>>> index = word.find('a')
>>> index
1

[8244e78c77b3fdf58c0397a2f7b4d1ba | starter\data\raw\thinkpython2.pdf | page 98]
>>> name.find('b', 1, 2)
-1
This search fails becausebdoes not appear in the index range from1to2, not including2.
Searching up to, but not including, the second index makesfindconsistent with the slice
operator.

[391cf24dff20530b698f1bb9983b332e | starter\data\raw\thinkpython2.pdf | page 123]
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary
(the book, not the data structure). You start in the middle and check to see whether the word you are
looking for comes before the word in the middle of the list. If so, you search the first half of the list
the same way. Otherwise you search the second half.

**Các query đã tìm:**
[
  "find method start end position search range Chapter 8"
]

## q05

**Câu hỏi:** Sách đề xuất cách nào để giảm khác biệt hoa/thường trước khi so sánh các chuỗi?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Sách đề xuất chuyển các chuỗi về một định dạng chuẩn — ví dụ tất cả thành chữ thường (all lowercase) — trước khi thực hiện phép so sánh [76b7668e999719557d3c86953956b275]. Lý do là Python không xử lý chữ hoa/chữ thường giống con người: mọi chữ cái hoa đứng trước mọi chữ cái thường, nên việc so sánh trực tiếp có thể cho kết quả trái với mong đợi, chẳng hạn "Pineapple" được xem là đứng trước "banana" [41403b5428dc8469445383ec32dcc679] [76b7668e999719557d3c86953956b275].

**Đáp án tham chiếu:**
Chuyển các chuỗi về cùng một định dạng, chẳng hạn chuyển tất cả sang chữ thường, trước khi so sánh.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 99,
    "evidence": "A common way to address this problem is to convert strings to a standard format, such as\nall lowercase, before performing the comparison."
  }
]

**Citations theo thứ tự cần chấm:**
["76b7668e999719557d3c86953956b275", "41403b5428dc8469445383ec32dcc679"]

**Context cuối thực sự gửi cho model:**
[18edaf2d96821ff802e014131e5eaed9 | starter\data\raw\thinkpython2.pdf | page 138]
work with tuples and other sequences; Python starts by comparing

[76b7668e999719557d3c86953956b275 | starter\data\raw\thinkpython2.pdf | page 99]
uppercase letters come before all the lowercase letters, so:
Your word, Pineapple, comes before banana.
A common way to address this problem is to convert strings to a standard format, such as
all lowercase, before performing the comparison. Keep that in mind in case you have to
defend yourself against a man armed with a Pineapple.

[41403b5428dc8469445383ec32dcc679 | starter\data\raw\thinkpython2.pdf | page 99]
bananas.')
Python does not handle uppercase and lowercase letters the same way people do. All the

**Các query đã tìm:**
[
  "case differences comparing strings lowercase"
]

## q06

**Câu hỏi:** Phương thức nào của file object đọc các ký tự đến ký tự xuống dòng và trả về một chuỗi?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Đó là phương thức **`readline`**. Phương thức này đọc các ký tự từ file cho đến khi gặp ký tự xuống dòng (newline) và trả về kết quả dưới dạng một chuỗi [913eb0b827a2af56f2a765320ab9c2b7]. File object cũng ghi nhớ vị trí đọc trong file, nên nếu gọi `readline` lần nữa sẽ nhận được phần tiếp theo [a41f3bb6b7c607d9a52edf9d4a404ab4].

**Đáp án tham chiếu:**
Phương thức readline().

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 105,
    "evidence": "The file object provides several\nmethods for reading, includingreadline, which reads characters from the file until it gets\nto a newline and returns the result as a string:"
  }
]

**Citations theo thứ tự cần chấm:**
["913eb0b827a2af56f2a765320ab9c2b7", "a41f3bb6b7c607d9a52edf9d4a404ab4"]

**Context cuối thực sự gửi cho model:**
[913eb0b827a2af56f2a765320ab9c2b7 | starter\data\raw\thinkpython2.pdf | page 105]
finis a common name for a file object used for input. The file object provides several
methods for reading, includingreadline, which reads characters from the file until it gets
to a newline and returns the result as a string:
>>> fin.readline()
'aa\n'
The first word in this particular list is “aa”, which is a kind of lava. The sequence\n
represents the newline character that separates this word from the next.

[a41f3bb6b7c607d9a52edf9d4a404ab4 | starter\data\raw\thinkpython2.pdf | page 105]
The file object keeps track of where it is in the file, so if you callreadlineagain, you get
the next word:
>>> fin.readline()
'aah\n'

[8920d2aae123a058638216dffb4d2b8f | starter\data\raw\thinkpython2.pdf | page 118]
object.

**Các query đã tìm:**
[
  "file object method reads characters until newline returns string readline"
]

## q07

**Câu hỏi:** Trong ví dụ đọc danh sách từ, sách dùng phương thức nào để bỏ ký tự xuống dòng khỏi dòng vừa đọc?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Sách dùng phương thức chuỗi `strip` để loại bỏ ký tự xuống dòng khỏi dòng vừa đọc, ví dụ `word = line.strip()` [0d2e210930428930c52375dd962f1186]. Trong chương trình đọc `words.txt` và in từng từ, sách cũng minh họa tương tự với `word = line.strip()` [0e0e5c6e2351d8abed9d5c8404dcba46].

**Đáp án tham chiếu:**
Dùng phương thức strip() trên chuỗi vừa đọc, như word = line.strip().

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 106,
    "evidence": "Or, if it’s the newline character that’s bothering you, we can get rid of it with the\nstring methodstrip:\n>>> line = fin.readline()\n>>> word = line.strip()"
  }
]

**Citations theo thứ tự cần chấm:**
["0d2e210930428930c52375dd962f1186", "0e0e5c6e2351d8abed9d5c8404dcba46"]

**Context cuối thực sự gửi cho model:**
[0e0e5c6e2351d8abed9d5c8404dcba46 | starter\data\raw\thinkpython2.pdf | page 106]
open('words.txt')
for line in fin:
word = line.strip()
print(word)

[0d2e210930428930c52375dd962f1186 | starter\data\raw\thinkpython2.pdf | page 106]
84 Chapter 9. Case study: word play
The next word is “aah”, which is a perfectly legitimate word, so stop looking at me like
that. Or, if it’s the newline character that’s bothering you, we can get rid of it with the
string methodstrip:
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'
You can also use a file object as part of aforloop. This program readswords.txtand
prints each word, one per line:
fin =

[9c5406cb13323226c0e7813d7babfca3 | starter\data\raw\thinkpython2.pdf | page 98]
76 Chapter 8. Strings
This form of dot notation specifies the name of the method,upper, and the name of the
string to apply the method to,word. The empty parentheses indicate that this method
takes no arguments.
A method call is called aninvocation; in this case, we would say that we are invoking
upperonword.
As it turns out, there is a string method namedfindthat is remarkably similar to the
function we wrote:
>>> word ='banana'
>>> index = word.find('a')
>>> index
1

**Các query đã tìm:**
[
  "read list of words strip newline from line method"
]

## q08

**Câu hỏi:** Hàm uses_all trả về True khi từ đầu vào đáp ứng điều kiện nào đối với các ký tự required?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Hàm `uses_all(word, required)` trả về `True` nếu từ `word` sử dụng **tất cả các ký tự trong chuỗi `required` ít nhất một lần** [0d52e4dc4e3409b706503f63aa699aea]. Cách cài đặt duyệt qua từng ký tự trong `required`: nếu có ký tự nào không xuất hiện trong `word` thì trả về `False`; nếu tất cả đều xuất hiện thì trả về `True` [50d3699021a4cdd41f6e335447b0f1b6]. Tương đương, có thể viết `return uses_only(required, word)` [d5286a35b8295c70831a21d22ef13cd6].

**Đáp án tham chiếu:**
Từ phải chứa tất cả các ký tự trong required ít nhất một lần; thiếu bất kỳ ký tự bắt buộc nào thì trả về False.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 106,
    "evidence": "Exercise 9.5.Write a function nameduses_allthat takes a word and a string of required letters,\nand that returnsTrueif the word uses all the required letters at least once."
  },
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 107,
    "evidence": "Instead of traversing the letters inword, the loop traverses the required letters. If any of the\nrequired letters do not appear in the word, we can returnFalse.\nIf you were really thinking like a computer scientist, you would have recognized that\nuses_allwas an instance of a previously solved problem, and you would have written:\ndef uses_all(word, required):\nreturn uses_only(required, word)"
  }
]

**Citations theo thứ tự cần chấm:**
["0d52e4dc4e3409b706503f63aa699aea", "50d3699021a4cdd41f6e335447b0f1b6", "d5286a35b8295c70831a21d22ef13cd6"]

**Context cuối thực sự gửi cho model:**
[d5286a35b8295c70831a21d22ef13cd6 | starter\data\raw\thinkpython2.pdf | page 107]
return False
return True
Instead of traversing the letters inword, the loop traverses the required letters. If any of the
required letters do not appear in the word, we can returnFalse.
If you were really thinking like a computer scientist, you would have recognized that
uses_allwas an instance of a previously solved problem, and you would have written:
def uses_all(word, required):
return uses_only(required, word)

[50d3699021a4cdd41f6e335447b0f1b6 | starter\data\raw\thinkpython2.pdf | page 107]
uses_onlyis similar except that the sense of the condition is reversed:
def uses_only(word, available):
for letter in word:
if letter not in available:
return False
return True
Instead of a list of forbidden letters, we have a list of available letters. If we find a letter in
wordthat is not inavailable, we can returnFalse.
uses_allis similar except that we reverse the role of the word and the string of letters:
def uses_all(word, required):
for letter in required:
if letter not in

[0d52e4dc4e3409b706503f63aa699aea | starter\data\raw\thinkpython2.pdf | page 106]
that returnsTrueif the word contains only letters in the list. Can you make a sentence using only
the lettersacefhlo? Other than “Hoe alfalfa”?
Exercise 9.5.Write a function nameduses_allthat takes a word and a string of required letters,
and that returnsTrueif the word uses all the required letters at least once. How many words are
there that use all the vowelsaeiou? How aboutaeiouy?
Exercise 9.6.Write a function calledis_abecedarianthat

**Các query đã tìm:**
[
  "uses_all function returns True word required letters"
]

## q09

**Câu hỏi:** List khác string như thế nào về khả năng thay đổi phần tử?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
**String là bất biến (immutable)**, nên không thể thay đổi một ký tự bằng cách gán vào vị trí chỉ số. Ví dụ, `greeting[0] = 'J'` sẽ gây lỗi `TypeError: 'str' object does not support item assignment` [2bae53eeca782ab89f45628641cf0045]. **List là khả biến (mutable)**, nên có thể cập nhật/thay đổi giá trị của từng phần tử bằng câu lệnh gán theo chỉ số [9d84fa5418149d6955687fe552a97c59]. Chính vì list mutable, tài liệu cũng lưu ý rằng thường nên tạo bản sao trước khi thực hiện các thao tác làm thay đổi list [78260012feafeb8d03177df4fc4b03c6].

**Đáp án tham chiếu:**
List là mutable, có thể thay đổi phần tử tại chỗ; string thì không.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 112,
    "evidence": "Unlike strings, lists are mutable. When the bracket operator appears on the left side of an\nassignment, it identifies the element of the list that will be assigned."
  }
]

**Citations theo thứ tự cần chấm:**
["2bae53eeca782ab89f45628641cf0045", "9d84fa5418149d6955687fe552a97c59", "78260012feafeb8d03177df4fc4b03c6"]

**Context cuối thực sự gửi cho model:**
[78260012feafeb8d03177df4fc4b03c6 | starter\data\raw\thinkpython2.pdf | page 114]
both, the slice is a copy of the whole list.
>>> t[:]
['a','b','c','d','e','f']
Since lists are mutable, it is often useful to make a copy before performing operations that
modify lists.

[20514956c53e7e2324eed17fc381b325 | starter\data\raw\thinkpython2.pdf | page 96]
8.6 Searching
What does the following function do?
def find(word, letter):
index = 0
while index < len(word):
if word[index] == letter:
return index
index = index + 1
return -1

[9d84fa5418149d6955687fe552a97c59 | starter\data\raw\thinkpython2.pdf | page 113]
This loop traverses the list and updates each element.lenreturns the number of elements
in the list.rangereturns a list of indices from 0 ton−1, wherenis the length of the list.
Each time through the loopigets the index of the next element. The assignment statement
in the body usesito read the old value of the element and to assign the new value.
Aforloop over an empty list never runs the body:
for x in []:
print('This never happens.')

[2bae53eeca782ab89f45628641cf0045 | starter\data\raw\thinkpython2.pdf | page 96]
8.5 Strings are immutable
It is tempting to use the[]operator on the left side of an assignment, with the intention of
changing a character in a string. For example:
>>> greeting ='Hello, world!'
>>> greeting[0] ='J'
TypeError:'str'object does not support item assignment
The “object” in this case is the string and the “item” is the character you tried to assign.
For now, an object is the same thing as a value, but we will refine that definition later
(Section

**Các query đã tìm:**
[
  "list mutable, string immutable elements cannot be modified",
  "strings are immutable item assignment TypeError list item can be changed",
  "lists are mutable modify element assign list index"
]

## q10

**Câu hỏi:** Trong chương 10, vì sao phép gán t = t.sort() gây kết quả không mong muốn?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Vì `sort` là một phương thức “void”: nó sắp xếp danh sách tại chỗ nhưng trả về `None`. Do đó, khi viết `t = t.sort()`, biến `t` bị gán thành `None` thay vì giữ tham chiếu đến danh sách đã được sắp xếp, dẫn đến kết quả không mong muốn [e837a534a33c9d9c42c4f293bf000344].

**Đáp án tham chiếu:**
sort() sửa list tại chỗ và trả về None, vì vậy phép gán làm t trở thành None.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 114,
    "evidence": "Most list methods are void; they modify the list and returnNone. If you accidentally write\nt = t.sort(), you will be disappointed with the result."
  },
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 121,
    "evidence": "t = t.sort() # WRONG!\nBecausesortreturnsNone, the next operation you perform withtis likely to fail."
  }
]

**Citations theo thứ tự cần chấm:**
["e837a534a33c9d9c42c4f293bf000344"]

**Context cuối thực sự gửi cho model:**
[e837a534a33c9d9c42c4f293bf000344 | starter\data\raw\thinkpython2.pdf | page 114]
['a','b','c','d','e']
Most list methods are void; they modify the list and returnNone. If you accidentally write
t = t.sort(), you will be disappointed with the result.

[821667ea2b810277e5a13f9c5e1b490e | starter\data\raw\thinkpython2.pdf | page 114]
t1.extend(t2)
>>> t1
['a','b','c','d','e']
This example leavest2unmodified.
sortarranges the elements of the list from low to high:
>>> t = ['d','c','e','b','a']
>>> t.sort()
>>> t

[4ca5eefcf886891e1c9937552e810a06 | starter\data\raw\thinkpython2.pdf | page 96]
10.10).

**Các query đã tìm:**
[
  "Think Python Chapter 10 t = t.sort() sort returns None"
]

## q11

**Câu hỏi:** Phương thức pop() của list làm gì khi không truyền chỉ số?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi không truyền chỉ số, `pop()` sẽ xóa và trả về phần tử cuối cùng của list (đồng thời làm thay đổi list đó) [358ace752b82138a0af81e54d86037d6].

**Đáp án tham chiếu:**
Xóa và trả về phần tử cuối cùng của list.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 116,
    "evidence": "popmodifies the list and returns the element that was removed. If you don’t provide an\nindex, it deletes and returns the last element."
  }
]

**Citations theo thứ tự cần chấm:**
["358ace752b82138a0af81e54d86037d6"]

**Context cuối thực sự gửi cho model:**
[358ace752b82138a0af81e54d86037d6 | starter\data\raw\thinkpython2.pdf | page 116]
10.8 Deleting elements
There are several ways to delete elements from a list. If you know the index of the element
you want, you can usepop:
>>> t = ['a','b','c']
>>> x = t.pop(1)
>>> t
['a','c']
>>> x
'b'
popmodifies the list and returns the element that was removed. If you don’t provide an
index, it deletes and returns the last element.
If you don’t need the removed value, you can use thedeloperator:
>>> t =

[9c5406cb13323226c0e7813d7babfca3 | starter\data\raw\thinkpython2.pdf | page 98]
76 Chapter 8. Strings
This form of dot notation specifies the name of the method,upper, and the name of the
string to apply the method to,word. The empty parentheses indicate that this method
takes no arguments.
A method call is called aninvocation; in this case, we would say that we are invoking
upperonword.
As it turns out, there is a string method namedfindthat is remarkably similar to the
function we wrote:
>>> word ='banana'
>>> index = word.find('a')
>>> index
1

[20514956c53e7e2324eed17fc381b325 | starter\data\raw\thinkpython2.pdf | page 96]
8.6 Searching
What does the following function do?
def find(word, letter):
index = 0
while index < len(word):
if word[index] == letter:
return index
index = index + 1
return -1

**Các query đã tìm:**
[
  "list pop() method without index removes last element"
]

## q12

**Câu hỏi:** Muốn ghép một list các chuỗi thành một chuỗi bằng delimiter, dùng phương thức nào và gọi trên đối tượng nào?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Dùng phương thức `join`, gọi trên chuỗi delimiter (dấu phân cách) và truyền list các chuỗi làm đối số. Ví dụ: `delimiter = ' '` rồi `s = delimiter.join(t)` với `t = ['pining', 'for', 'the', 'fjords']`, kết quả là `'pining for the fjords'`. Nếu muốn nối mà không có khoảng trắng, dùng chuỗi rỗng `''` làm delimiter [060dff8e3159ea9152799639bb68c2eb] [e9cb1a022110108f4b7b88897c3a17ab].

**Đáp án tham chiếu:**
Dùng join(), gọi trên chuỗi delimiter và truyền list làm đối số: delimiter.join(list_chuoi).

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 117,
    "evidence": ">>> s = delimiter.join(t)\n>>> s\n'pining for the fjords'\nIn this case the delimiter is a space character, sojoinputs a space between words. To\nconcatenate strings without spaces, you can use the empty string,'', as a delimiter."
  }
]

**Citations theo thứ tự cần chấm:**
["060dff8e3159ea9152799639bb68c2eb", "e9cb1a022110108f4b7b88897c3a17ab"]

**Context cuối thực sự gửi cho model:**
[e9cb1a022110108f4b7b88897c3a17ab | starter\data\raw\thinkpython2.pdf | page 117]
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
In this case the delimiter is a space character, sojoinputs a space between words. To
concatenate strings without spaces, you can use the empty string,'', as a delimiter.

[060dff8e3159ea9152799639bb68c2eb | starter\data\raw\thinkpython2.pdf | page 117]
on the delimiter and pass the list as a parameter:
>>> t = ['pining','for','the','fjords']
>>> delimiter =' '

[9c5406cb13323226c0e7813d7babfca3 | starter\data\raw\thinkpython2.pdf | page 98]
76 Chapter 8. Strings
This form of dot notation specifies the name of the method,upper, and the name of the
string to apply the method to,word. The empty parentheses indicate that this method
takes no arguments.
A method call is called aninvocation; in this case, we would say that we are invoking
upperonword.
As it turns out, there is a string method namedfindthat is remarkably similar to the
function we wrote:
>>> word ='banana'
>>> index = word.find('a')
>>> index
1

**Các query đã tìm:**
[
  "join list of strings with delimiter string method"
]

## q13

**Câu hỏi:** Hai list chứa cùng các phần tử có nhất thiết phải là cùng một object không?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không nhất thiết. Hai list có cùng các phần tử thì được xem là có **cùng giá trị**, nhưng không nhất thiết là **cùng một object**; hai object tương đương không bắt buộc phải identical [d47d0792b790af695fbd82c66b898760]. Chúng chỉ cùng object khi một biến được gán bằng biến kia, ví dụ `b = a`, tức là có aliasing [f7948d3f5018303dcd6369324d75fba1].

**Đáp án tham chiếu:**
Không. Hai list có thể equivalent vì cùng giá trị nhưng không identical vì là hai object khác nhau.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 118,
    "evidence": "If two objects are identical,\nthey are also equivalent, but if they are equivalent, they are not necessarily identical.\nUntil now, we have been using “object” and “value” interchangeably, but it is more precise\nto say that an object has a value. If you evaluate[1, 2, 3], you get a list object whose\nvalue is a sequence of integers."
  }
]

**Citations theo thứ tự cần chấm:**
["d47d0792b790af695fbd82c66b898760", "f7948d3f5018303dcd6369324d75fba1"]

**Context cuối thực sự gửi cho model:**
[d47d0792b790af695fbd82c66b898760 | starter\data\raw\thinkpython2.pdf | page 118]
ements, but notidentical, because they are not the same object. If two objects are identical,
they are also equivalent, but if they are equivalent, they are not necessarily identical.
Until now, we have been using “object” and “value” interchangeably, but it is more precise
to say that an object has a value. If you evaluate[1, 2, 3], you get a list object whose
value is a sequence of integers. If another list has the same elements, we say it has the
same value, but it is not the same

[f7948d3f5018303dcd6369324d75fba1 | starter\data\raw\thinkpython2.pdf | page 118]
10.11 Aliasing
Ifarefers to an object and you assignb = a, then both variables refer to the same object:
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
The state diagram looks like Figure 10.4.
The association of a variable with an object is called areference. In this example, there are
two references to the same object.
An object with more than one reference has more than one name, so we say that the object
isaliased.
If the aliased object is mutable, changes made with one alias affect the other:

[8920d2aae123a058638216dffb4d2b8f | starter\data\raw\thinkpython2.pdf | page 118]
object.

**Các query đã tìm:**
[
  "two lists equal same elements not same object identity aliasing",
  "\"If another list has the same elements\" \"not the same object\""
]

## q14

**Câu hỏi:** dict.get(key, default) trả về gì khi key không tồn tại trong dictionary?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi `key` không tồn tại trong dictionary, `dict.get(key, default)` trả về giá trị `default` đã được truyền vào [d3f1db77682411be501d0bff70424c22]. Ví dụ, với `h = {'a': 1}`, `h.get('c', 0)` trả về `0` [220481f7608555ed38b64bd6c3a3859a].

**Đáp án tham chiếu:**
Trả về giá trị default đã truyền vào thay vì truy cập một key không tồn tại.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 127,
    "evidence": "Dictionaries have a method calledgetthat takes a key and a default value. If the key\nappears in the dictionary,getreturns the corresponding value; otherwise it returns the\ndefault value."
  }
]

**Citations theo thứ tự cần chấm:**
["d3f1db77682411be501d0bff70424c22", "220481f7608555ed38b64bd6c3a3859a"]

**Context cuối thực sự gửi cho model:**
[d3f1db77682411be501d0bff70424c22 | starter\data\raw\thinkpython2.pdf | page 127]
The histogram indicates that the letters'a'and'b'appear once;'o'appears twice, and
so on.
Dictionaries have a method calledgetthat takes a key and a default value. If the key
appears in the dictionary,getreturns the corresponding value; otherwise it returns the
default value. For example:
>>> h = histogram('a')
>>> h
{'a': 1}
>>> h.get('a', 0)

[220481f7608555ed38b64bd6c3a3859a | starter\data\raw\thinkpython2.pdf | page 128]
106 Chapter 11. Dictionaries
1
>>> h.get('c', 0)
0
As an exercise, usegetto writehistogrammore concisely. You should be able to eliminate
theifstatement.

[cbef56089c431525edf5f04216ef822e | starter\data\raw\thinkpython2.pdf | page 128]
11.3 Looping and dictionaries
If you use a dictionary in aforstatement, it traverses the keys of the dictionary. For exam-
ple,print_histprints each key and the corresponding value:
def print_hist(h):
for c in h:
print(c, h[c])
Here’s what the output looks like:
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1
Again, the keys are in no particular order. To traverse

[34d5e0903129b4520b794265a29e85fa | starter\data\raw\thinkpython2.pdf | page 129]
= d[key]

**Các query đã tìm:**
[
  "dict.get key default when key not in dictionary",
  "\"h.get('b', 0)\" get returns default value example"
]

## q15

**Câu hỏi:** Vì sao list không thể được dùng làm key của dictionary?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
List không thể làm key của dictionary vì list là kiểu **mutable** (có thể thay đổi), trong khi cơ chế bảng băm của dictionary đòi hỏi key phải **hashable** — thường là các kiểu bất biến như số nguyên, số thực và chuỗi [36fc7412ab05842da8dd048e69f348b5].

Cụ thể, dictionary dùng hàm băm để tính các số gọi là *hash value* nhằm lưu và tra cứu các cặp key–value. Hệ thống này hoạt động tốt nếu key bất biến. Nhưng nếu key có thể thay đổi, như list, thì sẽ xảy ra vấn đề: khi tạo cặp key–value, Python băm key và lưu nó vào vị trí tương ứng; nếu sau đó key bị sửa rồi băm lại, nó sẽ trỏ đến một vị trí khác. Khi đó có thể có hai mục cho cùng một key, và việc tra cứu sẽ không còn đáng tin cậy [412d0321c79b9750049765afeec019da].

**Đáp án tham chiếu:**
Dictionary key phải hashable, trong khi list là kiểu mutable và không hashable.

**Gold / lý do thiếu bằng chứng:**
[
  {
    "source_id": "thinkpython2-v2.4.1",
    "page": 130,
    "evidence": "That’s why keys have to be hashable, and why mutable types like lists aren’t."
  }
]

**Citations theo thứ tự cần chấm:**
["36fc7412ab05842da8dd048e69f348b5", "412d0321c79b9750049765afeec019da"]

**Context cuối thực sự gửi cho model:**
[36fc7412ab05842da8dd048e69f348b5 | starter\data\raw\thinkpython2.pdf | page 134]
more specific than our previous use of the word “value”.
implementation:A way of performing a computation.
hashtable:The algorithm used to implement Python dictionaries.
hash function:A function used by a hashtable to compute the location for a key.
hashable:A type that has a hash function. Immutable types like integers, floats and strings
are hashable; mutable types like lists and dictionaries are not.
lookup:A dictionary operation that takes a key and finds the corresponding value.

[412d0321c79b9750049765afeec019da | starter\data\raw\thinkpython2.pdf | page 130]
use these integers, called hash values, to store and look up key-value pairs.
This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,

[6e4155ce82c314965b3a58b5803b692d | starter\data\raw\thinkpython2.pdf | page 129]
>>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
A reverse lookup is much slower than a forward lookup; if you have to do it often, or if the
dictionary gets big, the performance of your program will suffer.

**Các query đã tìm:**
[
  "why lists cannot be dictionary keys mutable hashable",
  "hash function takes a value computes hash mutable list changes hash value dictionary lookup"
]

## dev_u01

**Câu hỏi:** Trong phiên Python hiện tại trên máy của tôi, gọi numbers.pop() sẽ trả về giá trị cụ thể nào? Tôi chưa cung cấp nội dung của list numbers. Cần xác định giá trị cụ thể, không chỉ mô tả quy tắc của pop().

**Có đáp án:** False
**Trạng thái:** abstain

**Câu trả lời:**
Không đủ bằng chứng trong tài liệu để trả lời.

**Đáp án tham chiếu:**
(Yêu cầu từ chối)

**Gold / lý do thiếu bằng chứng:**
"Corpus là tài liệu Think Python, không chứa trạng thái list numbers trong phiên chạy riêng của người hỏi. Quy tắc pop() không đủ để xác định giá trị cụ thể."

**Citations theo thứ tự cần chấm:**
[]

**Context cuối thực sự gửi cho model:**
[358ace752b82138a0af81e54d86037d6 | starter\data\raw\thinkpython2.pdf | page 116]
10.8 Deleting elements
There are several ways to delete elements from a list. If you know the index of the element
you want, you can usepop:
>>> t = ['a','b','c']
>>> x = t.pop(1)
>>> t
['a','c']
>>> x
'b'
popmodifies the list and returns the element that was removed. If you don’t provide an
index, it deletes and returns the last element.
If you don’t need the removed value, you can use thedeloperator:
>>> t =

[b1ab56c6426c8ed5ec9282c015f74d93 | starter\data\raw\thinkpython2.pdf | page 94]
you have to subtract 1 fromlength:
>>> last = fruit[length-1]
>>> last
'a'
Or you can use negative indices, which count backward from the end of the string. The
expressionfruit[-1]yields the last letter,fruit[-2]yields the second to last, and so on.

[d2c4495d5b525ff62fd45434ea57b80e | starter\data\raw\thinkpython2.pdf | page 143]
modify existing lists. But Python provides the built-in functionsorted, which takes any
sequence and returns a new list with the same elements in sorted order, andreversed,
which takes a sequence and returns an iterator that traverses the list in reverse order.

**Các query đã tìm:**
[
  "Python list pop() removes and returns last element"
]

## dev_u02

**Câu hỏi:** Trong phiên Python hiện tại trên máy của tôi, biểu thức profile['name'] sẽ trả về chuỗi cụ thể nào? Tôi chưa cung cấp nội dung dictionary profile. Cần xác định chuỗi cụ thể.

**Có đáp án:** False
**Trạng thái:** abstain

**Câu trả lời:**
Không đủ bằng chứng trong tài liệu để trả lời.

**Đáp án tham chiếu:**
(Yêu cầu từ chối)

**Gold / lý do thiếu bằng chứng:**
"Corpus không cung cấp trạng thái dictionary profile trong phiên chạy riêng của người hỏi. Ví dụ dictionary trong sách không phải dữ liệu của phiên chạy đó."

**Citations theo thứ tự cần chấm:**
[]

**Context cuối thực sự gửi cho model:**
[4431acda6ea35df3888154f5479cda2a | starter\data\raw\thinkpython2.pdf | page 98]
name ='bob'

[fa35d98aa1d902025cf6ff817ae8a7b0 | starter\data\raw\thinkpython2.pdf | page 134]
11.9 Glossary
mapping:A relationship in which each element of one set corresponds to an element of
another set.
dictionary:A mapping from keys to their corresponding values.
key-value pair:The representation of the mapping from a key to a value.
item:In a dictionary, another name for a key-value pair.
key:An object that appears in a dictionary as the first part of a key-value pair.
value:An object that appears in a dictionary as the second part of a key-value pair.

[72c247a5874a5b27c22fb8fc7b10e8b9 | starter\data\raw\thinkpython2.pdf | page 125]
can also say that each key “maps to” a value. As an example, we’ll build a dictionary that
maps from English to Spanish words, so the keys and the values are all strings.
The functiondictcreates a new dictionary with no items. Becausedictis the name of a
built-in function, you should avoid using it as a variable name.
>>> eng2sp = dict()
>>> eng2sp
{}
The squiggly-brackets,{}, represent an empty dictionary. To add items to the

**Các query đã tìm:**
[
  "profile['name'] dictionary value"
]
