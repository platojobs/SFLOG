# [Flutter异步支持](https://github.com/platojobs/SFLOG/issues/172)

```dart

//2. Future.catchError
test_catchError(){
  
  //catchError
  Future.delayed(Duration(seconds: 2),(){
    //return"hello,finish,success"; //成功的返回
     throw AssertionError("Error"); // 抛出一个错误
  }).then((data){
   // 成功
    print("成功");
  }).catchError((error){
    // 错误
    print(error);
  });

 //onError
 //  Future.delayed(Duration(seconds: 2),(){
 //    //return"hello,finish,success"; //成功的返回
 //    throw AssertionError("Error"); // 抛出一个错误
 //  }).then((data){
 //    // 成功
 //    print("成功");
 //  },onError: (e){
 //    //可选参数的捕获
 //    print("=====$e");
 //  });


```