
import pandas as pd
import sys
import MeCab
import textspan


def WordsLabels(text, labels):

    words = []
    labels_list = []
    tuple_list = []

    for label in labels:
        start = label[0]
        end = label[1]
        tag = label[2]

        # Store labels and words
        labels_list.append(tag)
        words.append(text[start:end])
        tuple_list.append((start, end))

    return words, labels_list, tuple_list


def fix_new_span(original_span, new_span):
    span = []
    for index, line in zip(range(0, len(original_span), 1), original_span):
        for ns in new_span[index]:
            l = []
            l.append(ns[0])
            l.append(ns[1])
            l.append(line[2])
            span.append(l)
    return span


if __name__ == "__main__":
    tagger = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/ipadic")

    # Read jsonl file from doccano
    pdjson = pd.read_json(sys.argv[1], orient="records", lines=True)

    # Sort the elements "labels" in ascending order
    pdjson["label"] = [sorted(l) for l in pdjson["label"]]

    for index, row in pdjson.iterrows():

        # Store tag's words and labels
        words, labels, tuple = WordsLabels(row["text"], row["label"])

        # morphorogical analysis
        parsetext = tagger.parse(row["text"]).rstrip()
        pdjson["text"][index] = parsetext

        new_span = textspan.align_spans(tuple, row["text"], parsetext)

        pdjson["label"][index] = fix_new_span(row["label"], new_span)

    pdjson.to_json(
        "test.jsonl",
        orient='records',
        lines=True,
        force_ascii=False)
