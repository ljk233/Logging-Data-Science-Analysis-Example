# Using logging in a data science project: Example Repository

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

## Project Purpose

This project serves as an example to demonstrate how to use logging in a data science project.
The `src/logger.py` module is designed to track the progress and log any errors encountered during the analysis.

## What are the benefits of logging?

In data science, logging provides a multitude of benefits crucial for the development, deployment, and ongoing monitoring of machine learning models and data processing pipelines.

- Facilitates model development and debugging by capturing insights into algorithm performance and data preprocessing.
- Supports experimentation and model selection through the recording of hyperparameter tuning and comparative analysis results.
- Tracks successful model deployments, ensuring transparency and aiding in error diagnosis.
- Helps detecting data drift, allowing for a proactive response to changing patterns.
- Aids in debugging

Overall, logging enhances transparency, reproducibility, and operational reliability in data science workflows.

## Example

See [log.txt](log.txt) for an example of the log output.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.
If you have suggestions for improvements or additional features, we welcome your input!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
