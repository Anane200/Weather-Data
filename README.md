# Weather-Data

A simple Python pipeline to fetch hourly weather data for **London** using the OpenWeatherMap API and save it to a CSV file for later analysis.

## 📌 Overview

This script:
- Retrieves real-time weather data every hour
- Extracts temperature, humidity, wind speed, and pressure
- Appends the data to a CSV file (`Weather_data.csv`)
- Logs indefinitely using the `schedule` library

## 🧰 Tech Stack

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [pandas](https://pypi.org/project/pandas/)
- [schedule](https://pypi.org/project/schedule/)
- OpenWeatherMap API

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-data-logger.git
cd weather-data-logger
