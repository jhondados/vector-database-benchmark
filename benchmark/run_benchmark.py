"""Vector database benchmark runner."""
import time
import numpy as np
from typing import List, Dict, Any

class VectorDBBenchmark:
    def __init__(self, vectors: np.ndarray, queries: np.ndarray, ground_truth: np.ndarray):
        self.vectors = vectors
        self.queries = queries
        self.ground_truth = ground_truth

    def compute_recall_at_k(self, results: List[List[int]], k: int = 10) -> float:
        hits = sum(len(set(r[:k]) & set(gt[:k])) for r, gt in zip(results, self.ground_truth))
        return hits / (len(self.queries) * k)

    def benchmark_qdrant(self, host: str = "localhost", port: int = 6333) -> Dict:
        from qdrant_client import QdrantClient
        from qdrant_client.models import Distance, VectorParams, PointStruct
        client = QdrantClient(host=host, port=port)
        client.recreate_collection("bench", vectors_config=VectorParams(size=self.vectors.shape[1], distance=Distance.COSINE))
        # Index
        t0 = time.perf_counter()
        client.upload_points("bench", [PointStruct(id=i, vector=v.tolist()) for i, v in enumerate(self.vectors)])
        index_time = time.perf_counter() - t0
        # Query
        t0 = time.perf_counter()
        results = [[r.id for r in client.search("bench", q.tolist(), limit=10)] for q in self.queries[:1000]]
        qps = 1000 / (time.perf_counter() - t0)
        return {"db": "qdrant", "recall@10": self.compute_recall_at_k(results), "qps": qps, "index_time_s": index_time}
