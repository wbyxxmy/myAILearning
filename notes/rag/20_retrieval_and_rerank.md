# RAG 教程 20：检索（Retrieval）怎么做？向量相似度怎么理解？

这篇教程聚焦“检索阶段”。在 RAG 中，检索质量往往决定最终体验。

## 1. 向量检索在做什么
- 把每个 chunk 的文本转换成向量（embedding）
- 把用户问题也转换成向量
- 计算相似度，取 TopK chunk 作为“证据上下文”

## 2. cosine / dot product 与 normalize
常见做法：
- 用 cosine 相似度衡量“语义接近程度”
- 实现上往往把向量做 L2 normalize 后，用点积（dot product / inner product）代替 cosine

在 `demos/rag_min/src/vector_store.py` 里做了两件事：
- embedding 后做 L2 normalize
- FAISS 用 `IndexFlatIP`（内积）做 TopK

这样内积值越大，语义越相近。

## 3. TopK 取多少合适
经验：
- K 太小：容易漏证据
- K 太大：噪声多、上下文膨胀（如果接大模型会更明显）

MVP 建议 K=3~8 之间，先用评测集找一个“稳定点”。

## 4. 为什么需要 rerank（本 demo 不实现，但要知道）
向量检索是“粗排”，很快但可能把一些“看起来像”的片段排在前面。
Rerank（重排）用更强的模型对 TopN 进行二次排序，通常能显著提升命中质量。

扩展路线（后续可做）：
- 先向量检索 top 50
- 再用 reranker 排 top 5

## 5. 混合检索（也属于后续扩展）
实际工程常用：向量检索 + 关键词检索（BM25）。
原因：一些专有名词、版本号、错误码，用关键词更稳。

---

## 📌 导航
- 上一章：[RAG 教程 10：切块（Chunking）](./10_chunking.md)
- 下一章：[RAG 教程 30：引用与 Grounding](./30_citations_and_grounding.md)
- 返回总览：[根目录学习导航](../../README.md#-专题学习导航prompt--rag--skill)
