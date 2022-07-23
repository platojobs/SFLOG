# [11云：swift类和结构体内存分配探索](https://github.com/platojobs/SFLOG/issues/11)

#### 1. 类和 结构体 内存分配探索

```swift
func stuctandClassTest() ->(){
    
    class Size {
        var width = 1
        var heght = 2
    }
    struct Point{
        var x = 3
        var y = 4
    }
    var size = Size()
    var point = Point()
    
    
    print("===+  %d",MemoryLayout<Size>.stride);
    print("===+  %d",MemoryLayout<Point>.stride);
    
    print(class_getInstanceSize(type(of: size))) //获取真正的内存大小
    
    print(Mems.ptr(ofRef: size))
    print(Mems.memStr(ofRef: size))
    
    print("1----------------")
    
    
    print(Mems.ptr(ofVal: &size))
    print(Mems.memStr(ofVal: &size))
       
    print("2----------------")
    
    print(Mems.ptr(ofVal: &point))
    print(Mems.memStr(ofVal: &point))
    
    
}

stuctandClassTest()



```

##### 1.1打印结果

```
===+  %d 8
===+  %d 16
32
0x000000010053cfc0
0x00000001000082a8 0x0000000200000002 0x0000000000000001 0x0000000000000002
1----------------
0x00007ffeefbff510
0x000000010053cfc0
2----------------
0x00007ffeefbff500
0x0000000000000003 0x0000000000000004

```

####  2. 分析结果

+ `0x00007ffeefbff510`（`size`）和`0x00007ffeefbff500`（`point`）的内存地址是挨着的，
+  `size` 需要申请堆空间内存,堆空间的内存大小也就是`32字节`，大致流程如下：
    1.`_allocating_init()`
    2.`_swift_allocObject`
    3.`swift_slowAlloc`
    4.`maloc`

+ `point `只是在栈空间，16个字节

+ ` size`堆空间的情况：
    `0x00000001000082a8`  ----`Size`类的信息

    `0x0000000200000002` ---- 引用计数
    
    `0x0000000000000001` ----- 1
    
    `0x0000000000000002`------- 2
    


