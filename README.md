# Benchmarking Script

This repository contains a benchmarking script (`bench.py`) that compares the performance of the Fibonacci function implemented in Python, Go, and Rust. The script performs the following tasks:

1. Writes the source code for the Fibonacci function in Python, Go, and Rust to separate files.
2. Compiles the Go and Rust programs.
3. Runs the benchmarks by executing each program multiple times and records the execution times.
4. Prints statistical information about the execution times.
5. Saves the benchmark results to a JSON file.
6. Cleans up the generated files.

## Requirements

-   Python 3.x
-   Go
-   Rust

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/kWAYTV/py-go-rust-benchmark.git
    cd py-go-rust-benchmark
    ```

2. Ensure you have Python, Go, and Rust installed on your system.

3. Run the benchmarking script:
    ```sh
    python bench.py
    ```

## Output

The script will output statistical information about the execution times for each language, including the average time, median time, standard deviation, minimum time, and maximum time. The results will also be saved to a `benchmark_results.json` file.
