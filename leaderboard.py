import pandas as pd

# Load scores from the game results file
def load_scores(file_path):
    try:
        scores_df = pd.read_csv(file_path, names=["Score"])
        return scores_df
    except FileNotFoundError:
        print("No scores file found. Play the game first!")
        return pd.DataFrame(columns=["Score"])

# Generate and display leaderboard
def display_leaderboard(scores_df):
    print("\n🏆 LEADERBOARD 🏆")
    print("-" * 20)
    top_scores = scores_df.sort_values(by="Score", ascending=False).head(5)  # Top 5 scores
    for rank, score in enumerate(top_scores['Score'], start=1):
        print(f"{rank}. {score} points")
    print("-" * 20)

# Main function
def main():
    scores_file = "dice_results.csv"  # Path to the results file
    scores_df = load_scores(scores_file)

    if not scores_df.empty:
        display_leaderboard(scores_df)
    else:
        print("No scores available to display. Go play the game!")

if __name__ == "__main__":
    main()
