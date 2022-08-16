# [swift枚举关联值](https://github.com/platojobs/SFLOG/issues/91)

总有一天，你会对著过去的伤痛微笑。你会感谢离开你的那个人，他配不上你的爱、你的好、你的痴心。他终究不是命定的那个人。幸好他不是。

—— 张小娴 ​​​​

---

```swift

enum Shape{
    case circle(center:(Double,Double),radius:Double)
    case rect(center:(Double,Double),width: Double, height: Double)
    case triangle(point1:(Double,Double),point2:(Double,Double),point3:(Double,Double))
}

var circle = Shape.circle(center: (0,0), radius: 3)

var rect = Shape.rect(center: (0,0), width: 100, height: 50)
var triangle = Shape.triangle(point1: (0,0), point2: (1,1), point3: (3, 3))

print(triangle)


func shapeFunc(param:Shape){
    
    switch param{
        
    case let .circle(center: center, radius: radius):
        print("==1==\(center), radius= \(radius)")
    case let .rect(center, width, height):
        print("rect= \(center), width=\(width), height=\(height)")
    case let .triangle(point1, point2, point3):
        print("trangle \(point1),\(point2),\(point3)")
    }
}

shapeFunc(param: circle)


```