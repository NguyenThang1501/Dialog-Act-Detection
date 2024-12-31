import json
import os


data_dir = "C:\Users\Public\NLP\DialogActDetection\MultiWOZ_2.2"

def extract_xy_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    dialog_path = "C:\Users\Public\NLP\DialogActDetection\MultiWOZ_2.2\dialog_acts.json"
    with open(dialog_path, 'r', encoding='utf-8') as f:
        dialog_data = json.load(f)

    xy_pairs = []
    
    for dialog in data:
        dialog_id = dialog["dialogue_id"]
        
        for turn in dialog['turns']:  
            speaker = turn.get("speaker")
            turn_id = turn.get('turn_id')  
            utterance = turn.get("utterance", "")
            dialog_get = dialog_data.get(dialog_id)
            dialog_act = dialog_get.get(turn_id)
            xy_pairs.append((dialog_id,turn_id,speaker, utterance, dialog_act))  

    return xy_pairs

def extract_xy_from_multiwoz(data_dir):
    xy_data = []

    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        if file_name.endswith('.json'):
            xy_data.extend(extract_xy_from_file(file_path))

    return xy_data

train_data_dir = os.path.join(data_dir, "train")
x_y_train = extract_xy_from_multiwoz(train_data_dir)

val_data_dir = os.path.join(data_dir, "dev")
x_y_val = extract_xy_from_multiwoz(val_data_dir)

test_data_dir = os.path.join(data_dir, "test")
x_y_test = extract_xy_from_multiwoz(test_data_dir)

print(f"Số lượng mẫu train: {len(x_y_train)}")
print(f"Số lượng mẫu val: {len(x_y_val)}")
print(f"Số lượng mẫu test: {len(x_y_test)}")

with open("train_xy2.json", "w", encoding="utf-8") as f:
    json.dump(x_y_train, f, ensure_ascii=False, indent=4)

with open("val_xy2.json", "w", encoding="utf-8") as f:
    json.dump(x_y_val, f, ensure_ascii=False, indent=4)

with open("test_xy2.json", "w", encoding="utf-8") as f:
    json.dump(x_y_test, f, ensure_ascii=False, indent=4)

