import subprocess
import time
import os
import statistics
import platform
import json
from typing import List

def run_command(command: str) -> float:
    """
    Runs a shell command and returns the time taken to execute it.

    Args:
        command (str): The command to run.

    Returns:
        float: The time taken to execute the command in seconds.
    """
    start_time = time.perf_counter()
    subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    end_time = time.perf_counter()
    return end_time - start_time

def write_file(filename: str, content: str) -> None:
    """
    Writes content to a file.

    Args:
        filename (str): The name of the file.
        content (str): The content to write to the file.
    """
    with open(filename, 'w') as f:
        f.write(content)

def benchmark(command: str, num_runs: int) -> List[float]:
    """
    Runs a benchmark by executing a command multiple times and recording the execution times.

    Args:
        command (str): The command to benchmark.
        num_runs (int): The number of times to run the command.

    Returns:
        List[float]: A list of execution times for each run.
    """
    return [run_command(command) for _ in range(num_runs)]

def print_stats(language: str, times: List[float]) -> None:
    """
    Prints statistical information about the execution times.

    Args:
        language (str): The name of the programming language.
        times (List[float]): A list of execution times.
    """
    print(f"{language} Statistics:")
    print(f"  Average time: {statistics.mean(times):.6f} seconds")
    print(f"  Median time:  {statistics.median(times):.6f} seconds")
    print(f"  Std Dev:      {statistics.stdev(times):.6f} seconds")
    print(f"  Min time:     {min(times):.6f} seconds")
    print(f"  Max time:     {max(times):.6f} seconds")
    print()

PYTHON_CODE = '''
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))
'''

GO_CODE = '''
package main

import "fmt"

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
    fmt.Println(fibonacci(30))
}
'''

RUST_CODE = '''
fn fibonacci(n: u32) -> u32 {
    if n <= 1 {
        return n;
    }
    fibonacci(n-1) + fibonacci(n-2)
}

fn main() {
    println!("{}", fibonacci(30));
}
'''

def get_executable_command(base_name: str) -> str:
    """
    Returns the executable command for a given base name, depending on the operating system.

    Args:
        base_name (str): The base name of the executable.

    Returns:
        str: The executable command.
    """
    if platform.system() == "Windows":
        return f"{base_name}.exe"
    return f"./{base_name}"

def main():
    """
    Main function to run the benchmark for Python, Go, and Rust implementations of the Fibonacci function.
    It writes the source code files, compiles the Go and Rust programs, runs the benchmarks, prints the statistics,
    saves the results to a JSON file, and cleans up the generated files.
    """
    write_file('fib.py', PYTHON_CODE)
    write_file('fib.go', GO_CODE)
    write_file('fib.rs', RUST_CODE)

    subprocess.run('go build fib.go', shell=True, check=True)
    subprocess.run('rustc fib.rs', shell=True, check=True)

    num_runs = 5
    python_times = benchmark('python fib.py', num_runs)
    go_times = benchmark(get_executable_command('fib'), num_runs)
    rust_times = benchmark(get_executable_command('fib'), num_runs)

    print_stats("Python", python_times)
    print_stats("Go", go_times)
    print_stats("Rust", rust_times)

    results = {
        "Python": {
            "average": statistics.mean(python_times),
            "median": statistics.median(python_times),
            "std_dev": statistics.stdev(python_times),
            "min": min(python_times),
            "max": max(python_times)
        },
        "Go": {
            "average": statistics.mean(go_times),
            "median": statistics.median(go_times),
            "std_dev": statistics.stdev(go_times),
            "min": min(go_times),
            "max": max(go_times)
        },
        "Rust": {
            "average": statistics.mean(rust_times),
            "median": statistics.median(rust_times),
            "std_dev": statistics.stdev(rust_times),
            "min": min(rust_times),
            "max": max(rust_times)
        }
    }

    with open('benchmark_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    os.remove('fib.py')
    os.remove('fib.go')
    os.remove('fib.rs')
    if platform.system() == "Windows":
        os.remove('fib.exe')
        if os.path.exists('fib.pdb'):
            os.remove('fib.pdb')
    else:
        os.remove('fib')

if __name__ == "__main__":
    main()