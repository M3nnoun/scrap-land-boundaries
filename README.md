---

# CIA World Factbook Data Extraction Project

## Overview
This project aims to extract data from the CIA World Factbook website regarding land boundaries of countries and store it in a structured format suitable for further analysis. The data will be extracted from the following URL: [https://www.cia.gov/the-world-factbook/field/land-boundaries/](https://www.cia.gov/the-world-factbook/field/land-boundaries/).

## Project Task
The main task of the project is to extract land boundary data and organize it into two separate file formats: XML and CSV.

### XML File: Land Boundary Details
This XML file will contain detailed information about land boundaries. Each country will be represented by a `<country>` element with child elements for country code, bordering countries, and border lengths.

### CSV File: Border Summary
This CSV file will contain summary information about land borders. Each row will represent a country, with columns for the country code, total border length, and any additional notes.

## Implementation
To achieve the project task, the following steps will be taken:
1. Scraping the required data from the CIA World Factbook website.
2. Parsing the extracted data and organizing it into the desired structure.
3. Writing the data into XML and CSV files using appropriate libraries in Python.
4. Verifying the accuracy and completeness of the extracted data.

## Usage
To use the project:
1. Clone the repository to your local machine.
2. Run the Python script to extract and organize the data.
3. Find the generated XML and CSV files in the project directory for further use.

## Dependencies
The project requires the following dependencies:
- Python 3.x
- BeautifulSoup (for web scraping)
- xml.etree.ElementTree (for XML file manipulation)
- csv (for CSV file manipulation)

## Author
MENNOUN Abdelfatah

## License
This project is licensed under the [MIT License](LICENSE).

---
