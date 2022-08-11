# [swift跳出语句](https://github.com/platojobs/SFLOG/issues/89)

总有一天，你会对著过去的伤痛微笑。你会感谢离开你的那个人，他配不上你的爱、你的好、你的痴心。他终究不是命定的那个人。幸好他不是。

—— 张小娴 ​​​​

---

```swift
enum MyError: Error {
    case errorOne
    case errorTwo
}

func newFunc() throws{
    
    throw MyError.errorOne
}

//newFunc()

func myFuncTwo(param:Int){
    if param <= 0 {
        return
    }
    print("其他操作")
}

func myFuncTwo2(param: Int){
    guard param>0 else {
        return
    }
    print("其他操作\(param)")
}

myFuncTwo2(param: 230)

var year = 2016

if year%400==0 || ((year%4==0) && (year%100 != 0)){
    print("闰年")
}


```