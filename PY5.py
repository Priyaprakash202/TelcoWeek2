import json

def main():
    # Load both JSON files -> Python dictionaries
    with open("data1.json") as f:
        data1 = json.load(f)

    with open("data2.json") as f:
        data2 = json.load(f)

    # Merge both dictionaries
    # If keys are same, data2 will overwrite data1
    merged_data = {**data1, **data2}

    # Save merged result to a file
    with open("merged.json", "w") as f:
        json.dump(merged_data, f, indent=4)

    print("Merged JSON saved to merged.json\n")
    print(json.dumps(merged_data, indent=4))


if __name__ == "__main__":
    main()
