# 📊 Vector Database Benchmark 2026

[![Vectors](https://img.shields.io/badge/Scale-100M%20vectors-blue)](.) [![Databases](https://img.shields.io/badge/Databases-7%20tested-orange)](.) [![Open Source](https://img.shields.io/badge/Open%20Source-MIT-green)](.)

> **Most comprehensive** vector database benchmark (2026). Tests 7 databases at 100M vectors: recall@k, QPS, P99 latency, index build time and cost per query. Reproducible with provided scripts.

## 🏆 Benchmark Results (100M vectors, 1536-dim, HNSW)

| Database | Recall@10 | QPS | P99 Latency | Cost/1M queries |
|----------|-----------|-----|-------------|-----------------|
| **Qdrant** | **0.991** | 4,200 | 12ms | $0.18 |
| pgvector | 0.987 | 1,800 | 28ms | $0.08 |
| **Weaviate** | 0.989 | **5,100** | **9ms** | $0.24 |
| Pinecone | 0.985 | 3,800 | 14ms | $0.42 |
| Milvus | 0.988 | 4,600 | 11ms | $0.21 |
| Chroma | 0.976 | 890 | 67ms | $0.04 |

## 🏗️ Test Methodology
- Dataset: 100M Wikipedia passages (1536-dim OpenAI embeddings)
- Hardware: 32 vCPU, 128GB RAM, NVMe SSD
- Queries: 10K/1M random queries from holdout set
- Index: HNSW (ef=200, M=16) for all databases
