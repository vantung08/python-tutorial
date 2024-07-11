from main.main import main

class TestClass:
    def test_main(self):
        assert main() == "Hello World"
    
    def test_char_main(self):
        assert "H" in main()



