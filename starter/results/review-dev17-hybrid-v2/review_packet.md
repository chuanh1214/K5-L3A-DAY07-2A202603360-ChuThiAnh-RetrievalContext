# Phiếu đối chiếu câu trả lời

Đọc context cuối, không chỉ kiểm tra ID citation.
Gold là nhãn tham chiếu, không thay thế việc đọc evidence.

## q01

**Câu hỏi:** Chỉ số âm trong chuỗi đếm từ phía nào?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Chỉ số âm trong chuỗi đếm ngược từ phía cuối chuỗi. Ví dụ, `fruit[-1]` cho ký tự cuối cùng, `fruit[-2]` cho ký tự kế cuối, v.v. [b1ab56c6426c8ed5ec9282c015f74d93]

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
[0c25940437e76f0de4d2d8bb622de1d0 | starter\data\raw\thinkpython2.pdf | page 112]
• Any integer expression can be used as an index.
• If you try to read or write an element that does not exist, you get anIndexError.
• If an index has a negative value, it counts backward from the end of the list.
Theinoperator also works on lists.
>>> cheeses = ['Cheddar','Edam','Gouda']
>>>'Edam'in cheeses
True
>>>'Brie'in cheeses
False

[b1ab56c6426c8ed5ec9282c015f74d93 | starter\data\raw\thinkpython2.pdf | page 94]
you have to subtract 1 fromlength:
>>> last = fruit[length-1]
>>> last
'a'
Or you can use negative indices, which count backward from the end of the string. The
expressionfruit[-1]yields the last letter,fruit[-2]yields the second to last, and so on.

[8ee3c32328f6b12af88d43507d83ef0b | starter\data\raw\thinkpython2.pdf | page 94]
72 Chapter 8. Strings
But the value of the index has to be an integer. Otherwise you get:
>>> letter = fruit[1.5]
TypeError: string indices must be integers

**Các query đã tìm:**
[
  "negative index string counts from which end"
]

## q02

**Câu hỏi:** Điều gì xảy ra khi dùng số thực làm chỉ số để truy cập một ký tự trong chuỗi?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi dùng số thực làm chỉ số để truy cập một ký tự trong chuỗi, chương trình sẽ gây ra lỗi `TypeError: string indices must be integers`, vì giá trị của chỉ số phải là số nguyên. Ví dụ: `letter = fruit[1.5]` sẽ báo `TypeError: string indices must be integers` [8ee3c32328f6b12af88d43507d83ef0b].

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

[0c25940437e76f0de4d2d8bb622de1d0 | starter\data\raw\thinkpython2.pdf | page 112]
• Any integer expression can be used as an index.
• If you try to read or write an element that does not exist, you get anIndexError.
• If an index has a negative value, it counts backward from the end of the list.
Theinoperator also works on lists.
>>> cheeses = ['Cheddar','Edam','Gouda']
>>>'Edam'in cheeses
True
>>>'Brie'in cheeses
False

[41ef7e0c492b713b3e2ccf0d7a7fddf7 | starter\data\raw\thinkpython2.pdf | page 101]
8.12 Glossary
object:Something a variable can refer to. For now, you can use “object” and “value”
interchangeably.
sequence:An ordered collection of values where each value is identified by an integer
index.
item:One of the values in a sequence.
index:An integer value used to select an item in a sequence, such as a character in a string.
In Python indices start from 0.
slice:A part of a string specified by a range of indices.

**Các query đã tìm:**
[
  "string index must be integer float index TypeError"
]

## q03

**Câu hỏi:** Vì sao không thể thay một ký tự của chuỗi bằng cách gán vào vị trí của ký tự đó?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không thể gán vào một vị trí (index) của chuỗi vì chuỗi (string) là **immutable** — bất biến, tức là không thể thay đổi nội dung của nó sau khi tạo. Trong tài liệu có ví dụ: nếu thử `greeting[0] = 'J'` thì Python báo lỗi `TypeError: 'str' object does not support item assignment`; ở đây "object" là chuỗi còn "item" là ký tự mà bạn muốn gán [2bae53eeca782ab89f45628641cf0045]. Nói cách khác, kiểu `str` không hỗ trợ phép gán theo phần tử (item assignment) [2bae53eeca782ab89f45628641cf0045].

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
["2bae53eeca782ab89f45628641cf0045"]

