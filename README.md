# 文本断行：贪心、两端对齐与断字

排版后行宽忽长忽短、标点跑到行首：宽度测量按字符数而不是字宽，贪心断行没算空格，两端对齐空格分配不均，断字没有按上限，寡妇/孤行没有处理，空行计数错，批量段落只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
text/__init__.py
text/linebreak.py
tests/test_linebreak.py
```

## 当前状态

`text/linebreak.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_linebreak.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 按字宽测量
2. 贪心断行含空格
3. 两端对齐分配空格
4. 断字按上限
5. 行数统计
6. 批量段落统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `text/linebreak.py`
后 15 条用例应全部通过。
