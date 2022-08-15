# [swift冒泡排序测试](https://github.com/platojobs/SFLOG/issues/90)

总有一天，你会对著过去的伤痛微笑。你会感谢离开你的那个人，他配不上你的爱、你的好、你的痴心。他终究不是命定的那个人。幸好他不是。

—— 张小娴 ​​​​

---

```swift
func mySort(array: inout Array<Any> , sortClosure:(Any, Any)-> Bool) -> Array<Any>{
    
    for indexI in array.indices {
        if indexI == array.count - 1{
            break
        }
    
    for indexJ in 0...((array.count-1) - indexI-1){
        
        if sortClosure(array[indexJ],array[indexJ+1]){
            
        }else{
            array.swapAt(indexJ, indexJ+1)
        }
    }
    }
    return array
}

var arrar: Array<Any> = [ 1,2,4,5,6,2,3,4,1,4,8]

mySort(array: &arrar) { i, next in
    
    (i as! Int) < (next as! Int)
    
}

print(arrar)

```