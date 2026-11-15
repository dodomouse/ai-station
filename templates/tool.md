# 双语词条模板

每个工具采用一个目录，共享元数据，并分别维护中文和英文正文。

- [共享元数据](tool/tool.json)
- [中文正文](tool/README.zh-CN.md)
- [English description](tool/README.en.md)
- [GitHub 快照](github-snapshot.json)

使用以下命令创建草稿，替换示例参数：

```bash
python3 scripts/catalog.py new example-tool --repository owner/repository
```

录入步骤见[中文贡献指南](../CONTRIBUTING.md)和[English contribution guide](../CONTRIBUTING.en.md)。字段约定见[数据格式](../docs/data-format.md)。
