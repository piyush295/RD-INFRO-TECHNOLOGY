def log_message(message):
    print(f"[LOG] {message}")

def calculate_metrics(true_labels, predictions):
    from sklearn.metrics import confusion_matrix, classification_report
    cm = confusion_matrix(true_labels, predictions)
    report = classification_report(true_labels, predictions)
    return cm, report

def visualize_data(data, title="Data Visualization"):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Samples")
    plt.ylabel("Values")
    plt.show()