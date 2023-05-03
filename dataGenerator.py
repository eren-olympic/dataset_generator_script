import openai
import os
from dotenv import load_dotenv

load_dotenv(".env.local")

# 設置您的 OpenAI API 密鑰
openai.api_key = os.getenv("OPENAI_API_KEY")
# 讀取 category2.txt 文件中的所有行


def read_category_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# 向 OpenAI API 提出請求


def generate_items(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.1,
    )

    return response.choices[0].text.strip()

# 將生成的品項寫入 merchandise.txt 文件


def write_items_to_file(items, output_file):
    with open(output_file, "a", encoding="utf-8") as f_out:
        f_out.write(items + "\n")

# 主要流程


def main(input_file, output_file):
    categories = read_category_file(input_file)

    for category in categories:
        prompt = f"{category}，這是一個商品分類，列舉10項商品，using bullet points，格式為「- 商品, 完整分類」，舉例「- 蘋果, 食品 > 新鮮食材 > 水果」"
        generated_items = generate_items(prompt)
        write_items_to_file(generated_items, output_file)


if __name__ == "__main__":
    main("category2.txt", "merchandise.txt")
