from pathlib import Path

def list_samples():

    sample_folder = Path("samples")

    samples = []

    for file in sample_folder.iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            samples.append(file.name)

    return samples


if __name__ == "__main__":
    print("Testing style tool...")
    print(list_samples())
