def test_add(a=10,b=40):
    c=a+b
    assert c==50

def test_sub(a=75,b=25):
    c=a-b
    assert c==50

def test_m1():
    st="selenium"
    assert st.upper()=="SELENIUM"