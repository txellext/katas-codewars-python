import codewars_test as test
from solution import boolean_to_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")
        
@test.describe("Random Tests")
def random_tests():
    
    from random import choice
    
    for _ in range(100):
        s = choice([True, False])
        expected = str(s)
        @test.it(f"testing for boolean_to_string({s})")
        def test_case():
            test.assert_equals(boolean_to_string(s), expected)