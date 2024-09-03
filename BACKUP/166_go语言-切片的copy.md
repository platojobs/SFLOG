# [go语言-切片的copy](https://github.com/platojobs/SFLOG/issues/166)

```go
slice_1 := []int{1, 2, 3, 4, 5}  // 目标切片
	slice_2 := []int{5, 4, 3} //源切片
	copy(slice_1, slice_2) //把2逐个塞到1中去
	fmt.Println(slice_1) //[5 4 3 4 5]
	slice_3 := []int{}
	copy(slice_3,slice_2) //把2塞到3中，因为3此时是空切片，所以塞不进去
	fmt.Println(slice_3)//[]
	copy(slice_2,slice_3) //把空切片塞到2中去，目标切片不会变化
	fmt.Println(slice_2) //[5 4 3]
```