from {{ cookiecutter.project_slug }} import main

def test_main(capsys):
    main.main(['hello'])

    out, err = capsys.readouterr()
    assert out == 'Hello, World!\n'
    assert err == ''
