def find_element_with_text(root, element, text):
    return root.xpath("//{0}[normalize-space()='{1}']".format(element, text))


def extract_text(root):
    return " ".join(filter(lambda x: x.strip(), root.css("*::text").getall()))


def get_adjacent_cell_text(root, text):
    return extract_text(find_element_with_text(root, "th", text).css("*+td"))
