# [Flutter函数](https://github.com/platojobs/SFLOG/issues/183)

```dart

// 函数定义
void showDesc(var name, Function log) {
  log(name);
}

// 函数调用，匿名函数作为参数
showDesc("Bruce", (name) {
    print("name = $name");
  });

// 输出结果
name = Bruce


```