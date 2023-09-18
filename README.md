## Đề bài:
Hóa đơn hơn 100 thì tích được 1 điểm. Đủ 5 điểm thì lần mua đồ sau được giảm 10% bill với bill <= 1000

## Cách sinh test:
    - Lập bảng quyết định chuyển hóa thành test cases
    - Chia ra các phần tương đương của biến để tạo ra test cases

## Note:
Mặc dù test pass hết nhưng bộ test không bắt được trường hợp

```python
	accumulated_points = 4
    bill = 150
    self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')
```

Trong trường hợp này, code sẽ check bill > 100, nên accumulated_points + 1 = 5
từ đó mà đủ điều kiện để nhận discount, nhưng theo đề bài, discount này đáng ra
phải được dùng cho lần sau nên kết quả phải là:  '+1 accumulated point'
chứ không phải 'You got a 10% bill discount' như hiện tại

# run tests
python -m unittest test.py