from harvesttext import HarvestText
import os
import re
import tqdm


def replace_punctuation(text):
    punctuation = {'，': ',', '！': '!', '？': '?',
                   '；': ';', '：': ':', '“': '"', '”': '"',
                   '‘': "'", '’': "'", "（": "(", "）": ")",
                   "【": "[", "】": "]", "《": "<", "》": ">"}
    pattern = re.compile('|'.join(punctuation.keys()))
    return pattern.sub(lambda x: punctuation[x.group()], text)


def word_dir(folder_path):
    file_list = []
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".txt"):
                file_list.append(filepath)
    return file_list


def chinese_clean(content):
    ht = HarvestText()
    content = replace_punctuation(content)
    pattern = re.compile("[^./?!;<>[]()\"\'\u4e00-\u9fa5a-zA-Z0-9]+")
    content = pattern.sub("", content)
    content = ht.clean_text(content)
    content = ht.clean_text(content, norm_html=True)
    content = re.sub(r'[\x00-\x1f\x7f-\xff]', ' ', content)
    contents = ht.cut_sentences(content)
    return contents


if __name__ == '__main__':
    txt_files = word_dir("./data")
    with open("sentences.txt", 'w') as output_sentences_file:
        for file_path_index in tqdm.tqdm(range(len(txt_files))):
            txt_file = txt_files[file_path_index]
            with open(txt_file, 'r') as test_file:
                data = test_file.read()
                result = chinese_clean(data)
                for sentence in result:
                    if len(sentence) > 6:
                        output_sentences_file.write(sentence + "\n")

