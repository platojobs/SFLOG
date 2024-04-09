# [swift的enum的内存布局研究](https://github.com/platojobs/SFLOG/issues/184)

```swift
enum Password {
    case number(Int, Int,Int,Int)
    case other
}

var pwd = Password.number(9, 8, 6, 4)
pwd = .other
print(MemoryLayout.stride(ofValue: pwd)) // 40 系统分配的
print(MemoryLayout.size(ofValue: pwd)) // 33 实际用到的
print(MemoryLayout.alignment(ofValue: pwd)) // 8 对齐单位

enum TestRnum {
    case test1 , test2,test3
}

var tt = TestRnum.test1
print(MemoryLayout.stride(ofValue: tt))  // 1
print(MemoryLayout.size(ofValue: tt))  //1
print(MemoryLayout.alignment(ofValue: tt)) //1

enum TestRnum11{
    case test(Int)
}
var tt11 = TestRnum11.test(12)
print(MemoryLayout.stride(ofValue: tt11))  // 8
print(MemoryLayout.size(ofValue: tt11))  //8
print(MemoryLayout.alignment(ofValue: tt11)) //8


enum TestEnum22 {
    case test1(Int,Int,Int)
    case test2(Int,Int)
    case test3(Int)
    case test4(Bool)
}

var tt22 = TestEnum22.test1(1, 2, 3)
print(MemoryLayout.stride(ofValue: tt22))  // 32
print(MemoryLayout.size(ofValue: tt22))  // 25
print(MemoryLayout.alignment(ofValue: tt22)) // 8


enum TestEnum33 {
    case test0
    case test1
    case test2(Int , Int)
    case test3(Int,Int,Int)
    case test4(Int,Int,Int,Bool)
}

var test33 = TestEnum33.test0

print(MemoryLayout.stride(ofValue: test33))  // 32
print(MemoryLayout.size(ofValue: test33))  // 25
print(MemoryLayout.alignment(ofValue: test33)) // 8


enum TestEnum44 {
    case test0
    case test1
    case test2(Int , Int)
    case test3(Int,Int,Int)
    case test4(Int,Bool,Int,Int)
}

var test44 = TestEnum44.test0

print(MemoryLayout.stride(ofValue: test44))  // 40
print(MemoryLayout.size(ofValue: test44))  // 33
print(MemoryLayout.alignment(ofValue: test44)) // 8


enum TestEnum55 {
    case test0
    case test1
    case test2(Int ,Int)
    case test3(Int,Int,Int)
    case test4(Bool,Int,Int,Int)
}
var test55 = TestEnum55.test0
print(MemoryLayout.stride(ofValue: test55))  // 40
print(MemoryLayout.size(ofValue: test55))  // 33
print(MemoryLayout.alignment(ofValue: test55)) // 8


enum Test00{
     case enum1(t1:Int)
     case enum2(t1:Int8,t2:Int16,t3:Int)  // 1,2,8
     case enum3(t1:Int8,t2:Int,t3:Int16,t4:Int32)
     case enum4(t1:Int8,t2:Int,t3:Int16,t4:Int,t5:Int8,t6:String) //(1,8,2,8,1,16)
}


var testddd = Test00.enum1(t1: 1)

print(MemoryLayout.stride(ofValue: testddd))  // 56
print(MemoryLayout.size(ofValue: testddd))  // 56
print(MemoryLayout.alignment(ofValue: testddd)) // 8


```