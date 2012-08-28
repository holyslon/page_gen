import markdown2
from mako.template import Template
import os


def convert_to_html(text_in_markdown):
    return markdown2.markdown(text_in_markdown)


def apply_template(template, page, pages):
    return template.render_unicode(name=page.name, text=page.text, pages=pages).encode('utf-8', 'replace')


def create_template(template_file):
    return Template(filename=template_file, input_encoding='utf-8')


def generate_pages(template_file, pages):
    template = create_template(template_file)
    return [(page.html_path, apply_template(template, page, pages)) for page in pages]


def save_generated_files(generated_files, root_folder):
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
    for (file_name, content) in generated_files:
        output_path = os.path.join(root_folder, file_name)
        print output_path
        with open(output_path, "w") as f:
            f.write(content)
