# ==============================
# STEP 0: Imports
# ==============================
import pandas as pd
import numpy as np


# ==============================
# STEP 1: Load Dataset
# ==============================
df = pd.read_csv("data/Chennai_RealEstate.csv")

print("Dataset loaded successfully")
print(df.head())


# ==============================
# STEP 2: DATA CLEANING
# ==============================

# Ensure target variable has no missing values
df = df.dropna(subset=["Estimated Sale Price (INR)"])

# Fill numeric missing values with median
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values
categorical_cols = df.select_dtypes(include=["object", "string"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Data cleaning completed")


# ==============================
# STEP 3: DATA PREPARATION / FEATURE ENGINEERING
# ==============================

df["Parking_Code"] = df["Parking Facility Yes/No"].map({
    "Yes": 1,
    "No": 0
})

df["Furnishing_Code"] = df["Furnishing Status"].map({
    "Unfurnished": 0,
    "Semi-Furnished": 1,
    "Fully Furnished": 2
})

df["Property_Type_Code"] = df["Property Type"].map({
    "Apartment": 0,
    "Villa": 1,
    "Independent House": 2
})

df["Facing_Code"] = df["Facing"].map({
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
})

print("Data preparation completed")


# ==============================
# STEP 4: VERIFY ENCODING
# ==============================

print(df[[
    "Property Type", "Property_Type_Code",
    "Furnishing Status", "Furnishing_Code",
    "Parking Facility Yes/No", "Parking_Code",
    "Facing", "Facing_Code"
]].head())

