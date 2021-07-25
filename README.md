# Django Weather App REST API

## Description
A REST API built in Django that accepts city names and number of days to provide a temperature forecast. 
Consumes API from www.weatherapi.com/. Computes data and outputs maximum, minimum, average, and median temperatures. 

## Assumptions
1. Users want temperature forecasts only and not historical data
2. Computations are for total period of time, i.e. max temp over 72-hour period, not per day
3. English users who only want metric values

## Usage and Examples
### How To
**Request -**
ping the API at http://127.0.0.1:8000/api/locations/{city}/?days={number_of_days},
where user inputs desired name of city in {city} and period of time in {number_of_days}

**Response -** outputs response as such: {
    "maximum": value,
    "minimum": value,
    "average": value,
    "median": value,
    }

### Examples
1. Cape Town 1-day forecast:
http://127.0.0.1:8000/api/locations/cape town/?days=1
2. London 3-day forecast:
http://127.0.0.1:8000/api/locations/london/?days=3

## Calculations
Calculations are made over the entire time period. For example, querying a 2-day forecast will return the max, min,
mean, and median temperature over the whole 48-hour period. Calculations are made through use of the Python Statistics 
Module. All values rounded to one decimal place.

##Limitations
1. Does not handle special characters such as - or . or ü,
Will not work for cities such as München, Washington D.C., Nur-Sultan.
2. Can only forecast up to 3 days due to free tier limitations at www.weatherapi.com/
3. Some special cases of duplicated city names around the world: Cape Town, South Africa ≠ Capetown, USA
or San Francisco, USA ≠ Sanfrancisco, Venezuela. The temperature outputs are different!
4. More of an extension, if only the city is provided (incomplete url) or no days are provided,
   then number of days is set to default value of 1.
5. Forecast starts from first hour of today. A 1-day request made at 10am will provide a 24-hour forecast,
   however only 14 hours are in the future. 