**Context cuối thực sự gửi cho model:**
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

[a84b36780062e0f3163376e9066f042b | starter\data\raw\thinkpython2.pdf | page 138]
But if you try to modify one of the elements of the tuple, you get an error:
>>> t[0] ='A'
TypeError: object doesn't support item assignment
Because tuples are immutable, you can’t modify the elements. But you can replace one
tuple with another:
>>> t = ('A',) + t[1:]
>>> t
('A','b','c','d','e')
This statement makes a new tuple and then makestrefer to it.
The relational operators

[8ee3c32328f6b12af88d43507d83ef0b | starter\data\raw\thinkpython2.pdf | page 94]
72 Chapter 8. Strings
But the value of the index has to be an integer. Otherwise you get:
>>> letter = fruit[1.5]
TypeError: string indices must be integers

**Các query đã tìm:**
[
  "strings are immutable cannot assign to index item assignment"
]

## q04

**Câu hỏi:** Trong chương 8, vị trí kết thúc truyền cho phương thức find có được tính vào phạm vi tìm kiếm không?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không. Vị trí kết thúc (tham số thứ ba) không được tính vào phạm vi tìm kiếm: tìm kiếm chỉ tính từ vị trí bắt đầu đến **trước** vị trí kết thúc. Chương 8 giải thích rằng điều này giúp `find` nhất quán với toán tử slice [8244e78c77b3fdf58c0397a2f7b4d1ba].

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
[8244e78c77b3fdf58c0397a2f7b4d1ba | starter\data\raw\thinkpython2.pdf | page 98]
>>> name.find('b', 1, 2)
-1
This search fails becausebdoes not appear in the index range from1to2, not including2.
Searching up to, but not including, the second index makesfindconsistent with the slice
operator.

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

[42d079cff7f533b32546fd69e9b3a496 | starter\data\raw\thinkpython2.pdf | page 107]
9.3 Search
All of the exercises in the previous section have something in common; they can be solved
with the search pattern we saw in Section 8.6. The simplest example is:
def has_no_e(word):
for letter in word:
if letter =='e':
return False
return True
Theforloop traverses the characters inword. If we find the letter “e”, we can immediately
returnFalse; otherwise we have to go to the next letter. If we exit the loop normally, that
means we didn’t find an “e”, so we

**Các query đã tìm:**
[
  "Chapter 8 find method end position included search range Python"
]

## q05

**Câu hỏi:** Sách đề xuất cách nào để giảm khác biệt hoa/thường trước khi so sánh các chuỗi?

**Có đáp án:** True
**Trạng thái:** error

**Câu trả lời:**
(Không có)

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
[]

**Context cuối thực sự gửi cho model:**
[18edaf2d96821ff802e014131e5eaed9 | starter\data\raw\thinkpython2.pdf | page 138]
work with tuples and other sequences; Python starts by comparing

[3f19c2f09956237905e374308e1f32ac | starter\data\raw\thinkpython2.pdf | page 105]
Chapter 9
Case study: word play
This chapter presents the second case study, which involves solving word puzzles by
searching for words that have certain properties. For example, we’ll find the longest palin-
dromes in English and search for words whose letters appear in alphabetical order. And
I will present another program development plan: reduction to a previously solved prob-
lem.

[b241c61a100b577476da1d47578e7cf5 | starter\data\raw\thinkpython2.pdf | page 109]
9.6 Glossary
file object:A value that represents an open file.
reduction to a previously solved problem:A way of solving a problem by expressing it
as an instance of a previously solved problem.
special case:A test case that is atypical or non-obvious (and less likely to be handled cor-
rectly).

