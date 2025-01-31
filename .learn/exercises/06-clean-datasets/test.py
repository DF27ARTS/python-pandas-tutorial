import io, os, sys, pytest, re


@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas\s*as\s*pd")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the print function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "print" in content

@pytest.mark.it("Use the head function")
def test_head_function_used():
    f = open('app.py')
    content = f.read()
    assert "head" in content

@pytest.mark.it("You should be reading the csv file located at .learn/assets/us_baby_names_right.csv to create your DataFrame")
def test_reading_csv():
    f = open('app.py')
    content = f.read()
    assert ".learn/assets/us_baby_names_right.csv" in content and 'read_csv' in content

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """   Unnamed: 0     Id     Name  Year Gender State  Count
0       11349  11350     Emma  2004      F    AK     62
1       11350  11351  Madison  2004      F    AK     48
2       11351  11352   Hannah  2004      F    AK     46
3       11352  11353    Grace  2004      F    AK     44
4       11353  11354    Emily  2004      F    AK     41
"""

