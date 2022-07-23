# [57:swiftc常用命令](https://github.com/platojobs/SFLOG/issues/61)

swiftc常用命令

---

```
-dump-ast              解析和类型检查源文件 & 转换成 AST
-dump-parse            解析源文件 & 转换成 AST
-emit-assembly         生成汇编文件
-emit-bc               生成 LLVMBitcode 文件
-emit-executable       生成已链接的可执行文件
-emit-imported-modules 生成已导入的库
-emit-ir               生成 LLVMIR 文件
-emit-library          生成已连接的库
-emit-object           生成目标文件
-emit-silgen           生成 raw SIL 文件（第一个阶段）
-emit-sil              生成 canonical SIL 文件（第2个阶段）
-index-file            为源文件生成索引数据
-print-ast             解析和类型检查源文件 & 转换成更简约的格式更好的 AST
-typecheck             解析和类型检查源文件


```