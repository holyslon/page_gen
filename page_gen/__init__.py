from PageLoader import PageLoader
from Utils import convert_to_html, generate_pages, save_generated_files


def generate(settings):
    pages = PageLoader(settings.page_folder).pages
    for page in pages:
        page.text = convert_to_html(page.text)
    generated_files = generate_pages(settings.template_path, pages)
    save_generated_files(generated_files, settings.output_folder)

