import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ""
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text += char

    cleaned_text = cleaned_text.replace('\n', ' ')
    cleaned_text = ''.join(cleaned_text.split('   '))
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)


delete_html_tags('draft.html')
