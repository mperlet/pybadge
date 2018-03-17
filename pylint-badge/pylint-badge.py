def main():
    import argparse

    from pylint.lint import Run
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file_to_lint")
    args = parser.parse_args()
    file_to_lint = args.file_to_lint
    
    score = round(Run([file_to_lint], exit=False).linter.stats['global_note'], 2)
    
    with open('badge-template.svg', 'r') as f:
        template = f.read()
    
    color_ok = "#44cc11"
    color_warning = "#dfb317"
    color_red = "#e05f44"
    
    if float(score) < 3.0:
        color = color_red
    elif float(score) >= 3.0 and float(score) < 7.0:
        color = color_warning
    else:
        color = color_ok
    
    with open("pylint.svg", 'w') as score_file:
        score_file.write(template.format(score=score, color=color))
