# Import the text parsing functions
import text_parsing_functions as tpf

def read_and_print_file(filepath, stopwords, names, replace):
    with open(filepath, 'r') as file:
        cleaned_lines_list = []
        for line in file:
            cleaned_line = tpf.line_cleaning_pipeline(line, stopwords, names, replace)
            cleaned_lines_list.append(cleaned_line)
        return cleaned_lines_list

def write_cleaned_lines_to_file(cleaned_lines, output_filepath):
    with open(output_filepath, mode='w', encoding='utf-8') as myfile:
        myfile.write('\n'.join(cleaned_lines))

if __name__ == '__main__':
    # Load stopwords from file
    stopwords = tpf.load_stopwords('data/stopwords.txt')

    # Character names that should be replaced with 'person'
    replace = 'person'
    names = set(
        ['suan', 'seongkyeong', 'yonsuk', 'seokwoo',
         'ingil', 'yonghuk', 'jinhee']
    )

    # Test the pipeline with a sample line
    line_text = (
      "pregnant wife Seong-kyeong, "
      "a high school baseball team, "
      "rich-yet-egotistical"
    )
    cleaned_text = tpf.line_cleaning_pipeline(line_text,
                                              stopwords,
                                              names,
                                              replace)

    #print(cleaned_text)

    filepath = 'data/train_to_busan_description.txt'
    cleaned_file_lines = read_and_print_file(filepath, stopwords, names, replace)

    # Save to file
    write_cleaned_lines_to_file(cleaned_file_lines, 'parsed/train_to_busan.txt')