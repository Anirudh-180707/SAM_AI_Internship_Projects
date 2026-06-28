import pandas as pd

# Load dataset
df = pd.read_csv("zomato.csv")

# Keep only required columns
columns = [
    "name",
    "location",
    "cuisines",
    "rate",
    "votes",
    "approx_cost(for two people)"
]

df = df[columns]

# Remove missing values
df = df.dropna()

# Clean rating column
df["rate"] = df["rate"].astype(str).str.replace("/5", "", regex=False)
df = df[df["rate"] != "NEW"]
df = df[df["rate"] != "-"]

df["rate"] = df["rate"].astype(float)

# Clean cost column
df["approx_cost(for two people)"] = (
    df["approx_cost(for two people)"]
    .astype(str)
    .str.replace(",", "")
)

df["approx_cost(for two people)"] = pd.to_numeric(
    df["approx_cost(for two people)"],
    errors="coerce"
)

df = df.dropna()

print("=" * 55)
print("Restaurant Recommendation System")
print("=" * 55)

while True:

    cuisine = input("\nEnter Cuisine (Example: North Indian, Chinese, Pizza): ").strip()

    recommendations = df[
        df["cuisines"].str.contains(cuisine, case=False, na=False)
    ]

    if recommendations.empty:
        print("\nNo restaurants found for that cuisine.")
    else:
        recommendations = recommendations.sort_values(
            by=["rate", "votes"],
            ascending=False
        )

        print("\nTop Recommended Restaurants\n")

        for index, row in recommendations.head(5).iterrows():
            print(f"Restaurant : {row['name']}")
            print(f"Location   : {row['location']}")
            print(f"Cuisine    : {row['cuisines']}")
            print(f"Rating     : {row['rate']}/5")
            print(f"Votes      : {int(row['votes'])}")
            print(f"Cost for Two: ₹{int(row['approx_cost(for two people)'])}")
            print("-" * 50)

    choice = input("\nSearch another cuisine? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using the Restaurant Recommendation System!")
        break