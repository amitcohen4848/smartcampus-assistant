import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from service.llm_service import classify_question

os.chdir(os.path.dirname(os.getcwd()))
folder_path = os.getcwd()
filename = 'classifier_test.csv'
full_path = os.path.join(folder_path, filename)


df = pd.read_csv(full_path)
df["y_true"] = df["y_true"].str.strip()

# compute question length
df["length"] = df["question"].apply(lambda x: len(x.split()))


y_true = []
y_pred = []
lengths = []

for _, row in df.iterrows():

    question = row["question"]
    true_label = row["y_true"]

    pred = classify_question(question)

    y_true.append(true_label)
    y_pred.append(pred)
    lengths.append(len(question.split()))

    print(question, " -> ", pred)
# ---- Metrics ----

labels = [
    "student_courses",
    "course_name",
    "course_lecturer",
    "course_time",
    "course_classroom",
    "course_description",
    "technical_support",
    "unknown"
]



results_df = pd.DataFrame({
    "question": df["question"],
    "true": y_true,
    "pred": y_pred,
    "length": lengths
})

bins = [0,3,6,10,20]
labels_len = ["1-3","4-6","7-10","11+"]

results_df["length_group"] = pd.cut(results_df["length"], bins=bins, labels=labels_len)

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, labels=labels))

cm = confusion_matrix(y_true, y_pred, labels=labels)

# Plot heatmap
plt.figure(figsize=(10,8))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels,
    linewidths=1
)

plt.xlabel("Predicted Intent")
plt.ylabel("True Intent")
plt.title("Intent Classification Confusion Matrix")

plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()


print("\nAccuracy by prompt length:\n")

for group in labels_len:
    group_df = results_df[results_df["length_group"] == group]

    if len(group_df) == 0:
        continue

    acc = accuracy_score(group_df["true"], group_df["pred"])

    print(f"{group} words → accuracy: {acc:.2f} (samples={len(group_df)})")