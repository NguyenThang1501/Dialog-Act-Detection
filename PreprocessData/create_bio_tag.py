import json

def generate_bio_labels(sentence, span_info):
  bio_labels = ["O"] * len(sentence)

  # Gán nhãn cho từng ký tự
  for _, value_type, value, start, end in span_info:
      bio_labels[start] = f"B-{value_type}" 
      for i in range(start + 1, end):
          bio_labels[i] = f"I-{value_type}"  

  # Tách câu thành các từ
  tokens = sentence.split()
  token_labels = []

  # Ánh xạ lại nhãn ký tự sang nhãn từ
  current_char_idx = 0
  for token in tokens:
      token_length = len(token)
      token_bio_labels = bio_labels[current_char_idx]
      current_char_idx += token_length + 1

      # Lấy nhãn từ dựa trên ký tự đầu tiên
      if "B-" in token_bio_labels:
          token_labels.append(token_bio_labels)
      elif "I-" in token_bio_labels:
          token_labels.append(token_bio_labels)
      else:
          token_labels.append("O")

  return list(zip(tokens, token_labels))

def process_json_data(data):
    results = []
    for conversation in data:
        sentence = conversation[3]
        span_info = conversation[4].get("span_info", [])
        labels = generate_bio_labels(sentence, span_info)
        results.append({
            "sentence": sentence,
            "labels": labels
        })
    return results

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\train_xy.json", "r") as file:
    train_data = json.load(file)

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\val_xy.json", "r") as file:
    val_data = json.load(file)

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\test_xy.json", "r") as file:
    test_data = json.load(file)

train_results = process_json_data(train_data)
val_results = process_json_data(val_data)
test_results = process_json_data(test_data)

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\train_output.json", "w") as file:
    json.dump(train_results, file, indent=4)

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\val_output.json", "w") as file:
    json.dump(val_results, file, indent=4)

with open("C:\\Users\\Public\\NLP\\DialogActDetection\\test_output.json", "w") as file:
    json.dump(test_results, file, indent=4)
