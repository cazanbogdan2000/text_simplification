import os
import pandas as pd

FOLDER_NAME = 'wikilarge'

SOURCE_DIRECTORY = f'../../raw_data/{FOLDER_NAME}'

DEST_DIRECTORY = f'../../processed_data/{FOLDER_NAME}'

source_list = os.listdir(SOURCE_DIRECTORY)

source_list = list(map(lambda x: x.split('.'), source_list))

source_list = list(filter(lambda x: x[-1] in ['src', 'dst'], source_list))

source_list = list(map(lambda x: '.'.join(x), source_list))

for i in range(0, len(source_list), 2):
    dest = source_list[i]
    src = source_list[i+1]
    
    src_file = open(f'{SOURCE_DIRECTORY}/{src}', 'r', encoding='utf-8')
    dest_file = open(f'{SOURCE_DIRECTORY}/{dest}', 'r', encoding='utf-8')
    
    csv_file_df = pd.DataFrame(columns=['initial_text', 'simplified_text'])
        
    csv_file_df['initial_text'] = list(map(lambda x: x[:-1], src_file.readlines()))
    csv_file_df['simplified_text'] = list(map(lambda x: x[:-1], dest_file.readlines()))

    src_file.close()
    dest_file.close()

    processed_file_name = '.'.join(dest.split('.')[:-1])
    
    csv_file_df.to_csv(f'{DEST_DIRECTORY}/{processed_file_name}.tsv', index=False, sep='\t')