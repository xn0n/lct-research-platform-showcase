"""Synthetic public illustration; no private backend, collectors, ML, or network."""
import json


def main():
    documents = [
        {"id": "demo-doc-1", "title": "Вымышленный обзор учебного датчика"},
        {"id": "demo-doc-2", "title": "Вымышленная заметка о прототипе"},
    ]
    claims = [
        {"text": "В учебном сценарии описан прототип", "document": "demo-doc-2"},
    ]
    document_ids = {document["id"] for document in documents}
    result = {
        "example": "synthetic-showcase",
        "analysis": "static invented fixtures; no real model",
        "stages": ["request", "synthetic-documents", "illustrative-claims", "reference-check"],
        "documents": documents,
        "claims": claims,
        "references_exist_in_example": all(claim["document"] in document_ids for claim in claims),
        "scientific_quality": "not-evaluated",
        "network_requests": 0,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
