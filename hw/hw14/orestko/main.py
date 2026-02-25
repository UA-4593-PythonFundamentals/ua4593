import unittest
import functions_with_errors as lib

class TestFunctions(unittest.TestCase):
    def test_greeting_by_name_name(self):
        self.assertEqual(lib.greeting_by_name("Ivan"), "Hello Ivan!")

    def test_get_symbol_position_text_symbol_when_symbol_incorrect(self):
        self.assertEqual(lib.get_symbol_position("Python", "yy"), "Error! Symbol can be string with only one letter")

    def test_get_symbol_position_text_symbol_with_success(self):
        self.assertEqual(lib.get_symbol_position("Python", "y"), 2)

    def test_get_symbol_position_text_symbol_when_symbol_was_not_found(self):
        self.assertEqual(lib.get_symbol_position("Python", "z"), "Not found")

    def test_merge_dict1_dict2_dict1_immutability(self):
        d1, d2 = {"a": 1}, {"b": 2}
        lib.merge(d1, d2)
        self.assertEqual(d1, {"a": 1})

    def test_merge_dict1_dict2_dict2_immutability(self):
        d1, d2 = {"a": 1}, {"b": 2}
        lib.merge(d1, d2)
        self.assertEqual(d2, {"b": 2})

    def test_merge_dict1_dict2(self):
        self.assertEqual(lib.merge({"a": 1}, {"b": 2}), {"a": 1, "b": 2})

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    
    for test in suite:
        result = unittest.TestResult()
        test.run(result)
        
        
        raw_name = test._testMethodName
        
       
        display_name = raw_name.replace("test_", "").replace("_", " ")
        
       
        display_name = display_name.replace("name name", "greeting_by_name(name)")
        display_name = display_name.replace("text symbol", "get_symbol_position(text, symbol)")
        display_name = display_name.replace("dict1 dict2", "merge(dict1, dict2)")
        
        if result.wasSuccessful():
            print(f"Test {display_name} is Passed")
        else:
            print(f"Test {display_name} is Failed")