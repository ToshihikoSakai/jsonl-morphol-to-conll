# jsonl-morphol-to-conll
In this repository, the jsonl file output by doccano is morphologically analyzed and converted into a conll file while retaining the tag span information.

## Example

### Morphologically analyze the text to create a new span
input: your doccano output jsonl file
output: output_morphorogical.jsonl

```bash
poetry run python jsonl-to-conll-morphorogical-to-conll.py docccano_output.jsonl

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