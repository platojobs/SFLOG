# [Flutter 3.44 与 Google I/O 2026 同时发布](https://github.com/platojobs/SFLOG/issues/353)

Flutter 3.44 与 Google I/O 2026 同时发布。这一次，重点似乎更多地放在改变日常开发体验的更新上，而不是炫酷的新功能上。

需要特别注意的几点
首先，让我们挑出你绝对必须知道的关键点。

🤖 Agentic 热重载：AI 编码代理自动连接到您正在运行的 Flutter 应用，并为您处理热重载。
🎨 Material/Cupertino 正在远离主 SDK：迁移到独立软件包的趋势已经开始material_ui。cupertino_ui
📦 Swift Package Manager 成为 iOS/macOS 的默认包管理器：告别我们长期以来依赖的 CocoaPods 终于成为现实。
⚡混合组合++ (HCPP)：借助 Vulkan + SurfaceControl，Android 平台视图（WebView/Maps 等）的性能得到了极大提升。
🪟多窗口 API 已在桌面端实验性上线：维护负责人为 Canonical
人工智能/智能体开发支持
这是本次的亮点类别。它包含了所有专注于创建和运行带有 AI 代理的 Flutter 应用的最新资讯。

Agentic 热重装
🛠它的功能：只需告诉AI“更改此按钮的颜色”，智能体就会处理从代码修改→保存→热重载的所有操作。开发者只需查看屏幕并确认结果即可。
💡优势：摒弃了“让AI编写代码→手动重新加载→检查”的“打地鼠”式流程，将感知反馈周期从几分钟缩短到几秒钟。
[Dart/Flutter MCP 服务器](https://github.com/dart-lang/ai)
🛠您可以做什么：像 Claude Code 和 Cursor 这样的 AI 代理可以通过本地 Dart 分析器来操作代码和运行测试，同时了解项目的类型信息、组件树和依赖项。
💡优势：从“基于文本匹配重写代码”到“非破坏性重构和类型安全检查”。幻觉减少，提案的可信度增加。
[GenUI SDK](https://docs.flutter.dev/ai/genui/get-started)（[flutter/genui](https://github.com/flutter/genui)）
🛠你可以做什么：你可以将 AI 回复以真正的 Flutter UI 形式呈现，而不是“一大段文字” 。例如，“告诉我这个周末有什么活动”→ 你可以创建一个体验，在聊天窗口中显示活动卡片列表。
💡优势：基于聊天的用户界面从“只读”演变为“可在对话过程中进行交互的应用”。由于它使用嵌入在应用中的组件目录，因此安全性得到保证，因为它不会直接执行人工智能编写的代码。
[A2UI协议](https://a2ui.org/)
🛠功能介绍： GenUI 后台运行的通用 UI 格式(v0.9)，促进 AI 与应用程序之间的通信。使用相同的协议，可以针对不同的模型和实现创建相同的 UI。
💡优势：每次创建动态 UI 时，都会避免供应商锁定，防止每家公司开发自己独特的规范。
可解释字节码（临时用户界面交付） *截至 Dart 3.12 版本，目前仍处于研究阶段
🛠未来发展方向：其理念是能够为应用程序提供一次性用户界面，而无需经过 App Store 审核流程。
💡优势：A/B 测试 UI 和短期活动屏幕可以与发布周期分开部署。
[特工技能](https://docs.flutter.dev/ai/agent-skills)
🛠您可以做什么：您可以让代理执行Flutter 特有的任务，例如“添加集成测试”和“修复本地化”，并遵循该项目的最佳实践。
💡优势：不再是“基于通用 Flutter 知识编写代码”，而是根据特定的代码库编写更改。
框架（Material / Cupertino）
核心冻结是一个重要议题。各个组件的发展围绕三个方面展开：“菜单”、“可定制性”和“稳健性”。

Material/Cupertino 核心已冻结：从现在起，它将作为单独的软件包分发material_ui（cupertino_ui不再受 SDK 的 3 个月周期限制）。
库比蒂诺更新：更新使其更接近原生 iOS 的感觉CupertinoMenuAnchor，包括新增功能、CupertinoSheetRoute滚动和拖动支持CupertinoFocusHalo以及超级椭圆支持。
新增小部件/构造函数：已添加RoundedSuperellipseInputBorder，SizedBox.square()
增强自定义功能：为Carousel（无限滚动）、TabBar（可选ScrollController）、NavigationRail/ DropdownMenu/ Stepper​​/ Hero/ MenuAnchor/ AnimatedCrossFade/等添加了更精细的参数。ModalBottomSheet
增强功能和修复EditableText：修复了与 0x0 大小环境（及其他环境）中的崩溃预防、RangeSlider焦点行为、DateRangePicker主题应用、SegmentedButton宽度分布等相关的错误。
渲染（叶轮）
虽然没有花哨的新功能，但有几项改进。

Vulkan 内存管理：改进了缓存管理和 GPU/CPU 同步效率（从而在掉帧期间表现更稳定）。
Skia 后端弃用（Android 10+）：消除启动时着色器编译造成的垃圾。
圆的绘制方式进行了改进：改为基于有符号距离函数，以消除锯齿。
文本渲染：当缩放不均匀时，使用双线性滤波器TextFrame来减少共享数据。
iOS / macOS
这些变化主要集中在依赖管理和 Xcode 方面。

Swift Package Manager 是默认的包管理器：CLI 会自动迁移 Xcode 项目，CocoaPods 插件被视为备用方案，并会发出警告。
[现在推荐使用 SPM 将代码添加到 iOS 应用](https://docs.flutter.dev/add-to-app/ios/project-setup)：此方法涉及将生成的 Swift 包导入到现有的 iOS 应用中flutter build swift-package --platform ios。迁移之前需要移除现有的 CocoaPods/嵌入式框架集成（需要 Xcode 15.0 或更高版本）。
Xcode 26 兼容性：添加了对 arm64 排除设置的警告。
SwiftPM 改进了最小平台不匹配诊断：使依赖项解析失败消息更清晰。
针对 CocoaPods × SwiftPM 冲突的引导式错误处理：避免在迁移过程中项目陷入困境。
UIScene 生命周期警告：提前通知，以便为 Apple 的未来要求做好准备
内联文本预测输入：支持 iOS 上的内联自动完成功能。
移除了绕过 iOS 模拟器中虚假叶轮图像的变通方法。
安卓
平台视图已得到改进。

混合组合++ (HCPP) ：通过使用 Vulkan + SurfaceControl 将组合委托给操作系统来--enable-hcpp实现组合。
预测返回扩展：FlutterFragment现在FlutterFragmentActivity也支持预测返回
Android API 36 支持：CheckState支持新的 API 。
AGP 9 支持：由于 Kotlin 中集成了 AGP 9，插件应用程序需要进行审查。
修复了华为图像读取器的错误
改进内容尺寸
网站
主要侧重点在于一些细微的修正。

修复了 iframe 内滚动事件的传播问题。
修正因文本样式同步导致的输入法和选择行为异常。
在 iOS 的 iframe 中查看文本输入框。
修复了 iOS 26 上 Safari 浏览器中的自动填充错误。
桌面/嵌入式
组织架构调整和新API的迹象。

多窗口 API（实验性）：计划支持工具提示、弹出窗口、单​​独的对话框窗口等。
Canonical 接任桌面 Linux 的主要维护者：Linux/桌面生态系统的活动日益活跃。
丰田 RAV4 (2026)：车载信息娱乐系统基于 Flutter 运行。
LG webOS SDK：智能电视专用 SDK 即将推出
工具/开发者工具
直接影响日常开发体验的改进。

DevTools 迁移到 WASM 编译：改进了启动和操作响应。
使用 Dart 分析服务器，将小部件预览的内存占用降低高达 50%，从而提高效率。
默认情况下禁用硬件键盘规律性警告。
TestWidgetsApp新增功能：简化日常测试流程。
风格指南已更新：点简写，明确了扩展方法的推荐做法。
飞镖 3.12
Flutter 3.44 中包含了 Dart 的更新。

私有命名参数_field可以直接作为构造函数参数接受。
主构造函数（实验性）：一种语法，允许您在类声明的同时编写构造函数。
Genkit Dart：一个与模型无关的全栈 AI 框架现在支持 Dart。
破坏性变化
升级前您应该检查的变更。详情请参阅[官方重大变更指南。](https://docs.flutter.dev/release/breaking-changes)

ExtendSelectionByPageIntent删除：ExtendSelectionVerticallyToAdjacentPageIntent替换为。
TextDecorationGanifinal：继承和实现是不可能的。必须TextDecoration.combine通过结合使用或使用绘图层来处理。此外，处理方式在不同平台上也应maskValue保持一致。
更改了页面过渡生成器的导入路径：//CupertinoPageTransitionsBuilder引用已简化。建议对其进行标识。PageTransitionsBuilderpageTransitionsThemerg "CupertinoPageTransitionsBuilder|PageTransitionsBuilder|pageTransitionsTheme"
Android：嵌入式 Kotlin + AGP 9 支持：手动org.jetbrains.kotlin.android应用此功能可能会导致构建失败。需要遵循[Kotlin 迁移指南。](https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers)
iOS：[UIScene 生命周期](https://docs.flutter.dev/release/breaking-changes/uiscenedelegate)过渡通知UISceneDelegate：建议进行过渡以满足 Apple 的未来要求。
iOS/macOS：由于 SwiftPM 成为默认依赖项，依赖项解析方式有所变更：CocoaPods 依赖的插件现在会显示回退警告。与 SwiftPM 结合使用时可能会检测到冲突。CocoaPods注册表将于 2026 年 12 月 2 日变为只读，因此请尽早迁移，包括“添加到应用”类应用。
DropdownMenu对非空性的更改（部分已恢复）：如果您已为 3.43 版本重写，则可能需要重新调整。
概括
Agentic 热重载和 SwiftPM 的默认设置将影响未来的开发方式，因此值得在新项目中引入它们。Material
/Cupertino 包的分离需要持续关注。