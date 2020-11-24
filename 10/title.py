def format_name(f_name: str, l_name: str) -> str:
    """
        Return the title case version of the full name string
    """
    assert isinstance(f_name, str) and isinstance(
        l_name, str), "The arguments should be strings!"
    assert len(f_name) > 0, "First Name is empty!"
    assert len(l_name) > 0, "Last Name is empty!"

    return " ".join([f_name, l_name]).title()


print(format_name("doctor", "house"))
