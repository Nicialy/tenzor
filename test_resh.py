from resheto import proverka_prost


class TestResheto:

    def test_prostoe_2_t(self):
        assert proverka_prost(2) == True

    def test_prostoe_4_f(self):
        assert proverka_prost(4) == False
        
    def test_prostoe_25_f(self):
        assert proverka_prost(25) == False