from question3 import make_oven, alchemy_combine

def test_alchemy_combine():

    assert alchemy_combine(
        make_oven(),
        ["lead", "mercury"],
        5000
    ) == ['Boiledlead', 'Boiledmercury']  

    assert alchemy_combine(
        make_oven(),
        ["water", "air"],
        -100
    ) == ['Frozenwater', 'Frozenair'] 

    assert alchemy_combine(
        make_oven(),
        ["cheese", "dough", "tomato"],
        150
    ) == ['Boiledcheese', 'Boileddough', 'Boiledtomato'] 
