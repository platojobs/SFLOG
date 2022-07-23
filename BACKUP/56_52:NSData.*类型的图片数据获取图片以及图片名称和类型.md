# [52:NSData *类型的图片数据获取图片以及图片名称和类型](https://github.com/platojobs/SFLOG/issues/56)

需求：给定一个NSData *类型的图片数据，从中解析出图片和图片名称。其中图片数据NSData *的结构如下：
```
4个字节的图片名称长度+图片名称+4个字节的图片长度+图片数据
```

具体实现

> 假定NSData *imageData已经从网络中获取到了

1. 存储图片名称的字节数
```oc
 Byte imageNameLengthBytes[4];
 [imageData getBytes:imageNameLengthBytes length:4];//获取存储图片名称长度的字节

 int imageNameLenth = (int)  ((imageNameLengthBytes[0]&0xff) | ((imageNameLengthBytes[1] << 8)&0xff00) | ((imageNameLengthBytes[2]<<16)&0xff0000) | ((imageNameLengthBytes[3]<<24)&0xff000000));//解析出存储图片名称的字节数
```
2. 图片名称
 ```oc
 Byte newByte[imageNameLenth];
[imageData getBytes:newByte range:NSMakeRange(4, imageNameLenth)];//获取存储图片名称的字节
NSString *imageName = [[NSString alloc] initWithBytes:newByte length:imageNameLenth encoding:NSUTF8StringEncoding];//解析出图片名称
```
3.存储图片数据的字节数
```oc
 Byte imageLengthBytes[4];
[imageData getBytes:imageLengthBytes range:NSMakeRange((4 + imageNameLenth), 4)];//获取存储图片长度的字节
int imageLength = ((imageLengthBytes[0]&0xff) | ((imageLengthBytes[1] << 8)&0xff00) | ((imageLengthBytes[2] << 16)&0xff0000) | ((imageLengthBytes[3] << 24)&0xff000000));//解析出存储图片长度的字节数
```
3. 图片数据
```oc
NSData *data = [imageData subdataWithRange:NSMakeRange((8 + imageNameLenth), imageLength)];//获取图片数据
```
> 总结 1. `getBytes: length`获取从开始位置到指定长度的`byte`
2. `getBytes: range:`获取指定范围的`byte`
3. 将`byte`转换为`int`型，使用的是先“移位”然后“与”的方法，可以得到对应的值。




