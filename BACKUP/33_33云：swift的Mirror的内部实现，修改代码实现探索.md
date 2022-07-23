# [33云：swift的Mirror的内部实现，修改代码实现探索](https://github.com/platojobs/SFLOG/issues/33)

```swift

struct HTSruct {
    var age = 18
    var name = "FGH"
    var subclassName = "二年级"
    
}

struct StructMetadata {
    var kind:        Int
    var description: UnsafeMutablePointer<StructMetadataDesc>
}

struct StructMetadataDesc {
    var flags:              UInt32
    var parent:             UInt32  // 展示用Uint32代替，实际是相同大小的结构体，
    var name:               RelativeDirectPointer<CChar>
    // . . .  (当前研究获取属性类型，后面的属性先不管)
    var accessFunctionPtr:       RelativeDirectPointer<UnsafeRawPointer>  // 不在乎具体类型，就先用UnsafeRawPointer
        var fields:                  RelativeDirectPointer<FieldDescription>  // 不在乎具体类型，就先用UnsafeRawPointer
        var numFields:               UInt32  // 属性个数
        var fieldOffsetVectorOffset: UInt32
}

struct RelativeDirectPointer<T>{
    var offset: Int32
    
    // 偏移offset位置，获取内容指针
    mutating func get() -> UnsafeMutablePointer<T> {
        let offset = self.offset
        // withUnsafePointer获取指针
        return withUnsafePointer(to: &self) { p in
            // UnsafeMutablePointer 返回T类型对象的指针
            // UnsafeRawPointer将p指针转换为未知类型
            // numericCast将offset转换为偏移单位数
            // advanced进行内存偏移
            // assumingMemoryBound绑定指针为T类型
            return UnsafeMutablePointer(mutating: UnsafeRawPointer(p).advanced(by: numericCast(offset)).assumingMemoryBound(to: T.self))
        }
        
    }
}


// 记录结构体内所有属性的结构
struct FieldDescription {
    var MangledTypeName:         RelativeDirectPointer<CChar>
    var Superclass:              RelativeDirectPointer<CChar>
    var Kind:                    UInt16
    var FieldRecordSize:         UInt16
    var NumFields:               UInt32
    var fgfields:                  FieldRecord // 连续存储空间 (有几个数据，就会在后面添加几个记录，通过内存平移读取)
}

// 每个属性的内容
struct FieldRecord {
    var flag:                    Int32
    var mangledTypeName:         RelativeDirectPointer<CChar>
    var fieldName:               RelativeDirectPointer<CChar>   // 属性名称
}


let pp = unsafeBitCast(HTSruct.self as Any.Type, to:  UnsafeMutablePointer<StructMetadata>.self)
let namePtr = pp.pointee.description.pointee.name.get()
print(String(cString:namePtr ))
//HTSruct
let count = pp.pointee.description.pointee.numFields
print("HTStruct属性个数：\(count)")


// 单独读取第一个属性名
var fields = pp.pointee.description.pointee.fields.get()
let fieldRecord1Name = fields.pointee.fgfields.fieldName.get()
print(String(cString: fieldRecord1Name))

// 读取所有记录
print("----读取所有属性名----")
(0..<count).forEach { index in
    let recordPtr = withUnsafePointer(to: &fields.pointee.fgfields) {
        return UnsafeMutablePointer(mutating: UnsafeRawPointer($0).assumingMemoryBound(to: FieldRecord.self).advanced(by: Int(index)))
    }
    print(String(cString: recordPtr.pointee.fieldName.get()))
}

print("----dump----")
dump(HTSruct()) // 相似的实现方式


```

打印结果：
```swift
HTSruct
HTStruct属性个数：3
age
----读取所有属性名----
age
name
subclassName
----dump----
▿ __lldb_expr_14.HTSruct
  - age: 18
  - name: "FGH"
  - subclassName: "二年级"


```