import os
import re
import sys

import openai


def main(input_path, output_path=None):
    with open(input_path, 'r') as file:
        content = file.read()

    # parse the front matter and the content
    front_matter = []
    content = content.strip()
    if content.startswith('---'):
        front_matter, content = content.split('---', 2)[1:]
        front_matter = front_matter.strip().split('\n')
        content = content.strip()

    # split the content into paragraphs
    paragraphs = content.split('\n\n')

    # fix the grammar and punctuation
    fixed_paragraphs = []
    for p in paragraphs:

        # skip html tags, comments, and empty paragraphs
        if not p or not re.search(r'\w', p) or re.search(r'<[^>]+>', p):
            fixed_paragraphs.append(p)
            continue

        print("Checking paragraph: \n", p)
        fixed_paragraphs.append(fix_paragraph(p))

    # save the result to a file
    save_path = output_path or input_path
    with open(save_path, 'w') as file:
        # write the front matter
        for line in ['---', *front_matter, '---\n']:
            file.write(line + '\n')
        # write the content
        for p in fixed_paragraphs:
            file.write(p + '\n\n')

    print(f'Fixed content saved to {save_path}')


def fix_paragraph(paragraph):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    system_msg = "You only fixes the grammar and punctuation of provided text. Keep markdown and HTML tags as is."
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": paragraph}
        ]
    )
    print("Completion: ", completion)
    return completion.choices[0].message.content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a file path as an argument')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    main(input_path, output_path)
