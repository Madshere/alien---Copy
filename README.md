

## How To Use This Application
To use the virtual alien pet application, follow these steps:
- Install the required packages and dependencies by running `pip install -r requirements.txt`.
- Create a virtual environment by running `python3 -m venv venv` and activate it with `source venv/bin/activate`.
- Run the application by running `python main.py`.

The application will open a window displaying the virtual pet and the visualization for the grounding techniques with controls for feeding, playing games, and interacting with the pet using touch and voice commands. The visualization for grounding techniques also includes customizable 3D guided breathing techniques for stress and anxiety relief. 

## Expected Output
When the application runs successfully, you should see a window displaying the virtual pet and the visualization for grounding techniques with options for feeding, playing games, and interacting with the pet using touch and voice commands.


## Test Coverage Report
To measure the effectiveness of our tests, we use the Python `coverage` module to generate a coverage report. This report provides a detailed breakdown of the different areas and functions tested and the amount of code coverage achieved. To generate and view the test coverage report, follow these steps:
- Make sure to activate the virtual environment by running `source venv/bin/activate`.
- Install the coverage module by running `pip install coverage`.
- Generate the test coverage report by running `coverage report -m`.
The report displays several metrics, including:
- `lines`: the total number of lines in the code.
- `miss`: the number of lines not covered by tests.
- `cover`: the percentage of code coverage achieved. The higher the number, the better the code coverage. A score of 100% means that all lines of code have been tested.

Achieving good test coverage is essential for ensuring the quality and maintainability of our code as it makes it easier to identify and fix potential errors and bugs.