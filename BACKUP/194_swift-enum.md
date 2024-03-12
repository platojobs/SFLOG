# [swift-enum](https://github.com/platojobs/SFLOG/issues/194)

```swift

enum UGCContent {
    
    case west
    case east
    
    func desp() {
        print("hello")
    }
    
    static func ugcFun(){
        print("static")
    }
}

var rt = UGCContent.east
rt.desp()
UGCContent.ugcFun()

enum Weekday: String, CaseIterable {
  case sunday, monday, tuesday, wednesday, thursday, friday, saturday

  /* 自动合成的实现
  static var allCases: Self.AllCases { [sunday, monday, tuesday, wednesday, thursday, friday, saturday] }
  */
}

let weekday = Weekday.allCases.map{ $0.rawValue}.joined(separator: ",")
print(weekday)

//对于有关联值的枚举，不会自动合成 allCases，因为关联值没法确定


```