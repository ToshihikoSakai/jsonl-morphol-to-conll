# jsonl-morphol-to-conll
In this repository, the jsonl file output by doccano is morphologically analyzed and converted into a conll file while retaining the tag span information.

## Example

### Morphologically analyze the text to create a new span

* input: your doccano output jsonl file
* output: output_morphorogical.jsonl

```bash
poetry run python jsonl-to-conll-morphorogical-to-conll.py docccano_output.jsonl

```

for example, morphologically analyze the text to create a new span
```
{"id": 266708, "text": "明日、東京都に行きます", "label": [[3, 6, "LOC"]]}
->
{"id":266708,"text":"明日 、 東京 都 に 行き ます","label":[[5,7,"LOC"],[8,9,"LOC"]]}
```

### jsonl to conll
```bash
cat output_morphorogical.jsonl | sed 's/label/labels/g' > output_morphorogical_labels.jsonl   

poetry run jsonl-to-conll output_morphorogical_labels.jsonl output.conll   
```

### transform I-tag
At present, all are B-tags. Transform appropriate tag to I-tag.

```bash
poetry run python transform_I-tag.py output.conll > output_new.conll 

```

for example, you can get conll file.
```
明日 O
、 O
東京 B-LOC
都 I-LOC
に O
行き O
ます O
```