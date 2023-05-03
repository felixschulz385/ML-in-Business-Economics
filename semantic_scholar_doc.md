# Semantic Scholar Open Research Corpus (S2ORC)
## Documentation for use at the Chair of Marketing - University of Tübingen

> Author: Felix Schulz

S2ORC is the largest structured database on academic text in existence. It contains information on more than 81M individual publications and lists paper name, authors, publication venue, date, citations and abstracts, as well as several identifiers. For a complete list of fields, check out the dataset on [api.semanticscholar.org](https://api.semanticscholar.org/api-docs/datasets) or [huggingface.co](https://huggingface.co/datasets/allenai/s2orc/tree/main).

As part of a research project at the chair I downloaded and prepared the data for analysis. The downloaded data was moved to Prof. Papies home repository on the bwUniCluster. If one seeks to work with this data, they should request a copy of these files or download the files themselves.

The data used at the chair is based on an openly available dump hosted on [huggingface.co](https://huggingface.co/datasets/allenai/s2orc/tree/main). At the time of writing, the dump represented the S2ORC in December 2020 and is therefore not perfectly up-to-date. Newer data is available directly from Semantic Scholar under their conditions.

Based on this dump I created a subset of data on FT50(2023) papers between 2010 and 2020. The resulting file *ft50_data.csv* is available on request.

### Challenges in handling the data

The primary challenge when working with the data is its sheer size of more than 500GB. It is highly advised to utilize the resources of the bwUniCluster with frameworks like Arrow or Dask when handling the entire collection.

The paper abstracts are collected from various sources and contain a large range of irregular unicode characters. Before being able to parse the downloaded and extracted JSON files, I needed to normalize the files to remove linebreaks in the abstracts. After several attempts, I settled with a brute-force approach, turning the files into their hex-representation and deleting problematic HEX-codes of potential linebreaks. Anyone trying to download the data themselves is encouraged to find a more subtle approach.