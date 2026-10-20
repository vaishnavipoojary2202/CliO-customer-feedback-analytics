# CLIO — Intelligent Customer Feedback Analytics and Query Assistant for E-commerce

CLIO is an NLP-powered customer-feedback analytics system that transforms e-commerce reviews into structured insights and evidence-grounded answers. The initial analysis domain is **smartphone reviews**, allowing aspect-based sentiment analysis (ABSA) to focus on device-specific aspects.

## Objectives

- Analyze customer review sentiment.
- Identify aspect-level opinions about smartphone features such as battery, camera, display, performance, build quality, software, connectivity, audio, price/value, and reliability.
- Categorize complaints and discover recurring topics.
- Prepare analytical data for dashboards and trend analysis.
- Support natural-language queries through a Retrieval-Augmented Generation (RAG) assistant grounded in retrieved review evidence.

## Planned workflow

1. Data ingestion and validation.
2. Smartphone identification from product metadata, followed by sampling and manual quality checks.
3. Text and record preprocessing.
4. NLP analysis: overall sentiment, aspect extraction and sentiment, complaint categorization, topic discovery, and entity extraction.
5. Structured analytics using PostgreSQL.
6. Semantic indexing using SBERT embeddings and ChromaDB.
7. Hybrid retrieval and evidence-grounded answer generation.
8. Evaluation of model quality and answer faithfulness.

## Dataset

The initial source is the [Amazon Reviews 2023 dataset](https://amazon-reviews-2023.github.io/), using the **Cell Phones and Accessories** review and product-metadata files. This category includes accessories as well as phones; products must be filtered and sampled titles checked before describing the resulting dataset as smartphone-only.

- [Review file (JSONL.GZ)](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_2023/raw/review_categories/Cell_Phones_and_Accessories.jsonl.gz)
- [Product metadata file (JSONL.GZ)](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_2023/raw/meta_categories/meta_Cell_Phones_and_Accessories.jsonl.gz)

The raw data are intentionally not included in this repository. Put downloaded files in `data/raw/` locally. Check the dataset's citation and usage terms before redistributing raw reviews or using them commercially.

## Planned technology stack

- Python and Pandas
- Hugging Face Transformers and evaluated NLP models
- Sentence-BERT (SBERT) embeddings
- PostgreSQL
- ChromaDB
- LangChain and a selected LLM provider
- Dashboard and visualization tooling to be finalized

Model choices will be benchmarked against the project data rather than assumed in advance.

## Repository structure

```text
.
├── data/
│   ├── raw/          # downloaded source files; ignored by Git
│   └── processed/    # generated datasets; ignored by Git
├── notebooks/        # exploratory notebooks
├── src/              # project modules
├── tests/            # automated tests
├── outputs/           # generated artifacts; ignored by Git
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Local setup (macOS / VS Code)

```bash
git clone https://github.com/vaishnavipoojary2202/CliO-customer-feedback-analytics.git
cd CliO-customer-feedback-analytics
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Place the downloaded compressed files under `data/raw/`. Do not commit datasets, API keys, local databases, model weights, or vector-store files.

## Development status

Initial setup and data inspection utilities are being added. Smartphone filtering, sampling, preprocessing, ABSA, dashboards, and RAG remain to be implemented and evaluated.

## Citation

Cite Amazon Reviews 2023 as directed by its [official dataset page](https://amazon-reviews-2023.github.io/).
