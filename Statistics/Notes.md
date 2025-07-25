# What is Statistics?

## Definition
**Statistics** is the science of collecting, organizing, analyzing, interpreting, and presenting data to make informed decisions or draw meaningful conclusions in the face of uncertainty.

---

## Types of Statistics

### 1. Descriptive Statistics
- **Purpose**: Summarize and describe features of a dataset.
- **Tools**:
  - Measures of Central Tendency (Mean, Median, Mode)
  - Measures of Dispersion (Variance, Standard Deviation, Range)
  - Data Visualization (Histograms, Box Plots, Scatter Plots)

### 2. Inferential Statistics
- **Purpose**: Make predictions or generalizations about a population based on sample data.
- **Tools**:
  - Hypothesis Testing (t-tests, ANOVA)
  - Confidence Intervals
  - Regression Analysis

---

## Why is Statistics Important?
1. **Data-Driven Decisions**: Empowers businesses, governments, and researchers to base choices on evidence.
2. **AI/ML Foundation**: Critical for training models, evaluating performance (e.g., accuracy, precision).
3. **Risk Assessment**: Quantifies uncertainty (e.g., probability in finance, healthcare).

# Population vs Sample

## 1. Population
- **Definition**: The complete set of all individuals, items, or data points of interest in a study.
- **Characteristics**:
  - Often too large to measure entirely (e.g., all humans, all trees in a forest).
  - Described by **parameters** (fixed numerical values, usually unknown).
- **Examples**:
  - All smartphones sold in 2024.
  - Every student enrolled at Harvard University.

## 2. Sample
- **Definition**: A subset of the population, selected for actual data collection.
- **Characteristics**:
  - Used to **estimate** population parameters (via statistics).
  - Must be **representative** (avoid bias) and **random**.
- **Examples**:
  - 1,000 smartphone users surveyed about battery life.
  - 200 Harvard students' GPAs analyzed.
### Why Sampling?
1. **Cost-Effective**: Cheaper than surveying entire populations.
2. **Time-Saving**: Faster data collection.
3. **Practicality**: Some populations are infinite (e.g., all possible website visits).
---
# Types of Data in Statistics

## 1. Qualitative (Categorical) Data
**Definition**: Non-numerical data representing categories or labels.

### Subtypes:
- **Nominal Data**: 
  - No inherent order.
  - Examples: 
    - Gender (Male/Female/Other)
    - Colors (Red, Blue, Green)
- **Ordinal Data**:
  - Ordered categories but intervals are uneven.
  - Examples:
    - Survey ratings (Poor, Fair, Good, Excellent)
    - Education level (High School, Bachelor's, PhD)

## 2. Quantitative (Numerical) Data
**Definition**: Numerical data that can be measured.

### Subtypes:
- **Discrete Data**:
  - Countable, finite values (often integers).
  - Examples:
    - Number of students in a class
    - Cars in a parking lot
- **Continuous Data**:
  - Infinite possible values (measurements).
  - Examples:
    - Height/Weight
    - Temperature
      
# Measures of Central Tendency
## Definition
Measures of central tendency are statistical values that summarize a dataset by identifying the central point around which data clusters. They help simplify complex data into a single representative value.

## 1. Mean (Arithmetic Average)
### Definition
The mean is the sum of all values divided by the number of values.
### Formula
 - Mean = (Sum of all values) / (Total number of values)
### Key Properties
- **Sensitive to outliers** (extreme values skew the mean)
- **Best for normally distributed data** (symmetrical datasets)
### Example
**Dataset**: `[10, 20, 30, 40, 50]`  
**Calculation**:Mean = (10 + 20 + 30 + 40 + 50) / 5 = 150 / 5 = 30

## 2. Median (Middle Value)
### Definition
The median is the middle value in an ordered dataset.
### Steps to Calculate
1. Arrange data in ascending order
2. For odd number of values: Pick the middle one
3. For even number of values: Average the two middle values
### Key Properties
- **Robust to outliers** (unaffected by extreme values)
- **Preferred for skewed distributions**
### Examples
- **Odd dataset**: `[5, 7, 9, 12, 15]` → Median = `9`
- **Even dataset**: `[5, 7, 9, 12]` → Median = `(7 + 9)/2 = 8`

## 3. Mode (Most Frequent Value)
### Definition
The mode is the value that appears most frequently in a dataset.
### Key Properties
- Works for **categorical & numerical data**
- **No mode** if all values are unique
- **Multimodal** if multiple values tie for highest frequency
### Examples
- `[2, 3, 3, 5, 7]` → Mode = `3`
  
# Measures of Dispersion
## Definition
Measures of dispersion quantify how **spread out** or **varied** a dataset is. They complement measures of central tendency by describing data variability.

## Common Measures

### 1. Range
**Definition**: Difference between maximum and minimum values  
**Formula**:  Range = Max(X) - Min(X)
**Example**:  
`[10, 20, 30, 40, 50]` → Range = 50 - 10 = 40  
**Limitation**: Highly sensitive to outliers

### 2. Variance (σ²/s²)
**Definition**: Average of squared deviations from mean  
**Formulas**:  
- Population Variance:  σ² = Σ(xᵢ - μ)²/N
- Sample Variance:  s² = Σ(xᵢ - x̄)²/(n-1)
  
### 3. Standard Deviation (σ/s)
**Definition**: Square root of variance (in original units)  
**Formula**:  σ = √σ² or s = √s²

### 4. Interquartile Range (IQR)
**Definition**: Range of middle 50% of data (Q3 - Q1)  
**Calculation**:
1. Sort data
2. Find Q1 (25th percentile) and Q3 (75th percentile)
3. IQR = Q3 - Q1
   
## When to Use Which?
- **Range**: Quick estimate of spread
- **Variance/Standard Deviation**: For normally distributed data
- **IQR**: For skewed data or when outliers exist
  ## When to Use Which?
- **Range**: Quick estimate of spread
- **Variance/Standard Deviation**: For normally distributed data
- **IQR**: For skewed data or when outliers exist
  
# Outliers 
## Definition
Data points that **differ significantly** from other observations.
## Detection Methods
1. **IQR Method** (Most Common):
Lower Bound = Q1 - 1.5×IQR
Upper Bound = Q3 + 1.5×IQR

# Five Number Summary
## Definition
A robust data summary consisting of 5 key percentiles:
1. **Minimum** (0th percentile)
2. **Q1** (25th percentile)
3. **Median** (50th percentile)
4. **Q3** (75th percentile)
5. **Maximum** (100th percentile)