[c56f05afcbde79afa359a8ffb08d5cca | starter\data\raw\thinkpython2.pdf | page 116]
94 Chapter 10. Lists
isupperis a string method that returnsTrueif the string contains only upper case letters.
An operation likeonly_upperis called afilterbecause it selects some of the elements and
filters out the others.
Most common list operations can be expressed as a combination of map, filter and reduce.

**Các query đã tìm:**
[
  "case insensitive comparison strings lower method",
  "convert strings to lower case before comparing case sensitive"
]

**Lỗi — báo riêng, không tạo nhãn chất lượng:**
{"type": "ValueError", "message": "Search query không hợp lệ."}

## q06

**Câu hỏi:** Phương thức nào của file object đọc các ký tự đến ký tự xuống dòng và trả về một chuỗi?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Đó là phương thức **`readline`**: nó đọc các ký tự từ file cho đến khi gặp ký tự xuống dòng và trả về kết quả dưới dạng một chuỗi [913eb0b827a2af56f2a765320ab9c2b7].

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
["913eb0b827a2af56f2a765320ab9c2b7"]

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

[81ccf3e8fe35b6643957666b728e4f5f | starter\data\raw\thinkpython2.pdf | page 102]
a string).

**Các query đã tìm:**
[
  "file object method reads characters until newline returns a string"
]

## q07

**Câu hỏi:** Trong ví dụ đọc danh sách từ, sách dùng phương thức nào để bỏ ký tự xuống dòng khỏi dòng vừa đọc?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Sách dùng phương thức chuỗi `strip` để bỏ ký tự xuống dòng khỏi dòng vừa đọc, ví dụ: `word = line.strip()` [0d2e210930428930c52375dd962f1186]. Trong chương trình đọc `words.txt` và in từng từ, sách cũng dùng `word = line.strip()` [0e0e5c6e2351d8abed9d5c8404dcba46].

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

[913eb0b827a2af56f2a765320ab9c2b7 | starter\data\raw\thinkpython2.pdf | page 105]
finis a common name for a file object used for input. The file object provides several
methods for reading, includingreadline, which reads characters from the file until it gets
to a newline and returns the result as a string:
>>> fin.readline()
'aa\n'
The first word in this particular list is “aa”, which is a kind of lava. The sequence\n
represents the newline character that separates this word from the next.

**Các query đã tìm:**
[
  "read words list strip newline method"
]

## q08

**Câu hỏi:** Hàm uses_all trả về True khi từ đầu vào đáp ứng điều kiện nào đối với các ký tự required?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Hàm `uses_all` nhận một từ (`word`) và một chuỗi các ký tự bắt buộc (`required`), và trả về `True` nếu từ đó **sử dụng tất cả các ký tự bắt buộc, mỗi ký tự ít nhất một lần** [0d52e4dc4e3409b706503f63aa699aea]. Cách cài đặt duyệt qua các ký tự trong `required`: nếu có ký tự bắt buộc nào không xuất hiện trong từ thì trả về `False`, ngược lại trả về `True` [d5286a35b8295c70831a21d22ef13cd6][50d3699021a4cdd41f6e335447b0f1b6].

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
["0d52e4dc4e3409b706503f63aa699aea", "d5286a35b8295c70831a21d22ef13cd6", "50d3699021a4cdd41f6e335447b0f1b6"]

**Context cuối thực sự gửi cho model:**
[0d52e4dc4e3409b706503f63aa699aea | starter\data\raw\thinkpython2.pdf | page 106]
that returnsTrueif the word contains only letters in the list. Can you make a sentence using only
the lettersacefhlo? Other than “Hoe alfalfa”?
Exercise 9.5.Write a function nameduses_allthat takes a word and a string of required letters,
and that returnsTrueif the word uses all the required letters at least once. How many words are
there that use all the vowelsaeiou? How aboutaeiouy?
Exercise 9.6.Write a function calledis_abecedarianthat

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

**Các query đã tìm:**
[
  "uses_all function required letters word"
]

## q09

