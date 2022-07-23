# [45云：_modify和yield](https://github.com/platojobs/SFLOG/issues/48)

```swift
@inlinable
  public subscript(index: Int) -> Element {
    get {
      // This call may be hoisted or eliminated by the optimizer.  If
      // there is an inout violation, this value may be stale so needs to be
      // checked again below.
      let wasNativeTypeChecked = _hoistableIsNativeTypeChecked()

      // Make sure the index is in range and wasNativeTypeChecked is
      // still valid.
      let token = _checkSubscript(
        index, wasNativeTypeChecked: wasNativeTypeChecked)

      return _getElement(
        index, wasNativeTypeChecked: wasNativeTypeChecked,
        matchingSubscriptCheck: token)
    }
    _modify {
      _makeMutableAndUnique() // makes the array native, too
      _checkSubscript_native(index)
      let address = _buffer.subscriptBaseAddress + index
      yield &address.pointee
    }
  }
```