# [RXSwift的merge](https://github.com/platojobs/SFLOG/issues/185)

```swift
let disposeBag = DisposeBag()
         
let subject1 = PublishSubject<Int>()
let subject2 = PublishSubject<Int>()
 
Observable.of(subject1, subject2)
    .merge()
    .subscribe(onNext: { print($0) })
    .disposed(by: disposeBag)
 
subject1.onNext(20)
subject1.onNext(40)
subject1.onNext(60)
subject2.onNext(1)
subject1.onNext(80)
subject1.onNext(100)
subject2.onNext(1)
```