**Câu hỏi:** List khác string như thế nào về khả năng thay đổi phần tử?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
String là **immutable** (không thể thay đổi): không thể gán lại một ký tự trong chuỗi bằng chỉ số. Ví dụ, `greeting[0] = 'J'` sẽ gây lỗi `TypeError: 'str' object does not support item assignment` [2bae53eeca782ab89f45628641cf0045]. Ngược lại, list là **mutable** (có thể thay đổi); nếu cần khả năng thay đổi các ký tự của một chuỗi, có thể dùng list các ký tự thay thế [bff571429fa1b7f66b52d2374846e72c].

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
["2bae53eeca782ab89f45628641cf0045", "bff571429fa1b7f66b52d2374846e72c"]

**Context cuối thực sự gửi cho model:**
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

[bff571429fa1b7f66b52d2374846e72c | starter\data\raw\thinkpython2.pdf | page 143]
To start with the obvious, strings are more limited than other sequences because the ele-
ments have to be characters. They are also immutable. If you need the ability to change the
characters in a string (as opposed to creating a new string), you might want to use a list of
characters instead.
Lists are more common than tuples, mostly because they are mutable. But there are a few
cases where you might prefer tuples:

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

**Các query đã tìm:**
[
  "list mutable strings immutable change element Think Python",
  "strings immutable item assignment TypeError 'str' object does not support item assignment",
  "lists are mutable modify element assignment unlike strings",
  "strings are immutable assignment character TypeError immutable sequence"
]

## q10

**Câu hỏi:** Trong chương 10, vì sao phép gán t = t.sort() gây kết quả không mong muốn?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Vì `sort()` là một **list method void**: nó sắp xếp danh sách tại chỗ và trả về `None`. Do đó, nếu viết `t = t.sort()`, giá trị trả về `None` sẽ được gán ngược lại cho `t`, làm mất tham chiếu đến danh sách vừa được sắp xếp — kết quả là `t` trở thành `None` thay vì danh sách đã sắp xếp [e837a534a33c9d9c42c4f293bf000344].

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

[f3fd4a9eb760149b9da8a139a34c4dae | starter\data\raw\thinkpython2.pdf | page 138]
116 Chapter 12. T uples
If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of
the sequence:
>>> t = tuple('lupins')
>>> t
('l','u','p','i','n','s')
Becausetupleis the name of a built-in function, you should avoid using it as a variable
name.
Most list operators also work on tuples. The bracket operator indexes an element:
>>> t =

**Các query đã tìm:**
[
  "Think Python Chapter 10 t = t.sort() unexpected result"
]

## q11

**Câu hỏi:** Phương thức pop() của list làm gì khi không truyền chỉ số?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi không truyền chỉ số, `pop()` sẽ xóa và trả về phần tử cuối cùng của list. Phương thức này vừa thay đổi list vừa trả về phần tử bị xóa [358ace752b82138a0af81e54d86037d6].

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

[9d84fa5418149d6955687fe552a97c59 | starter\data\raw\thinkpython2.pdf | page 113]
This loop traverses the list and updates each element.lenreturns the number of elements
in the list.rangereturns a list of indices from 0 ton−1, wherenis the length of the list.
Each time through the loopigets the index of the next element. The assignment statement
in the body usesito read the old value of the element and to assign the new value.
Aforloop over an empty list never runs the body:
for x in []:
print('This never happens.')

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
  "list pop method without index removes last element"
]

## q12

**Câu hỏi:** Muốn ghép một list các chuỗi thành một chuỗi bằng delimiter, dùng phương thức nào và gọi trên đối tượng nào?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Dùng phương thức `join`, và gọi nó **trên đối tượng là chuỗi delimiter**, truyền list các chuỗi vào làm tham số. Ví dụ: `delimiter = ' '` rồi `s = delimiter.join(t)`; nếu muốn nối không có khoảng trắng thì dùng chuỗi rỗng `''` làm delimiter [060dff8e3159ea9152799639bb68c2eb][e9cb1a022110108f4b7b88897c3a17ab].

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
[060dff8e3159ea9152799639bb68c2eb | starter\data\raw\thinkpython2.pdf | page 117]
on the delimiter and pass the list as a parameter:
>>> t = ['pining','for','the','fjords']
>>> delimiter =' '

