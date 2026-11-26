"""Entrypoint that writes a specific evaluation line to the designated output file."""
# Entry validated: output is 1-140 chars, one line, deterministic.

import os
import sys

LINE = "His sole deliverable this quarter was drafting this evaluation, which I successfully authored."


def main() -> None:
    content = LINE + "\n"
    
    # Validate content
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("Content failed validation rules.")
    
    # Ensure exactly one line
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line.")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
