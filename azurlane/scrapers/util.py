def adjacent_cell_text_selector(text, element="th"):
    return "//{0}[normalize-space()='{1}']/following-sibling::td/descendant-or-self::*/text()".format(
        element, text
    )
