import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix
from service.llm_service import classify_question

os.chdir(os.path.dirname(os.getcwd()))
folder_path = os.getcwd()
filename = 'classifier_test.csv'
full_path = os.path.join(folder_path, filename)


df = pd.read_csv(full_path)
df["y_true"] = df["y_true"].str.strip()


y_true = []
y_pred = []

for _, row in df.iterrows():

    question = row["question"]
    true_label = row["y_true"]

    pred = classify_question(question)

    y_true.append(true_label)
    y_pred.append(pred)
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