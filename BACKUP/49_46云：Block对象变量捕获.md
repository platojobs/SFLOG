# [46云：Block对象变量捕获](https://github.com/platojobs/SFLOG/issues/49)

```oc
 FangYanPing * person = [[FangYanPing alloc] init];
            person.age = 10;
            void (^block)(void) = ^{
                NSLog(@"年龄:%ld",person.age);
            };
            person.age = 20;
            block();
            
            NSLog(@"%@",[block class]);

//2021-09-17 18:31:26.103463+0800 xxxApp[3845:180755] 年龄:20
//2021-09-17 18:31:26.103618+0800 xxxApp[3845:180755] __NSMallocBlock__


```
1、对象的局部变量捕获和基本数据类型有点区别，对象的局部auto变量捕获是指针捕获不是值捕获，所以捕获的内容会受外部变量的影响
2、因为block捕获了auto变量所以`block`是`NSStackBlock`,在ARC下将block赋值给__strong指针时会自动将栈上的block复制到堆上，block由`NSStackBlock`变为`NSMallocBlock`
