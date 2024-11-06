import process_data
import model
import synthetic_data

def main():
    # Splits data and converts them to PyTorch tensors
    process_data.main()
    # generates synthetic negative examples
    synthetic_data.main()
    # Runs model
    model.main()
    
if __name__ == "__main__":
    main()
