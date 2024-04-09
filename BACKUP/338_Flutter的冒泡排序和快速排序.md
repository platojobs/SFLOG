# [Flutter的冒泡排序和快速排序](https://github.com/platojobs/SFLOG/issues/338)

```dart

// 冒泡排序 in Flutter
List<int> bubbleSort(List<int> arr) {
  int n = arr.length;
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

// 快速排序 in Flutter
List<int> quickSort(List<int> arr) {
  if (arr.length <= 1) return arr;
  int pivot = arr[arr.length ~/ 2];
  List<int> left = [];
  List<int> right = [];
  for (int i = 0; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.add(arr[i]);
    } else if (arr[i] > pivot) {
      right.add(arr[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}


```