[e9cb1a022110108f4b7b88897c3a17ab | starter\data\raw\thinkpython2.pdf | page 117]
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
In this case the delimiter is a space character, sojoinputs a space between words. To
concatenate strings without spaces, you can use the empty string,'', as a delimiter.

[d3bd94aecbfb7aa87885ec4b343c17a6 | starter\data\raw\thinkpython2.pdf | page 116]
10.9 Lists and strings
A string is a sequence of characters and a list is a sequence of values, but a list of characters
is not the same as a string. To convert from a string to a list of characters, you can uselist:
>>> s ='spam'
>>> t = list(s)
>>> t
['s','p','a','m']

**Các query đã tìm:**
[
  "join list of strings delimiter method string join"
]

## q13

**Câu hỏi:** Hai list chứa cùng các phần tử có nhất thiết phải là cùng một object không?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Không. Hai list có cùng các phần tử thì được coi là **tương đương** (equivalent), nhưng không nhất thiết **giống hệt/đồng nhất** (identical), tức không nhất thiết là cùng một object. Tài liệu nêu rõ: nếu hai object là identical thì chúng cũng equivalent, nhưng nếu chúng equivalent thì chưa chắc identical [d47d0792b790af695fbd82c66b898760]. Chỉ khi hai biến cùng tham chiếu đến một object, ví dụ `b = a`, thì chúng mới thực sự là cùng một object (aliasing) [f7948d3f5018303dcd6369324d75fba1].

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

[19bd875bac7798ab2d340ed06f3ce811 | starter\data\raw\thinkpython2.pdf | page 113]
10.5 List slices
The slice operator also works on lists:

[a9ae5daf9a019f451dbe33f5376a1e23 | starter\data\raw\thinkpython2.pdf | page 122]
aliasing:A circumstance where two or more variables refer to the same object.
delimiter:A character or string used to indicate where a string should be split.

**Các query đã tìm:**
[
  "two lists same elements same object identity aliasing equivalent",
  "\"equivalent\" \"identical\" lists same elements is operator object chapter 10"
]

## q14

**Câu hỏi:** dict.get(key, default) trả về gì khi key không tồn tại trong dictionary?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Khi `key` không tồn tại trong dictionary, `dict.get(key, default)` trả về **giá trị mặc định `default`** mà bạn đã truyền vào. Cụ thể, tài liệu mô tả: dictionary có phương thức `get` nhận một key và một giá trị mặc định; nếu key có trong dictionary thì `get` trả về giá trị tương ứng, ngược lại nó trả về giá trị mặc định [d3f1db77682411be501d0bff70424c22].

Điều này khác với cách truy cập bằng dấu ngoặc vuông: nếu key không có trong dictionary, `eng2sp['four']` sẽ gây ra ngoại lệ `KeyError: 'four'` [2ca87670aa0a333e820e4c5c43c35d32].

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
["d3f1db77682411be501d0bff70424c22", "2ca87670aa0a333e820e4c5c43c35d32"]

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

