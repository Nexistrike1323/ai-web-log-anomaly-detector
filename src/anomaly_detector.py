import pandas as pd
import re
from sklearn.ensemble import IsolationForest

# Path to the web server log file
LOG_FILE_PATH = "../data/access.log"

# List to store parsed log data
parsed_logs = []

# Regex pattern to extract useful fields from Apache logs
log_pattern = r'(\d+\.\d+\.\d+\.\d+).+"(GET|POST) (.+?) HTTP.*" (\d+)'

# Step 1: Read and parse the log file line by line
with open(LOG_FILE_PATH, "r") as log_file:
    for line in log_file:
        match = re.search(log_pattern, line)

        # If the line matches the expected log format
        if match:
            ip_address = match.group(1)
            http_method = match.group(2)
            requested_endpoint = match.group(3)
            status_code = int(match.group(4))

            parsed_logs.append([
                ip_address,
                http_method,
                requested_endpoint,
                status_code
            ])

# Step 2: Convert parsed data into a DataFrame
logs_df = pd.DataFrame(
    parsed_logs,
    columns=["ip_address", "method", "endpoint", "status_code"]
)

# Step 3: Feature engineering
# Count number of requests per IP address
request_features = (
    logs_df
    .groupby("ip_address")
    .size()
    .reset_index(name="request_count")
)

# Step 4: Train Isolation Forest model to detect anomalies
anomaly_model = IsolationForest(
    contamination=0.2,
    random_state=42
)

request_features["anomaly_flag"] = anomaly_model.fit_predict(
    request_features[["request_count"]]
)

# Step 5: Convert model output to readable labels
request_features["traffic_type"] = request_features["anomaly_flag"].apply(
    lambda value: "Suspicious" if value == -1 else "Normal"
)

# Step 6: Save results to output file
output_path = "../output/anomaly_results.csv"
request_features.to_csv(output_path, index=False)

print("Anomaly detection completed successfully.")
print(f"Results saved to {output_path}")
