def read_txt_file(filepath):
    with open(filepath) as f:
        lines = f.read()
    return lines


def lines_to_list(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    return lines


def make_invite(filepath, contents):
    with open(filepath, "w") as f:
        f.write(contents)


if __name__ == "__main__":
    inv_letter = read_txt_file("Input/Letters/starting_letter.txt")
    names = lines_to_list("Input/Names/invited_names.txt")
    names = [name.strip() for name in names]
    placeholder = "[name]"
    for name in names:
        edited_inv_letter = inv_letter.replace(placeholder, name)
        make_invite(f"Output/ReadyToSend/letter_for_{name}.txt", edited_inv_letter)