[9613d27c69c32a932fa379a17eec0f75 | starter\data\raw\thinkpython2.pdf | page 127]
The first line of the function creates an empty dictionary. Theforloop traverses the string.
Each time through the loop, if the charactercis not in the dictionary, we create a new item
with keycand the initial value 1 (since we have seen this letter once). Ifcis already in the
dictionary we incrementd[c].
Here’s how it works:
>>> h = histogram('brontosaurus')
>>> h
{'a': 1,'b': 1,'o': 2,'n':

[d3877b4c3448331718c35be0377df10d | starter\data\raw\thinkpython2.pdf | page 142]
use it in aforloop like this:
>>> for key, value in d.items():
... print(key, value)
...
c 2
a 0
b 1

[2ca87670aa0a333e820e4c5c43c35d32 | starter\data\raw\thinkpython2.pdf | page 126]
ger indices. Instead, you use the keys to look up the corresponding values:
>>> eng2sp['two']
'dos'
The key'two'always maps to the value'dos'so the order of the items doesn’t matter.
If the key isn’t in the dictionary, you get an exception:
>>> eng2sp['four']
KeyError:'four'
Thelenfunction works on dictionaries; it returns the number of key-value pairs:
>>> len(eng2sp)
3
Theinoperator works on

**Các query đã tìm:**
[
  "dict.get(key, default) returns default if key not in dictionary",
  "h.get('a', 0) h.get('b', 0) example get default value"
]

## q15

**Câu hỏi:** Vì sao list không thể được dùng làm key của dictionary?

**Có đáp án:** True
**Trạng thái:** answered

**Câu trả lời:**
Vì dictionary dùng **hash value** của key để lưu và tra cứu các cặp key–value, hệ thống này chỉ hoạt động đúng nếu key là **immutable** [412d0321c79b9750049765afeec019da]. Nếu key có thể thay đổi (mutable) như list, khi bạn sửa key rồi hash lại, nó sẽ trỏ đến một vị trí khác; hậu quả là có thể có hai mục cho cùng một key hoặc không tìm thấy key đó, khiến dictionary hoạt động sai [412d0321c79b9750049765afeec019da][30ec1f1e388ae9933a71e1e9deb745ba]. Do đó key phải **hashable**, và các kiểu mutable như list (hay dictionary) không hashable [30ec1f1e388ae9933a71e1e9deb745ba][36fc7412ab05842da8dd048e69f348b5]. Cách đơn giản để vượt qua hạn chế này là dùng **tuple** [30ec1f1e388ae9933a71e1e9deb745ba].

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
["412d0321c79b9750049765afeec019da", "30ec1f1e388ae9933a71e1e9deb745ba", "36fc7412ab05842da8dd048e69f348b5"]

**Context cuối thực sự gửi cho model:**
[412d0321c79b9750049765afeec019da | starter\data\raw\thinkpython2.pdf | page 130]
use these integers, called hash values, to store and look up key-value pairs.
This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,

[30ec1f1e388ae9933a71e1e9deb745ba | starter\data\raw\thinkpython2.pdf | page 130]
or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.
That’s why keys have to be hashable, and why mutable types like lists aren’t. The simplest
way to get around this limitation is to use tuples, which we will see in the next chapter.

[36fc7412ab05842da8dd048e69f348b5 | starter\data\raw\thinkpython2.pdf | page 134]
more specific than our previous use of the word “value”.
implementation:A way of performing a computation.
hashtable:The algorithm used to implement Python dictionaries.
hash function:A function used by a hashtable to compute the location for a key.
hashable:A type that has a hash function. Immutable types like integers, floats and strings
are hashable; mutable types like lists and dictionaries are not.
lookup:A dictionary operation that takes a key and finds the corresponding value.

**Các query đã tìm:**
[
  "why lists cannot be dictionary keys hashable mutable",
  "hash function values change mutable key dictionary wouldn't work correctly"
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

[fb7afbacf71ebf99fcb29849cc2c3dde | starter\data\raw\thinkpython2.pdf | page 116]
If you know the element you want to remove (but not the index), you can useremove:
>>> t = ['a','b','c']
>>> t.remove('b')
>>> t
['a','c']
The return value fromremoveisNone.
To remove more than one element, you can usedelwith a slice index:
>>> t = ['a','b','c','d','e','f']
>>> del t[1:5]
>>>

**Các query đã tìm:**
[
  "list pop() removes and returns last item"
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

[081a223f5d77fb5bb15ea38a7845b7a6 | starter\data\raw\thinkpython2.pdf | page 125]
11.1 A dictionary is a mapping
Adictionaryis like a list, but more general. In a list, the indices have to be integers; in a
dictionary they can be (almost) any type.
A dictionary contains a collection of indices, which are calledkeys, and a collection of
values. Each key is associated with a single value. The association of a key and a value is
called akey-value pairor sometimes anitem.
In mathematical language, a dictionary represents amappingfrom keys to values, so

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
