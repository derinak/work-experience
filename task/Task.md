# Performance Monitoring

## Project Overview

Build a Python-based monitoring system to detect performance anomalies and changepoints in Cisco router metrics, preventing network outages before they happen. This project applies Netflix's anomaly detection and changepoint techniques (from their performance regression detection system) to network infrastructure monitoring.

## Getting Started

### Setup Instructions

```bash
# Navigate to project directory
cd <path>

# Create virtual environment
python3 -m venv .env

# Activate the environment
source .env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

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

- `csv` or built-in `open()` for file reading - [documentation](https://www.w3schools.com/python/ref_module_csv.asp)
- `statistics` for mean/stdev calculations - [documentation](https://www.w3schools.com/python/module_statistics.asp)
- `math` for sqrt and other mathematical operations - [documentation](https://www.w3schools.com/python/module_math.asp)
- `matplotlib.pyplot` for plotting visualization - [documentation](https://www.w3schools.com/python/matplotlib_pyplot.asp)
- `pandas` for data manipulation and analysis - [documentation](https://www.w3schools.com/python/pandas/default.asp)

## Technical Implementation Details

### Anomaly Detection Algorixthm

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

## Real-World Data

The project uses actual XR-E (Cisco Extended Router) performance data collected over a 6-month period from production systems. This data is anonymized and consists of three main metric categories:

### Data Location
`task/real_data/` - Contains anonymized production performance data

### Metric 1: Reload Time Performance
Tracks the time required for router reload operations across 3 different platforms.

**Files:**
- `metric1_run1.pq` - Platform 1 reload times
- `metric1_run2.pq` - Platform 2 reload times  
- `metric1_run3_high_variance.pq` - Platform 3 (VXR simulator - high variance/noisy)

**Structure:** Each row contains:
- `date`: Timestamp of the reload operation
- `total_seconds`: Total reload time in seconds

**Breakdown Files:**
- `metric1_breakdown_run1.pq` - Platform 1 phase breakdown
- `metric1_breakdown_run2.pq` - Platform 2 phase breakdown
- `metric1_breakdown_run3_high_variance.pq` - Platform 3 phase breakdown

**Breakdown Structure:** Multiple rows per date, one for each phase:
- `date`: Timestamp of the reload operation
- `phase`: Phase identifier (Phase 1, Phase 2, etc.)
- `start_time`: Phase start time (seconds from reload start)
- `duration`: Phase duration in seconds
- `end_time`: Phase end time (seconds from reload start)

### Metric 2: Install Performance
Tracks installation operation times for software upgrades and SMU (Software Maintenance Update) installations.

**Summary Files:**
- `metric2_large_run1.pq` - Full upgrade install times
- `metric2_small_run1.pq` - SMU install times

**Structure:** Each row contains:
- `date`: Timestamp of the install operation
- `total_seconds`: Total install time in seconds

**Breakdown Files:**
- `metric2_large_breakdown_run1.pq` - Upgrade install phase breakdown
- `metric2_small_breakdown_run1.pq` - SMU install phase breakdown

**Breakdown Structure:** Multiple rows per date, one for each phase:
- `date`: Timestamp of the install operation
- `phase`: Phase identifier
- `start_time`: Phase start time (seconds from install start)
- `duration`: Phase duration in seconds
- `end_time`: Phase end time (seconds from install start)

### Metric 3: Memory Usage
Tracks total memory consumption over time.

**Files:**
- `metric3_run1.pq` - Memory usage data

**Structure:** Each row contains:
- `date`: Timestamp of the measurement
- `total_size`: Total memory usage in bytes

### Working with the Data

The data is stored in Parquet format (`.pq` files), which is a columnar storage format optimized for analytics. To read it:

```python
import pandas as pd

# Load reload time data
df = pd.read_parquet('task/real_data/metric1_run1.pq')

# Load phase breakdown data
breakdown_df = pd.read_parquet('task/real_data/metric1_breakdown_run1.pq')

# Example: Calculate average reload time
avg_reload_time = df['total_seconds'].mean() / 60  # Convert to minutes
print(f"Average reload time: {avg_reload_time:.2f} minutes")
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
