# **Category-based Merchandise Generator**

This project generates a list of merchandise items based on predefined categories using the OpenAI API. The category information is stored in the **`category2.txt`** file and the generated merchandise list will be saved in the **`merchandise.txt`** file.

## **Prerequisites**

- Python 3.6 or higher
- OpenAI Python library
- python-dotenv library

## **Installation**

1. Clone the repository or download the project files.
2. Install the required Python libraries:
    
    ```
    pip install openai python-dotenv
    ```
    
3. Set up your OpenAI API key in the **`.env.local`** file:
    
    ```
    OPENAI_API_KEY="your_openai_api_key"
    ```
    

Replace **`your_openai_api_key`** with your actual OpenAI API key.

## **Usage**

1. Run the **`transformat.py`** script to transform the **`category.txt`** file into the **`category2.txt`** file:
    
    ```
    python transformat.py
    ```
    
2. Run the **`dataGenerator.py`** script to generate the merchandise list based on the categories in the **`category2.txt`** file:
    
    ```
    python dataGenerator.py
    ```
    
3. The generated merchandise list will be saved in the **`merchandise.txt`** file.

## **Files**

- **`category.txt`**: Contains the initial category information.
- **`transformat.py`**: Transforms the **`category.txt`** file into the **`category2.txt`** file.
- **`category2.txt`**: Contains the transformed category information.
- **`dataGenerator.py`**: Generates the merchandise list based on the categories in the **`category2.txt`** file.
- **`merchandise.txt`**: Contains the generated merchandise list.
- **`.env.local`**: Stores the OpenAI API key as an environment variable.

## **License**

This project is licensed under the **[MIT License](https://opensource.org/licenses/MIT)**.
