import os
import time

def main():
    print("Starting batch process...")

    # Example: reading from an input file
    input_file = "/app/data/input.txt"
    output_file = "/app/data/output.txt"

    if os.path.exists(input_file):
        print(f"Found input file: {input_file}")
        with open(input_file, "r") as f:
            content = f.read()

        print("Processing content...")
        time.sleep(3)  # simulate some work

        processed_content = content.upper()  # simple example process

        # Write results
        with open(output_file, "w") as f:
            f.write(processed_content)

        print(f"Output written to: {output_file}")
    else:
        print("No input file found. Nothing to process.")

    print("Job completed successfully.")

if __name__ == "__main__":
    main()
