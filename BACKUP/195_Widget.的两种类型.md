# [Widget 的两种类型](https://github.com/platojobs/SFLOG/issues/195)

出了 Widget 的两种类型，即：StatelessWidget 不带绑定状态，而 StatefulWidget 带绑定状态。当你所要构建的用户界面不随任何状态信息的变化而变化时，需要选择使用 StatelessWidget，反之则选用 StatefulWidget。前者一般用于静态内容的展示，而后者则用于存在交互反馈的内容呈现中。