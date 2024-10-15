import time

def timing_decorator(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record end time
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def add_numbers(a, b):
    """Calculate the sum of two numbers and print the result."""
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result

@timing_decorator
def read_and_write_numbers(input_file, output_file):
    """Read two numbers from a file and write the sum to another file."""
    try:
        with open(input_file, 'r') as infile:
            # Read the first line and split into two integers
            a, b = map(int, infile.readline().strip().split())
        result = a + b
        with open(output_file, 'a') as outfile:
            outfile.write(f"The sum of {a} and {b} is: {result}\n")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except ValueError:
        print("Error: Input file must contain two integers separated by space.")

# Example usage
if __name__ == "__main__":
    # Test the add_numbers function
    add_numbers(10, 20)

    # Test the read_and_write_numbers function
    # Ensure input.txt exists with two integers
    read_and_write_numbers('input.txt', 'output.txt')
