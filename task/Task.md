# Performance Monitoring

## Project Overview

Build a Python-based monitoring system to detect performance anomalies and changepoints in Cisco router metrics, preventing network outages before they happen. This project applies Netflix's anomaly detection and changepoint techniques (from their performance regression detection system) to network infrastructure monitoring.

## Background

Cisco routers are networking devices that forward data packets between computer networks, acting as traffic controllers for the internet. They power a huge portion of the world's internet infrastructure, used by businesses, governments, and ISPs worldwide. When a router fails, businesses lose connectivity, operations stop, and revenue is lost (potentially thousands of dollars per minute).

## Key Concepts

### 1. Anomaly Detection
- **Definition**: A data point that is unusually far from the mean
- **Method**: Dynamic threshold using mean + n×σ (n standard deviations)
- **Purpose**: Catches sudden spikes immediately (real-time detection)
- **Formula**: `Threshold = μ + (n × σ)` where `μ` is mean and `σ` is standard deviation

### 2. Changepoint Detection
- **Definition**: A point where the data's behavior fundamentally changes
- **Method**: E-Divisive-inspired approach (simplified version)
- **Purpose**: Finds subtle, persistent changes and filters out one-time spikes
- **Key Difference**: Anomaly = one weird spike; Changepoint = permanent shift

## Requirements

### Minimum Requirements (Core Features)

1. **Data Loading**
   - Read Cisco router performance data from CSV file

2. **Anomaly Detection**
   - Implement dynamic threshold method: `threshold = mean + (n × std_dev)`
   - Parameters:
     - Window size (m): Last 30-40 data points
     - Threshold multiplier (n): 3-4 standard deviations
   - Analyze at least 2 metrics: CPU and Memory
   - Return indices of detected anomalies

3. **Changepoint Detection**
   - Implement simplified E-Divisive method
   - Split data into "before" and "after" groups
   - Find splits with maximum difference between groups
   - Minimum segment size: 10 data points
   - Filter nearby changepoints (keep only if 10+ points apart)

4. **Output**
   - Print indices of detected anomalies for each metric
   - Print indices of detected changepoints
   - Print summary statistics (mean, std dev) for each metric

5. **Visualization**
   - Plot all monitored metrics with:
     - Main data line
     - Anomalies marked with red circles
     - Changepoints marked with green vertical lines
   - Save plot to file

### Allowed Libraries

- `csv` or built-in `open()` for file reading
- `statistics` for mean/stdev calculations
- `math` for sqrt and other mathematical operations
- `matplotlib.pyplot` for plotting visualization

## Technical Implementation Details

### Anomaly Detection Algorithm

```python
def detect_anomalies(data, window_size=40, n_sigma=4):
    
    """
    Args:
        data: List of numeric values
        window_size: Number of recent points to use (m)
        n_sigma: Number of standard deviations (n)
    
    Returns:
        List of indices where anomalies were detected
    """
    # For each point after window_size:
    #   1. Get recent window of data
    #   2. Calculate mean and std_dev
    #   3. Set threshold = mean + (n_sigma * std_dev)
    #   4. If current value > threshold, mark as anomaly
```

### Changepoint Detection Algorithm

```python
def detect_changepoints(data, min_size=10):
    """
    Args:
        data: List of numeric values
        min_size: Minimum size for each segment
    
    Returns:
        List of changepoint indices
    """
    # For each possible split point:
    #   1. Split data into before/after groups
    #   2. Calculate mean and std_dev for each group
    #   3. Check if means are significantly different
    #      (difference > 2 * combined_std)
    #   4. Keep split with maximum divergence
    #   5. Filter nearby changepoints
```

## Bonus Challenges (Extensions)

### 1. Severity Scoring
Calculate overall router health score based on multiple metrics:
```python
def router_severity(cpu, memory):
    """Calculate overall router health score."""
    # Return: "CRITICAL", "WARNING", or "NORMAL"
```

### 2. Sustained Anomaly Detection
Find runs of consecutive anomalies (more concerning than single spikes):
```python
def find_sustained_anomalies(anomaly_indices, min_consecutive=3):
    """Find runs of consecutive anomalies."""
```

### 3. Automatic Alerting
Generate alerts with context and recommended actions:
```python
def generate_alert(timestamp, cpu, memory, loss, severity):
    """Generate router alert with context."""
```
