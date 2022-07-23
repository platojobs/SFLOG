# [55:BlockOperation](https://github.com/platojobs/SFLOG/issues/59)

```swift
class ObjectBlockOperation{
    func threadOperation(){
        let operation = BlockOperation(block: {
            [weak self] in self?.worker()
            return
        })
        let queue = OperationQueue()
        queue.addOperation(operation)
        print("threadBlockOperation\(Thread.current)")
    }
    @objc func worker(){
        print("blockoperation")
    }
}

let blockObject = ObjectBlockOperation()
blockObject .threadOperation()

```