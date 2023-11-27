# Using logs during the data science pipepline

This repository contains a simple example project that demonstrates how to track the progress of a simple data modelling pipeline using a custom logging process.

## Project Structure

```plaintext
root/
├── src/
│   ├── __init__.py
│   ├── logger.py     # Custom logging module
├── log.txt           # Log file where events are records.
├── main.py           # Script to perform modelling
├── README.md         # This file
└── requirements.txt  # Project dependencies
```

## Getting Started

1. Clone the Repository

   ```bash
   git clone https://github.com/your-username/linear-regression-analysis.git
   cd linear-regression-analysis
   ```

2. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis**

   ```bash
   python main.py
   ```

## Logging

The project uses a custom logging system to track the progress of the linear regression analysis.
Logs are stored in `log.txt` and include information such as data loading, data splitting, model training, predictions, and evaluation.
An example log file can be seen in [log.txt](log.txt)

## Example log

See [example_log]

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. If you have suggestions for improvements or additional features, we welcome your input!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
