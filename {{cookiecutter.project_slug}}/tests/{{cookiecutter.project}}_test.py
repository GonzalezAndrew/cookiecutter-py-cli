from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

def test_main(capsys):
    {{ cookiecutter.project_slug }}.main(['hello'])

    out, err = capsys.readouterr()
    assert out == 'Hello, World\n'
    assert err == ''
