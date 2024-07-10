# [swift文件相关的操作](https://github.com/platojobs/SFLOG/issues/168)

### 路径
```swift
let path1 = "/Users/pj/Downloads/1.html"
let path2 = "/Users/pj/Documents/GitHub/"

let u1 = URL(string: path1)
do {
    // 写入
    let url1 = try FileManager.default.url(for: .itemReplacementDirectory, in: .userDomainMask, appropriateFor: u1, create: true) // 保证原子性安全保存
    print(url1)

    // 读取
    let s1 = try String(contentsOfFile: path1, encoding: .utf8)
    print(s1)

} catch {}

// 检查路径是否可用
let u2 = URL(fileURLWithPath:path2)
do {
    let values = try u2.resourceValues(forKeys: [.volumeAvailableCapacityForImportantUsageKey])
    if let capacity = values.volumeAvailableCapacityForImportantUsage {
        print("可用: \(capacity)")
    } else {
        print("不可用")
    }
} catch {
    print("错误: \(error.localizedDescription)")
}
```