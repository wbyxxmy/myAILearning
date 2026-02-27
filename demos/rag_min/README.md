# rag_min（离线 RAG 最小 Demo）

目标：用本地 Markdown 文档构建“可检索知识库”，查询时返回 TopK 相关片段，并输出带引用的模板式回答（不调用大模型）。

## 目录结构
- `data/docs/`：知识库 Markdown 文档
- `src/`：
  - `ingest.py`：切块 + embedding + 建索引
  - `query.py`：查询 + 检索 + 引用输出 + 模板回答
- `.rag_index/`：生成的索引目录（运行 ingest 后出现）

## 环境安装（两套方案）

### 方案 A（推荐，使用 FAISS：速度快）
> Windows 上建议用 conda 安装 faiss-cpu 更稳。

```bash
conda create -n ragmin python=3.10
conda activate ragmin
conda install -c conda-forge faiss-cpu
pip install -r requirements.txt
```

### 方案 B（兜底，不使用 FAISS：100% 可跑）
```bash
pip install -r requirements-win-no-faiss.txt
```

## 1. 准备知识库文档
把 Markdown 放到 `data/docs/` 下（可参考本 repo 的示例文档）。

## 2. 构建索引
```bash
python -m src.ingest --docs_dir data/docs --out_dir .rag_index
```

## 3. 查询
```bash
python -m src.query --index_dir .rag_index --top_k 5 "什么是RAG？它的基本流程是什么？"
```

输出包含：
- TopK 命中（相似度 + 引用 + 标题路径）
- 模板式回答（每条要点都附引用）

## 常见问题
- Q: Windows 装 faiss-cpu 失败？
  - 用“方案 B（兜底）”先跑通；或切换到 conda 安装。