# Bookline_Test_2

This application is for booking cars. It includes two endpoints, one for viewing a list of available cars in a given date and one for creating bookings.

---

## Prerequisites

There are two ways for running this application:

### Option 1: Without Docker
- Python 3.12
- `pip`

### Option 2: With Docker
- Docker

---

## Installation

### Option 1: Without Docker
1. Clone this repository:
   ```
   git clone https://github.com/Nico-Pardo-Medina/Bookline_Test_2.git
   cd Bookline_Test_2
   ```
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Start the FastAPI server:
    ```
    uvicorn main:app --reload
    ```
### Option 2: With Docker
1. Clone this repository:
    ```
    git clone https://github.com/Nico-Pardo-Medina/Bookline_Test_2.git
    cd Bookline_Test_2
    ```
2. Build the Docker image:
    ```
    docker build -t app .
    ```
3. Run the container:
    ```
    docker run app
    ```
---

## Endpoints
### /cars
- Description: Gets available cars for a specific date.
- Parameters: date with format yyyy-mm-dd.
- Response: A list of car IDs available on the specified date.
### /booking
- Description: Create a booking for a car on a specific date.
- Parameter: dictionary with "car-id" with an int and "date" with the format yyyy-mm-dd.
- Response: A success message or an error with details (it also adds the booking date to the dictionary of cars).

### Notes
- In the models folder there are pydantic BaseModels for the input parameters with validators so that the program returns an exception if the format is not correct.
- There is also a services folder with the functions that interact with the json to keep a separation between the request handling logic and the data operations.

---

## Testing

The tests can be run with docker and without it.

### Option 1: Without Docker
    ```
    set PYTHONPATH=. pytest
    ```
Sometimes it is enough only with `pytest` but sometimes the pythonpath may not be right.

### Option 2: With Docker
    ```
    docker build -t app .
    docker run app pytest  
    ```

### Mocked Data
To ensure that the original cars dictionary is not modified in the testing, some mocked data was used with pytest fixture and monkeypatch.