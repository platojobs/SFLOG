# [Finding the Closest Parent View of Two UIViews](https://github.com/platojobs/SFLOG/issues/169)

//Finding the Closest Parent View of Two UIViews
```swift
func findClosestCommonParent(view1: UIView, view2: UIView) -> UIView? {
    var path1 = [UIView]()
    var path2 = [UIView]()

    // Trace path for view1
    var currentView: UIView? = view1
    while let view = currentView {
        path1.append(view)
        currentView = view.superview
    }

    // Trace path for view2
    currentView = view2
    while let view = currentView {
        path2.append(view)
        currentView = view.superview
    }

    // Convert path2 into a hash table
    let hashTable = Set(path2)

    // Find the closest common ancestor
    for ancestor in path1 {
        if hashTable.contains(ancestor) {
            return ancestor
        }
    }

    return nil // No common ancestor found
}


```