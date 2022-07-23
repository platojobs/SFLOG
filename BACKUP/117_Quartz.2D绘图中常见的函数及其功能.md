# [Quartz 2D绘图中常见的函数及其功能](https://github.com/platojobs/SFLOG/issues/117)

在`Quartz 2D`的绘图中常见的函数及其功能如下：
（1）`draw（_rect：CGRect）`函数：这个是UIView内部自动调用，用于重画整个UIView中的图形内容，一般需要重载，实现自定义绘图。
（2）`UIGraphicsGetCurrentContext（）`函数：用于获得当前的图形上下文。
（3）`UIGraphicsEndImageContext（）`函数：关闭图形上下文。
（4）`CGPoint（x：，y：）`函数：建立一个点，其坐标为（x，y）。
（5）`CGRect（x：，y：，width：，height：）`函数：建立一个矩形，其左上角坐标为（x，y），其宽为width，其高为height。
（6）`move（to：CGPoint）`函数：将画图的落笔移动到CGPoint这一点所在的位置，开始画。
（7）`addLine（to：CGPoint）`函数：从当前点开始，画一条线段，其终点为CGPoint所在位置。
（8）`setStrokeColor（CGColor）`函数：设置笔画线段的颜色。
（9）`setFillColor（CGColor）`函数：设置填充的颜色。
（10）`setLineWidth（CGFloa）`函数：设置笔画线段的粗细。
（11）`addRect（CGRect）`函数：根据CGRect的矩形位置和大小，画出一个矩形。
（12）`strokeEllipse（in：CGRect）`函数：根据CGRect矩形的大小，画出了椭圆形。
（13）`addArc（center：，radius：，startAngle：，endAngle：，clockwise：）`函数：以`center`为中心，半径为radius，开始位置为startAngle，圆弧结束位置为endAngle（以弧度表示，CGFloat.pi*2代表整个圆），`clockwise`为true代表为顺时针方向。
（14）`strokePath（）`函数：立即根据前面设置的路径画线。
（15）`fillPath（）`函数：立即根据前面设置的路径填充颜色。
（16）`closePath（）`函数：从当前的位置，连接到起始点所在的位置。
（17）`context.setLineDash（phase：0，lengths：[6，1]）`函数：设置为虚线，其中phase为0代表从头开始，lengths为[6，1]代表实线和虚线的比例为6：1。
18）`drawPath（using：CGPathDrawingMode.fillStroke）`函数：可以实现笔画线段和内部填充同时进行，相当于`strokePath（）`和`fillPath（）`的功能。
（19）`CoreGraphUIView（）`：从UIView继承而来的一个自定义的类，在这个新类中，重载了`draw（_rect：CGRect）`函数，从而实现绘图功能。