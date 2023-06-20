# Regional Enterprise Parser
This parser is designed to extract names and addresses of enterprises from the selected region's HTML markup and save the retrieved data to an Excel file.

## Project Description
The parser performs the following actions:

1. HTML Markup Parsing: Extracting enterprise information from an HTML page.
2. Data Extraction: Obtaining the name and address of each enterprise.
3. Data Saving: Storing the obtained enterprise names and addresses in an Excel file.

## Installation and Usage

#### ЧTo install and use the parser, follow these steps:

1. Clone the repository to your local computer:
    ```shell
    git clone https://github.com/yourusername/enterprise-parser.git

2. Navigate to the project directory:
    ```shell
    cd enterprise-parser
   
3. Install the dependencies listed in the requirements.txt file:
    ```shell
    pip install -r requirements.txt

4. Run the parser:
    ```shell
    python main.py

After the parsing is completed, the obtained enterprise names and addresses will be saved in an Excel file using the Pandas library.

### Note
Before running the parser, ensure that you have access to the HTML page containing the enterprises and that the HTML element selectors are correctly specified.
For using the parser in different regions or on different websites, you may need to adjust the parser's parameters according to the HTML markup of the specific data source.

# Updated
Unfortunately, the website may be temporarily or permanently unavailable. In such cases, the parser will not be able to retrieve the enterprise data. Make sure to check the website's availability before running the parser.