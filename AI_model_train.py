import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Ensure model directory exists
os.makedirs("models", exist_ok=True)

# ------------------------------
# Generate synthetic training data
# ------------------------------
def generate_data(num_samples=1000):
    data = []
    for _ in range(num_samples):
        src = random.randint(1, 10)
        dest = random.randint(1, 10)
        load_src = random.randint(0, 100)
        load_dest = random.randint(0, 100)
        bandwidth = random.choice([10, 100, 1000])  # Mbps

        # Routing logic (mock): hop depends on destination
        next_hop = dest % 5 + 1

        # Loss logic: if load is high, packet might be lost
        loss = int((load_src + load_dest) > 160 or random.random() > 0.85)

        data.append([src, dest, load_src, load_dest, bandwidth, next_hop, loss])
    return pd.DataFrame(data, columns=["src", "dest", "load_src", "load_dest", "bandwidth", "next_hop", "loss"])

df = generate_data()

# ------------------------------
# Train Routing Predictor Model
# ------------------------------
X_route = df[["src", "dest", "load_src", "load_dest", "bandwidth"]]
y_route = df["next_hop"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_route, y_route, test_size=0.2, random_state=42)

route_model = RandomForestClassifier(n_estimators=100, random_state=42)
route_model.fit(X_train_r, y_train_r)

y_pred_r = route_model.predict(X_test_r)
print("✅ Routing Predictor Accuracy:", accuracy_score(y_test_r, y_pred_r))

# Save routing model
joblib.dump(route_model, "models/routing_predictor.pkl")

# ------------------------------
# Train Packet Loss Predictor Model
# ------------------------------
X_loss = X_route  # same input
y_loss = df["loss"]

X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(X_loss, y_loss, test_size=0.2, random_state=42)

loss_model = LogisticRegression(max_iter=200)
loss_model.fit(X_train_l, y_train_l)

y_pred_l = loss_model.predict(X_test_l)
print("✅ Packet Loss Predictor Accuracy:", accuracy_score(y_test_l, y_pred_l))

# Save loss model
joblib.dump(loss_model, "models/loss_predictor.pkl")

print("🎉 All models trained and saved in /models/")
